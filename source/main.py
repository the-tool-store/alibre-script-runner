import sys
import clr
import os
import glob
import os as _os
import glob as _glob

def _alibre_program_dir():
    override = _os.environ.get("ALIBRE_PROGRAM_DIR")
    if override and _os.path.isdir(override):
        return override
    roots = []
    base = _os.environ.get("ProgramFiles", "C:\\Program Files")
    for candidate in _glob.glob(_os.path.join(base, "Alibre Design *", "Program")):
        if "BETA" in candidate.upper():
            continue
        if _os.path.isfile(_os.path.join(candidate, "AlibreX.dll")):
            roots.append(candidate)
    return sorted(roots)[-1] if roots else None

ALIBRE_PROGRAM_DIR = _alibre_program_dir()

def _add_alibre_paths():
    if not ALIBRE_PROGRAM_DIR:
        return
    script_dir = _os.path.join(ALIBRE_PROGRAM_DIR, "Addons", "AlibreScript")
    for candidate in (ALIBRE_PROGRAM_DIR, script_dir,
                      _os.path.join(script_dir, "PythonLib"),
                      _os.path.join(script_dir, "PythonLib", "site-packages")):
        if _os.path.isdir(candidate) and candidate not in sys.path:
            sys.path.append(candidate)

_add_alibre_paths()

clr.AddReference("AlibreX")
clr.AddReference("AlibreScriptAddOn")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
clr.AddReference("System.Runtime.InteropServices")

import AlibreX
from System.Runtime.InteropServices import Marshal
from System.Windows.Forms import (Application, Form, MenuStrip, ToolStripMenuItem,
                                  MessageBox, MessageBoxButtons, MessageBoxIcon,
                                  FolderBrowserDialog, DialogResult)
from System.Drawing import Size
from System.Threading import Thread, ThreadStart, ApartmentState

import AlibreScript
from AlibreScript.API import *

base_path = r'T:\a\alibre-script-runner'
main_form = None

try:
    alibre = Marshal.GetActiveObject("AlibreX.AutomationHook")
    root = alibre.Root
except:
    MessageBox.Show("Alibre Design not found. Please ensure Alibre Design is running.", "Connection Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
    sys.exit()

Win = Windows()

def execute_script(script_path):
    """
    Reads and executes the Python script from the given file path.
    The script is executed in the global scope, giving it access to all
    initialized Alibre objects and imported modules (e.g., 'alibre', 'Part', 'Win').
    """
    try:
        with open(script_path, 'r') as f:
            script_code = f.read()
        exec(script_code, globals())
    except Exception as ex:
        error_message = "An error occurred while running the script:\n'{0}'\n\n{1}".format(os.path.basename(script_path), str(ex))
        Win.ErrorDialog(error_message, "Script Execution Error")

def set_base_path_click(sender, e):
    """
    Event handler for the 'Set Base Path' menu item. Opens a folder browser
    dialog and updates the base_path if a new folder is selected.
    """
    global base_path, main_form

    dialog = FolderBrowserDialog()
    dialog.Description = "Select the base folder containing your script directories (scripts, prototypes, etc.)"
    dialog.SelectedPath = base_path

    if dialog.ShowDialog(main_form) == DialogResult.OK:
        base_path = dialog.SelectedPath
        create_menus(main_form)

def create_menus(form):
    """
    Dynamically creates menu items by scanning specified subdirectories for .py files.
    This function can be called multiple times to refresh the menu structure.
    """
    menu_strip = None
    for control in form.Controls:
        if isinstance(control, MenuStrip):
            menu_strip = control
            break

    if menu_strip is None:
        menu_strip = MenuStrip()
        form.MainMenuStrip = menu_strip
        form.Controls.Add(menu_strip)

    menu_strip.Items.Clear()

    file_menu = ToolStripMenuItem("File")
    set_path_item = ToolStripMenuItem("Set Base Path...")
    set_path_item.Click += set_base_path_click
    file_menu.DropDownItems.Add(set_path_item)
    menu_strip.Items.Add(file_menu)

    menu_definitions = {
        "Scripts": "scripts",
        "Prototypes": "prototypes",
        "R&D Tools": "randd",
        "Examples": "examples"
    }

    for menu_title, folder_name in menu_definitions.items():
        script_folder_path = os.path.join(base_path, folder_name)

        if not os.path.isdir(script_folder_path):
            continue

        script_files = glob.glob(os.path.join(script_folder_path, '*.py'))

        if not script_files:
            continue

        top_level_menu = ToolStripMenuItem(menu_title)

        for script_path in sorted(script_files):
            script_name = os.path.basename(script_path)
            menu_item_label = os.path.splitext(script_name)[0]

            item = ToolStripMenuItem(menu_item_label)
            item.Click += lambda sender, e, path=script_path: execute_script(path)
            top_level_menu.DropDownItems.Add(item)

        menu_strip.Items.Add(top_level_menu)

    root_script_files = [f for f in glob.glob(os.path.join(base_path, '*.py'))
                         if os.path.isfile(f) and os.path.basename(f).lower() != 'main.py']

    if root_script_files:
        root_scripts_menu = ToolStripMenuItem("Root Scripts")

        for script_path in sorted(root_script_files):
            script_name = os.path.basename(script_path)
            menu_item_label = os.path.splitext(script_name)[0]

            item = ToolStripMenuItem(menu_item_label)
            item.Click += lambda sender, e, path=script_path: execute_script(path)
            root_scripts_menu.DropDownItems.Add(item)

        menu_strip.Items.Add(root_scripts_menu)

def run_winforms():
    """
    Creates and runs the main application window in a dedicated STA thread.
    """
    global main_form
    form = Form()
    main_form = form

    form.Text = "Alibre Script Runner"
    form.Size = Size(800, 600)

    create_menus(form)

    Application.Run(form)

def main():
    """
    Main entry point. Runs the WinForms application in a separate thread
    with the Single-Threaded Apartment (STA) state, which is required for WinForms.
    """
    t = Thread(ThreadStart(run_winforms))
    t.SetApartmentState(ApartmentState.STA)
    t.Start()
    t.Join()

main()

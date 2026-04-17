import sys
import clr
import os
import glob

# Add references to Alibre Design and .NET assemblies
sys.path.append(r"C:\Program Files\Alibre Design 28.0.2.28126\Program")
sys.path.append(r"C:\Program Files\Alibre Design 28.0.2.28126\Program\Addons\AlibreScript")
clr.AddReference("AlibreX")
clr.AddReference("AlibreScriptAddOn")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
clr.AddReference("System.Runtime.InteropServices")

# Import Alibre and .NET classes
import AlibreX
from System.Runtime.InteropServices import Marshal
from System.Windows.Forms import (Application, Form, MenuStrip, ToolStripMenuItem, 
                                  MessageBox, MessageBoxButtons, MessageBoxIcon,
                                  FolderBrowserDialog, DialogResult)
from System.Drawing import Size
from System.Threading import Thread, ThreadStart, ApartmentState

# Add paths for Alibre Script libraries
sys.path.append(r"C:\PROGRAM FILES\Alibre Design 28.0.2.28126\PROGRAM\ADDONS\ALIBRESCRIPT\PythonLib")
sys.path.append(r"C:\PROGRAM FILES\Alibre Design 28.0.2.28126\PROGRAM\ADDONS\ALIBRESCRIPT")
sys.path.append(r"C:\PROGRAM FILES\Alibre Design 28.0.2.28126\PROGRAM\ADDONS\ALIBRESCRIPT\PythonLib\site-packages")

# Import Alibre Script API
import AlibreScript
from AlibreScript.API import *

# --- Global Variables ---
# Default path for scripts. This can be changed at runtime via the UI.
base_path = r'T:\a\alibre-script-runner'
# A global reference to the main form, needed for dialogs.
main_form = None

# Establish connection to the running Alibre Design application
try:
    alibre = Marshal.GetActiveObject("AlibreX.AutomationHook")
    root = alibre.Root
except:
    MessageBox.Show("Alibre Design not found. Please ensure Alibre Design is running.", "Connection Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
    sys.exit()

# Instantiate the Windows helper class for dialogs
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
        # Execute the script's code within the current global context
        exec(script_code, globals())
    except Exception as ex:
        # Display a detailed error message if the script fails
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
    dialog.SelectedPath = base_path # Start browsing from the current base path

    # Show the dialog. The 'main_form' argument makes it modal to our app.
    if dialog.ShowDialog(main_form) == DialogResult.OK:
        base_path = dialog.SelectedPath
        # Re-create all menus to reflect the new path
        create_menus(main_form)

def create_menus(form):
    """
    Dynamically creates menu items by scanning specified subdirectories for .py files.
    This function can be called multiple times to refresh the menu structure.
    """
    # Find existing menu strip or create a new one if it's the first run.
    menu_strip = None
    for control in form.Controls:
        if isinstance(control, MenuStrip):
            menu_strip = control
            break
            
    if menu_strip is None:
        menu_strip = MenuStrip()
        form.MainMenuStrip = menu_strip
        form.Controls.Add(menu_strip)
        
    # Clear all existing items to prepare for a full refresh
    menu_strip.Items.Clear()

    # --- Create the static 'File' menu ---
    file_menu = ToolStripMenuItem("File")
    set_path_item = ToolStripMenuItem("Set Base Path...")
    set_path_item.Click += set_base_path_click
    file_menu.DropDownItems.Add(set_path_item)
    menu_strip.Items.Add(file_menu)

    # --- Create dynamic menus from folders ---
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

    # --- Create menu for scripts in the root of the base_path ---
    # Find scripts in the base directory, excluding the runner itself.
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
    main_form = form # Store a global reference to the form instance
    
    form.Text = "Alibre Script Runner"
    form.Size = Size(800, 600)

    create_menus(form) # Create the initial set of menus

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

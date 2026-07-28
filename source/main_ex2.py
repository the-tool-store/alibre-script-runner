import sys
import clr
import os
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

import AlibreX
import AlibreScript
from AlibreScript.API import *

clr.AddReference("System.Runtime.InteropServices")
from System.Runtime.InteropServices import Marshal

from System.Windows.Forms import Application, Form, MenuStrip, ToolStripMenuItem
from System.Threading import Thread, ThreadStart, ApartmentState
from System.Drawing import Size
alibre = Marshal.GetActiveObject("AlibreX.AutomationHook")
root = alibre.Root

Win = Windows()

EXAMPLES_DIR = r"C:\Path\To\Example\Scripts"
example_files = [
    "Assembly-Constraints.py", "Bolt-Creator.py", "Calculating-Length-of-Curves.py",
    "Cap-Screw-ISO-4762-Bolts.py", "Copy-sketch.py", "Create-Reference-Planes-Axes-and-Points.py",
    "Create-and-Modify-Global-Parameters.py", "Creating-a-3D-Sketch-with-a-Spline-and-an-Arc.py",
    "Creating-a-Cylinder-Between-Two-Points.py", "Creating-and-Manipulating-Assemblies.py",
    "Custom-Values-and-Settings-Window.py", "Default-Reference-Geometry.py", "Drop-Down-Lists.py",
    "Everyone-Loves-a-Slinky.py", "Gear-Example.py", "Geodesic-Dome-Reference-Geometry.py",
    "Getting-User-Input.py", "Helical-spring.py", "Import-points-from-a-CSV-file-rotate-them-and-connect-into-a-polyline.py",
    "Importing-Files.py", "Joint-Creator.py", "List-All-Parts-in-an-Assembly-and-Sub-Assemblies.py",
    "Lofting-with-a-Guide-Curve.py", "Midplane-Extrusion.py", "Mobius-Strip.py", "Modify-an-Existing-Part.py",
    "Parameters-with-Units.py", "Pocket-Hole-Creator.py", "Polygon-Incircle.py", "Profile-and-Sweep-Path.py",
    "Reading-from-a-Spreadsheet.py", "Rectangular-hollow-formed-profiles.py", "Reference-Geometry.py",
    "Scaling-a-Sketch.py", "Servo-Cam.py", "Slice-a-Part.py", "Square-hollow-formed-profiles.py",
    "Supressing-Unsupressing-and-Removing-Features.py", "Tool-Cutting.py", "Triangle.py",
    "Type-11-flanges-according-to-BS-EN-1092-PN16.py", "Units.py", "Useful-Dialogs.py", "Wave-washer.py",
    "Working-with-Configurations.py"
]
def run_example(script_name):
    script_path = os.path.join(EXAMPLES_DIR, script_name)
    if os.path.exists(script_path):
        try:
            exec(open(script_path).read(), globals())
            Win.InfoDialog("Executed: {0}".format(script_name), "Execution Complete")
        except Exception as e:
            Win.ErrorDialog("Error executing {0}: {1}".format(script_name, str(e)), "Execution Error")
    else:
        Win.ErrorDialog("File not found: {0}".format(script_name), "File Error")
def create_menus(form):
    menu_strip = MenuStrip()
    examples_menu = ToolStripMenuItem("Example Scripts")

    for example in example_files:
        menu_item = ToolStripMenuItem(example)
        menu_item.Click += lambda sender, e, script=example: run_example(script)
        examples_menu.DropDownItems.Add(menu_item)

    menu_strip.Items.Add(examples_menu)
    form.MainMenuStrip = menu_strip
    form.Controls.Add(menu_strip)
def run_winforms():
    form = Form()
    form.Text = "Alibre Script Example Runner"
    form.Size = Size(600, 400)
    create_menus(form)
    Application.Run(form)
def main():
    t = Thread(ThreadStart(run_winforms))
    t.SetApartmentState(ApartmentState.STA)
    t.Start()
    t.Join()
main()

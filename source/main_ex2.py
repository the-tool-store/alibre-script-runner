import sys
import clr
import os
sys.path.append(r"C:\Program Files\Alibre Design 28.0.2.28126\Program")
sys.path.append(r"C:\Program Files\Alibre Design 28.0.2.28126\Program\Addons\AlibreScript")
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
            Win.InfoDialog(f"Executed: {script_name}", "Execution Complete")
        except Exception as e:
            Win.ErrorDialog(f"Error executing {script_name}: {str(e)}", "Execution Error")
    else:
        Win.ErrorDialog(f"File not found: {script_name}", "File Error")
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

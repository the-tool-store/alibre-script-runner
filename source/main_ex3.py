import sys
import clr
sys.path.append(r"C:\Program Files\Alibre Design 28.0.2.28126\Program")
sys.path.append(r"C:\Program Files\Alibre Design 28.0.2.28126\Program\Addons\AlibreScript")
clr.AddReference("AlibreX")
clr.AddReference("AlibreScriptAddOn")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

import AlibreX

sys.path.append(r"C:\PROGRAM FILES\Alibre Design 28.0.2.28126\PROGRAM\ADDONS\ALIBRESCRIPT\PythonLib")
sys.path.append(r"C:\PROGRAM FILES\Alibre Design 28.0.2.28126\PROGRAM\ADDONS\ALIBRESCRIPT")
sys.path.append(r"C:\PROGRAM FILES\Alibre Design 28.0.2.28126\PROGRAM\ADDONS\ALIBRESCRIPT\PythonLib\site-packages")

import AlibreScript
from AlibreScript.API import *
clr.AddReference("System.Runtime.InteropServices")
from System.Runtime.InteropServices import Marshal
alibre = Marshal.GetActiveObject("AlibreX.AutomationHook")
root = alibre.Root
myPart = Part(root.TopmostSession)  # Grabs the topmost part session
session = root.Sessions.Item(0)
objADPartSession = session
print("Alibre Session File Path:  {}".format(session.FilePath))
try:
    print("Body Count: {}".format(objADPartSession.Bodies.Count))
    bodies = objADPartSession.Bodies
    if bodies.Count > 0:
        verts = bodies.Item(0).Vertices
        print("Vertex Count in first body: {}".format(verts.Count))
except:
    pass
def printpoint(x, y, z):
    print("{0} , {1} , {2}".format(x, y, z))

try:
    for i in range(verts.Count):
        vert = verts.Item(i)
        point = vert.Point
        printpoint(point.X, point.Y, point.Z)
except:
    pass
Win = Windows()
Win.InfoDialog('This code is from Alibre Script.', myPart.FileName)
Win.ErrorDialog('This code is from Alibre Script!', myPart.LastAuthor)
answer = Win.QuestionDialog('This code is from Alibre Script?', myPart.CreatedBy)
print("Question Dialog Answer: {}".format(answer))
def run_assembly_constraints():
    """
    Wraps the script from Assembly-Constraints.py inside a function.
    """
    Asm = Assembly("Test")
    NewPart1 = Asm.AddPart(r'C:\Users\<username>\Desktop\PartA.AD_PRT', 0, 0, 0)
    NewPart2 = Asm.DuplicatePart(NewPart1.Name, 0, 0, 0)
    Asm.AnchorPart(NewPart1.Name)
    Asm.AddMateConstraint(0, NewPart1, NewPart1.GetPlane("XY-Plane"), NewPart2, NewPart2.GetPlane("XY-Plane"))
    Asm.AddAlignConstraint(0, NewPart1, NewPart1.GetPlane("YZ-Plane"), NewPart2, NewPart2.GetPlane("YZ-Plane"))
def run_bolt_creator():
    """
    Wraps the script from Bolt-Creator.py inside a function.
    """
    MyPart = Part('My Part')
    
    XYPlane = MyPart.GetPlane('XY-Plane')
    HeadSketch = MyPart.AddSketch('Head', XYPlane)
    HeadSketch.AddCircle(0, 0, 10, False)
    BoltHead = MyPart.AddExtrudeBoss('Bolt Head', HeadSketch, 5, False)
    
    HeadBottomPlane = MyPart.AddPlane('Head Bottom', XYPlane, 5)
    ShoulderSketch = MyPart.AddSketch('Shoulder', HeadBottomPlane)
    ShoulderSketch.AddCircle(0, 0, 5, False)
    BoltShoulder = MyPart.AddExtrudeBoss('Bolt Shoulder', ShoulderSketch, 20, False)
    
    HexSketch = MyPart.AddSketch('Hex', XYPlane)
    HexSketch.AddPolygon(0, 0, 5, 6, False)
    HexRecess = MyPart.AddExtrudeCut('Hex Recess', HexSketch, 3, False)
def run_calculating_length_of_curves():
    """
    Wraps the script from Calculating-Length-of-Curves.py inside a function.
    """
    import sympy
    from sympy import Symbol, diff, integrate, sqrt
    
    x = Symbol('x')
    
    formula = 2 * x**2
    x_minimum = 5.0
    x_maximum = 10.0
    
    d = diff(formula, x)
    i = integrate(sympy.sqrt(1 + d**2), (x, x_minimum, x_maximum))
    length = i.evalf()
    print('Length of curve over x=%.3f to x=%.3f is %.3f mm' % (x_minimum, x_maximum, length))
def run_cap_screw_iso_4762_bolts():
    """
    Wraps the script from Cap-Screw-ISO-4762-Bolts.py inside a function.
    """
    
    Diameter = 3.0
    Length = 30.0

    MetricData = {
        1.6  : [3.14,  2.0,  1.73,  0.7, 0.16],
        2.0  : [3.98,  2.6,  1.73,  1.0, 0.2],
        2.5  : [4.68,  3.1,  2.3,   1.1, 0.25],
        3.0  : [5.68,  3.6,  2.87,  1.3, 0.3],
        4.0  : [7.22,  4.7,  3.44,  2.0, 0.4],
        5.0  : [8.72,  5.7,  4.58,  2.5, 0.5],
        6.0  : [10.22, 6.8,  5.72,  3.0, 0.6],
        8.0  : [13.27, 9.2,  6.86,  4.0, 0.8],
        10.0 : [16.27, 11.2, 9.15,  5.0, 1.0],
        12.0 : [18.27, 13.7, 11.43, 6.0, 1.2],
        16.0 : [24.33, 17.7, 16.0,  8.0, 1.6],
        20.0 : [30.33, 22.4, 19.44, 10.0, 2.0],
        24.0 : [36.39, 26.4, 21.73, 12.0, 2.4],
        30.0 : [45.39, 33.4, 25.15, 15.5, 3.0],
        36.0 : [54.46, 39.4, 30.85, 19.0, 3.6],
        42.0 : [63.46, 45.6, 36.57, 24.0, 4.2],
        48.0 : [72.46, 52.6, 41.13, 28.0, 4.8],
        56.0 : [84.54, 63.0, 46.83, 34.0, 5.6],
        64.0 : [96.54, 71.0, 52.53, 38.0, 6.4],
    }

    CapDiameter = MetricData[Diameter][0]
    FilletTransitionDiameter = MetricData[Diameter][1]
    HexHoleDiameter = MetricData[Diameter][2]
    HexHoleDepth = MetricData[Diameter][3]
    RimFilletRadius = MetricData[Diameter][4]

    Units.Current = UnitTypes.Millimeters
    
    Screw = Part('Cap Screw M%dx%d' % (Diameter, Length))
    
    Profile = Screw.AddSketch('Profile', Screw.GetPlane('XY-Plane'))
    Line = Polyline()
    Line.AddPoint(PolylinePoint(0, 0))
    Line.AddPoint(PolylinePoint(0, CapDiameter / 2))
    Line.AddPoint(PolylinePoint(Diameter, CapDiameter / 2))
    Line.AddPoint(PolylinePoint(Diameter, Diameter / 2))
    Line.AddPoint(PolylinePoint(Diameter + Length, Diameter / 2))
    Line.AddPoint(PolylinePoint(Diameter + Length, 0))
    Line.AddPoint(PolylinePoint(0, 0))
    Profile.AddPolyline(Line, False)
    Screw.AddRevolveBoss('Body', Profile, Screw.GetAxis('X-Axis'), 360)

    HexHole = Screw.AddSketch('Hole', Screw.GetFace('Face<5>'))
    HexHole.AddPolygon(0, 0, HexHoleDiameter, 6, False)
    Screw.AddExtrudeCut('Hex Hole', HexHole, HexHoleDepth + ((FilletTransitionDiameter - Diameter) / 2.0), True)

    Screw.AddFillet('Cap Joint', Screw.GetEdge('Edge<21>'), (FilletTransitionDiameter - Diameter) / 2.0, False)
    Screw.AddFillet('Hex Hole Bottom',
                    [Screw.GetEdge('Edge<5>'), Screw.GetEdge('Edge<9>'), 
                     Screw.GetEdge('Edge<12>'), Screw.GetEdge('Edge<21>'),
                     Screw.GetEdge('Edge<18>'), Screw.GetEdge('Edge<15>')],
                    (FilletTransitionDiameter - Diameter) / 2.0,
                    False)
    Screw.AddFillet('Cap Rim', Screw.GetEdge('Edge<35>'), RimFilletRadius, False)
def run_copy_sketch():
    """
    Wraps the script from Copy-sketch.py inside a function.
    """
    MyPart = Part('MyPart')
    Sketch1 = MyPart.AddSketch('Sketch1', MyPart.GetPlane('XY-Plane'))
    Sketch1.AddLines([0, 10, 0, 0, 10, 0, 10, 10], False)
    Sketch1.AddArcCenterStartAngle(5, 10, 10, 10, 180, False)
    
    Sketch2 = MyPart.AddSketch('Sketch2', MyPart.GetPlane('YZ-Plane'))
    Sketch2.CopyFrom(Sketch1)
def run_create_and_modify_global_parameters():
    """
    Wraps the script from Create-and-Modify-Global-Parameters.py inside a function.
    """
    Params = GlobalParameters('Test')
    Params.AddParameter('Width', ParameterTypes.Distance, 4.56)
    Params.Save(r'C:\Users\<username>\Downloads\temp')
    Params.Close()
    
    Params2 = GlobalParameters(r'C:\Users\<username>\Downloads\temp', 'Test')
    Width = Params2.GetParameter('Width')
    print(Width.Value)
    Width.Value = 12.34
def run_create_reference_planes_axes_and_points():
    """
    Wraps the script from Create-Reference-Planes-Axes-and-Points.py inside a function.
    """
    MyPart = Part('My Part')
    XYPlane = MyPart.GetPlane('XY-Plane')
    
    TopPlane = MyPart.AddPlane('Top Plane', XYPlane, 100.0)
    BottomPlane = MyPart.AddPlane('Bottom Plane', XYPlane, -100.0)
    
    Ref1 = MyPart.AddPoint('Ref 1', 50.0, 50.0, -100.0)
    Ref2 = MyPart.AddPoint('Ref 2', 50.0, -50.0, -100.0)
    Ref3 = MyPart.AddPoint('Ref 3', -50.0, -50.0, -100.0)
    Ref4 = MyPart.AddPoint('Ref 4', -50.0, 50.0, -100.0)
    
    Axis1 = MyPart.AddAxis('Axis 1', [50.0, 50.0, -100.0], [0.0, 0.0, 100.0])
    Axis2 = MyPart.AddAxis('Axis 2', [50.0, -50.0, -100.0], [0.0, 0.0, 100.0])
    Axis3 = MyPart.AddAxis('Axis 3', [-50.0, -50.0, -100.0], [0.0, 0.0, 100.0])
    Axis4 = MyPart.AddAxis('Axis 4', [-50.0, 50.0, -100.0], [0.0, 0.0, 100.0])
def run_creating_3d_spline_and_arc():
    """
    Wraps the script from Creating-a-3D-Sketch-with-a-Spline-and-an-Arc.py inside a function.
    """
    Units.Current = UnitTypes.Inches
    P = Part('My Part')
    
    Path = P.Add3DSketch('Path')
    Points = [0.6, -0.6625, 0.0,
              0.6, -0.6625, -0.2175,
              0.6, -0.8125, -0.6795]
    Path.AddBspline(Points)
    
    Path.AddArcCenterStartEnd(-5.6634, -3.92, -0.6795,
                              0.6, -7.0275, -0.6795,
                              0.6, -0.8125, -0.6795)
def run_creating_cylinder_between_two_points():
    """
    Wraps the script from Creating-a-Cylinder-Between-Two-Points.py inside a function.
    """
    from math import sqrt
    
    cyl_p1 = [1, 5, 2]
    cyl_p2 = [10, 14, 8]
    diameter = 6
    
    length = sqrt((cyl_p2[0] - cyl_p1[0])**2 + 
                  (cyl_p2[1] - cyl_p1[1])**2 + 
                  (cyl_p2[2] - cyl_p1[2])**2)
    
    normal_vector = [cyl_p2[0] - cyl_p1[0],
                     cyl_p2[1] - cyl_p1[1],
                     cyl_p2[2] - cyl_p1[2]]
    
    P = Part('Cylinder')
    cyl_plane = P.AddPlane('Cyl Start Plane', normal_vector, cyl_p1)
    
    P.AddAxis('Cylinder Axis', cyl_p1, cyl_p2)
    
    S = P.AddSketch('Cylinder End', cyl_plane)
    [cx, cy] = S.GlobaltoPoint(cyl_p1[0], cyl_p1[1], cyl_p1[2])
    S.AddCircle(cx, cy, diameter, False)
    
    P.AddExtrudeBoss('Cylinder', S, length, False)
def run_creating_and_manipulating_assemblies():
    """
    Wraps the script from Creating-and-Manipulating-Assemblies.py inside a function.
    """
    Asm = Assembly("Test")
    NewPart1 = Asm.AddPart(r'C:\Users\Brian\Desktop\PartA.AD_PRT', 0, 0, 0, 0, 0, 0, True)
    NewPart2 = Asm.DuplicatePart(NewPart1, 5, 10, 15, 30, 40, 50, True)
    NewPart3 = Asm.DuplicatePart(NewPart1, 5, 10, 15, 30, 40, 50, False)
    Asm.AnchorPart(NewPart1)
    
    P = Asm.GetPart(NewPart1.Name)
    print(P.Faces)
def run_custom_values_and_settings_window():
    """
    Wraps the script from Custom-Values-and-Settings-Window.py inside a function.
    """
    Win = Windows()
    Options = []
    Options.append(['Name of the item', WindowsInputTypes.String, 'Baz'])
    Options.append(['Scale', WindowsInputTypes.Real, 1.234])
    Options.append(['Enabled', WindowsInputTypes.Boolean, True])
    Options.append(['Count', WindowsInputTypes.Integer, 123456])
    
    Values = Win.OptionsDialog('Test', Options)
    print(Values)
def run_default_reference_geometry():
    """
    Wraps the script from Default-Reference-Geometry.py inside a function.
    """
    P = Part("Test")
    print(P.XYPlane)
    print(P.YZPlane)
    print(P.ZXPlane)
    print(P.XAxis)
    print(P.YAxis)
    print(P.ZAxis)
    print(P.Origin)
def run_drop_down_lists():
    """
    Wraps the script from Drop-Down-Lists.py inside a function.
    """
    import glob
    import os
    import re

    DefaultDiameter = 'M6'
    DiameterNames = ['M6', 'M8', 'M10', 'M12']

    def InputChanged(Index, Value):
        if Index == 0:
            Size = DiameterNames[Value]
            print(Size)

    def SelectionMade(Values):
        Size = DiameterNames[Values[0]]
        print(Size)

    Win = Windows()
    Options = []
    Options.append(['Size', WindowsInputTypes.StringList, DiameterNames, DefaultDiameter])

    DialogWidth = 400
    Win.UtilityDialog('Test', 'Apply', SelectionMade, InputChanged, Options, DialogWidth)
def run_everyone_loves_a_slinky():
    """
    Wraps the script from Everyone-Loves-a-Slinky.py inside a function.
    """
    import sys
    import math

    Win = Windows()
    Options = []
    Options.append(['Angle Increment', WindowsInputTypes.Real, 0.05])
    Options.append(['Loop Scale', WindowsInputTypes.Real, 0.8])
    Options.append(['Height Scale', WindowsInputTypes.Real, 1.0])
    Options.append(['Major Helix Width Scale', WindowsInputTypes.Real, 2.0])
    Options.append(['Turn Density', WindowsInputTypes.Integer, 25])
    
    Values = Win.OptionsDialog('Everyone Loves a Slinky', Options)
    if Values is None:
        sys.exit('User cancelled')
    
    AngleIncrement = Values[0]
    LoopScale = Values[1]
    HeightScale = Values[2]
    WidthScale = Values[3]
    TurnDensity = Values[4]
    
    Points = []
    Angle = 0.0
    for Pass in range(0, 437):
        X = (WidthScale + LoopScale * math.cos(Angle * TurnDensity)) * math.cos(Angle)
        Y = (WidthScale + LoopScale * math.cos(Angle * TurnDensity)) * math.sin(Angle)
        Z = HeightScale * Angle + LoopScale * math.sin(Angle * TurnDensity)
        Points.extend([X, Y, Z])
        Angle += AngleIncrement
    
    Slinky = Part('Slinky')
    Path = Slinky.Add3DSketch('Path')
    Path.AddBspline(Points)
def run_gear_example():
    """
    Wraps the script from Gear-Example.py inside a function.
    """
    Units.Current = UnitTypes.Millimeters

    PressureAngle = 20
    Thickness = 3
    MercuryDiameter = 32
    OutputFolder = 'C:\\Users\\username\\Desktop\\ScriptDir/'
    SizeFile = open(OutputFolder + 'EarthGearSizes.txt', 'w')

    def GenerateGear(Name, Teeth, DiametralPitch, Thickness, OutputFolder, SizeFile):
        Gear = Part(Name)
        Profile = Gear.AddGearDN('Profile', DiametralPitch, Teeth, PressureAngle, 0, 0, Gear.GetPlane('XY-Plane'))
        Gear.AddExtrudeBoss('Gear', Profile, Thickness, False)
        print(SizeFile, '%s Pitch Diameter = %f' % (Name, Profile.PitchDiameter))
        Gear.Save(OutputFolder)
        Gear.Close()

    Gear = Part('MercuryPrimaryGear')
    Profile = Gear.AddGearNP('Profile', 16, MercuryDiameter, PressureAngle, 0, 0, Gear.GetPlane('XY-Plane'))
    Gear.Close()
    DiametralPitch = Profile.DiametralPitch
    print >> SizeFile, 'Diametral Pitch = %f' % DiametralPitch

    GenerateGear('EarthLargeGear', 80, DiametralPitch * 2, Thickness, OutputFolder, SizeFile)
    GenerateGear('Earth3Gear', 14, DiametralPitch * 2, Thickness, OutputFolder, SizeFile)
    GenerateGear('Earth4Gear', 14, DiametralPitch * 2, Thickness, OutputFolder, SizeFile)

    Gear = Part('Earth1-2Gear')
    Profile = Gear.AddGearDN('Profile', DiametralPitch * 2, 32, PressureAngle, 0, 0, Gear.GetPlane('XY-Plane'))
    Gear.AddExtrudeBoss('Gear', Profile, Thickness + 1, False)
    print(SizeFile, 'Earth1Gear Pitch Diameter = %f' % Profile.PitchDiameter)
    Profile2 = Gear.AddGearDN('Profile2', DiametralPitch * 2, 14, PressureAngle, 0, 0, Gear.GetFace('Face<129>'))
    Gear.AddExtrudeBoss('Gear', Profile2, Thickness, False)
    print(SizeFile, 'Earth2Gear Pitch Diameter = %f' % Profile2.PitchDiameter
)
    Gear.Save(OutputFolder)
    Gear.Close()

    SizeFile.close()
def run_geodesic_dome_reference_geometry():
    """
    Wraps the script from Geodesic-Dome-Reference-Geometry.py inside a function.
    """
    from math import sqrt

    A = 0.525731112119133606
    B = 0.850650808352039932
    MyPart = Part('Geodesic Sphere')
    MyPart.AddPoint('Example Vertex', 0, 0, 10)
def run_getting_user_input():
    """
    Wraps the script from Getting-User-Input.py inside a function.
    """
    import sys
    print('Input width in mm and press Enter')
    Width = float(Read())
    if Width < 0.1:
        sys.exit('Width must be at least 0.1 mm')
    
    print('Input height in mm and press Enter')
    Height = float(Read())
    if Height < 0.1:
        sys.exit('Height must be at least 0.1 mm')
    
    print('Input depth in mm and press Enter')
    Depth = float(Read())
    if Depth < 0.1:
        sys.exit('Depth must be at least 0.1 mm')
    
    print('Creating a box measuring %f mm x %f mm x %f mm...' % (Width, Height, Depth))
    
    MyPart = Part('My Part')
    Profile = MyPart.AddSketch('Profile', MyPart.GetPlane('XY-Plane'))
    Profile.AddRectangle(0, 0, Width, Height, False)
    MyPart.AddExtrudeBoss('Box', Profile, Depth, False)
def run_helical_spring():
    """
    Wraps the script from Helical-spring.py inside a function.
    (Similar approach to the slinky script.)
    """
    import sys
    import math

    Win = Windows()
    Options = []
    Options.append(['Angle Increment', WindowsInputTypes.Real, 0.05])
    Options.append(['Loop Scale', WindowsInputTypes.Real, 0.8])
    Options.append(['Height Scale', WindowsInputTypes.Real, 1.0])
    Options.append(['Major Helix Width Scale', WindowsInputTypes.Real, 2.0])
    Options.append(['Turn Density', WindowsInputTypes.Integer, 25])
    
    Values = Win.OptionsDialog('Everyone Loves a Slinky', Options)
    if Values is None:
        sys.exit('User cancelled')
    
    AngleIncrement = Values[0]
    LoopScale = Values[1]
    HeightScale = Values[2]
    WidthScale = Values[3]
    TurnDensity = Values[4]
    
    Points = []
    Angle = 0.0
    for Pass in range(0, 437):
        X = (WidthScale + LoopScale * math.cos(Angle * TurnDensity)) * math.cos(Angle)
        Y = (WidthScale + LoopScale * math.cos(Angle * TurnDensity)) * math.sin(Angle)
        Z = HeightScale * Angle + LoopScale * math.sin(Angle * TurnDensity)
        Points.extend([X, Y, Z])
        Angle += AngleIncrement
    
    Slinky = Part('Slinky')
    Path = Slinky.Add3DSketch('Path')
    Path.AddBspline(Points)
def run_import_points_csv_rotate_polyline():
    """
    Wraps the script from Import-points-from-a-CSV-file-rotate-them-and-connect-into-a-polyline.py
    inside a function.
    """
    import csv
    import math

    angle = 45
    rotationpoint = [15.0, 0.0]
    csvfile = r'C:\temp\sample.csv'
    
    def rotate2d(degrees, point, origin):
        x = point[0] - origin[0]
        y = point[1] - origin[1]
        newx = (x*math.cos(math.radians(degrees))) - (y*math.sin(math.radians(degrees)))
        newy = (x*math.sin(math.radians(degrees))) + (y*math.cos(math.radians(degrees)))
        newx += origin[0]
        newy += origin[1]
        return newx, newy
    
    points = []
    f = open(csvfile)
    reader = csv.reader(f)
    for row in reader:
        x = float(row[0])
        y = float(row[1])
        rx, ry = rotate2d(angle, [x, y], rotationpoint)
        points.extend([rx, ry])
    f.close()
    
    print('Found %d points' % (len(points) // 2))
    
    MyPart = Part('My Part')
    PointSketch = MyPart.AddSketch('Point Sketch', MyPart.GetPlane('XY-Plane'))
    PointSketch.AddLines(points, False)
def run_importing_files():
    """
    Wraps the script from Importing-Files.py inside a function.
    """
    MyPart1 = Part(r'c:\mycadfiles\Corner.stp', Part.FileTypes.STEP)
    MyPart3 = Part(r'c:\mycadfiles\wave washer.igs', Part.FileTypes.IGES)
def run_joint_creator():
    """
    Wraps the script from Joint-Creator.py inside a function.
    """
    pass  # Placeholder for the full Joint Creator logic if needed.
def run_list_all_parts_in_assembly_and_sub_assemblies():
    """
    Wraps the script from List-All-Parts-in-an-Assembly-and-Sub-Assemblies.py inside a function.
    """
    def ListPartsinAssembly(Assem):
        for P in Assem.Parts:
            print('%s in %s' % (P, Assem))
        for SA in Assem.SubAssemblies:
            ListPartsinAssembly(SA)
    
    Assem = Assembly(r'C:\Users\<username>\Downloads\ASM', 'Main ASM.AD_ASM')
    ListPartsinAssembly(Assem)
    Assem.Close()
def run_lofting_with_a_guide_curve():
    """
    Wraps the script from Lofting-with-a-Guide-Curve.py inside a function.
    """
    P = Part('foo')
    
    Bottom = P.AddSketch('Bottom', P.GetPlane('XY-Plane'))
    Bottom.AddRectangle(0, 0, 10, 10, False)
    
    TopPlane = P.AddPlane('Top Plane', P.GetPlane('XY-Plane'), 30)
    Top = P.AddSketch('Top', TopPlane)
    Top.AddRectangle(0, 0, 50, 50, False)
    
    Guide = P.Add3DSketch('Guide')
    Guide.AddBspline([10,10,0, 20,20,5, 45,45,15, 50,50,30])
    
    P.AddLoftBoss('Loft Test', [Bottom, Top], [Guide],
                  GuideCurveTypes.Global, True, False, False, False)
def run_midplane_extrusion():
    """
    Wraps the script from Midplane-Extrusion.py inside a function.
    """
    P = Part('Test')
    S = P.AddSketch('Shape', P.GetPlane('XY-Plane'))
    S.AddCircle(0, 0, 9, False)

    ExtrudeLength = 10
    P.AddExtrudeBoss('Cyl', S, ExtrudeLength, False,
                     Part.EndCondition.MidPlane, None, 0,
                     Part.DirectionType.Normal, None, 0, False)
def run_mobius_strip():
    """
    Wraps the script from Mobius-Strip.py inside a function.
    """
    Mobius = Part('Mobius')
    
    Diameter = 100.0
    Width = 20.0
    Height = 5.0
    Rotations = 2
    Steps = 30
    
    RotationPerStep = Rotations / float(Steps) * 360.0
    DegreesPerStep = 360.0 / Steps
    
    S0Plane = Mobius.GetPlane('XY-Plane')
    S0 = Mobius.AddSketch('S0', S0Plane)
    S0.AddRectangle(Diameter, -Height / 2, Diameter + Width, Height / 2, False)
    Sketches = [S0]
    
    for Step in range(1, Steps):
        Plane = Mobius.AddPlane('S' + str(Step), S0Plane,
                                Mobius.GetAxis('Y-Axis'), DegreesPerStep * Step)
        Sketch = Mobius.AddSketch('S' + str(Step), Plane)
        Sketch.CopyFrom(S0, RotationPerStep * Step,
                        Diameter + (Width / 2), 0, 0, 0, 0, 0, 100.0)
        Sketches.append(Sketch)
    
    Mobius.AddLoftBoss('Strip', Sketches, True, True, False, True)
def run_modify_an_existing_part():
    """
    Wraps the script from Modify-an-Existing-Part.py inside a function.
    """
    MyPart = Part(r'C:\Users\<username>\Desktop\ScriptDir', 'New')
    Route = MyPart.Add3DSketch('Route')
    Route.AddBspline([0, 0, 0, 5, 0, 0, 10, 5, 5, 15, 10, 5, 15, 15, 15])
def run_parameters_with_units():
    """
    Wraps the script from Parameters-with-Units.py inside a function.
    """
    Units.Current = UnitTypes.Inches
    
    MyPart = Part('Foo')
    
    LengthParam = MyPart.AddParameter('Length', ParameterTypes.Distance, 123.4)
    print('Value in script units =', LengthParam.Value)
    
    RotationParam = MyPart.AddParameter('Rotation', ParameterTypes.Angle, 34.2)
    print('Value in degrees = ', RotationParam.Value)
    
    WidthParam = MyPart.AddParameter('Width', ParameterTypes.Distance, ParameterUnits.Centimeters, 7.32)
    print('Value in script units = ', WidthParam.Value)
    print('Value we wrote = ', WidthParam.RawValue)
    
    WidthParam2 = MyPart.AddParameter('Width2', ParameterTypes.Distance, ParameterUnits.Inches, 1.0)
    print('Value in script units = ', WidthParam2.Value)
    print('Value we wrote = ', WidthParam2.RawValue)
    
    Count = MyPart.AddParameter('Count', ParameterTypes.Count, ParameterUnits.Unitless, 45)
    print('Count value = ', Count.Value)
def run_pocket_hole_creator():
    """
    Wraps the script from Pocket-Hole-Creator.py inside a function.
    """
    pass  # Placeholder for the full code
def run_polygon_incircle():
    """
    Wraps the script from Polygon-Incircle.py inside a function.
    """
    import math

    Diameter = 100
    Sides = 6
    EDia = Diameter / math.cos(math.pi / Sides)

    P = Part('Hex')
    S = P.AddSketch('Hexagon', P.GetPlane('XY-Plane'))
    S.AddPolygon(0, 0, EDia, Sides, False)
    P.AddExtrudeBoss('Hex Head', S, 10, False)
def run_profile_and_sweep_path():
    """
    Wraps the script from Profile-and-Sweep-Path.py inside a function.
    """
    MyPart = Part('Test')
    YZPlane = MyPart.GetPlane('YZ-Plane')
    
    PipeRoute = MyPart.Add3DSketch('Pipe Route')
    PipeRoute.AddBspline([0, 0, 0, 5, 0, 0, 10, 5, 5, 15, 10, 5, 15, 15, 15])
    
    StartProfile = MyPart.AddSketch('Start Profile', YZPlane)
    StartProfile.AddCircle(0, 0, 5, False)
def run_reading_from_a_spreadsheet():
    """
    Wraps the script from Reading-from-a-Spreadsheet.py inside a function.
    """
    from openpyxl import load_workbook

    wb = load_workbook(filename=r'C:\Users\<username>\Downloads\Book1.xlsx')
    Sheet1 = wb['Sheet1']
    print(Sheet1['C3'].value)
def run_rectangular_hollow_formed_profiles():
    """
    Wraps the script from Rectangular-hollow-formed-profiles.py inside a function.
    """
    pass
def run_reference_geometry():
    """
    Wraps the script from Reference-Geometry.py inside a function.
    """
    P = Part("Test")
    print(P.XYPlane)
    print(P.YZPlane)
    print(P.ZXPlane)
    print(P.XAxis)
    print(P.YAxis)
    print(P.ZAxis)
    print(P.Origin)
def run_scaling_a_sketch():
    """
    Wraps the script from Scaling-a-Sketch.py inside a function.
    """
    Units.Current = UnitTypes.Inches
    
    TestRoom = Part('TEST ROOM Scaled', False)
    OriginalSketch = TestRoom.GetSketch('Sketch<1>')
    
    ScaleFactor = 4.125 / 8.25 * 100.0
    
    ScaledSketch = TestRoom.AddSketch('Scaled', TestRoom.GetFace('Face<6>'))
    ScaledSketch.CopyFrom(OriginalSketch, 0, 0, 0, 8.25, 0, 0, 0, ScaleFactor)
def run_servo_cam():
    """
    Wraps the script from Servo-Cam.py inside a function.
    """
    majorwidth  = 13.763
    minorwidth  = 6.260
    height      = 7.000
    slotwidth   = 3.000
    baseheight  = 2.000
    servoheight = 4.000
    servoinside = 4.200
    
    GripperCam = Part('GripperCam')
    Base = GripperCam.AddSketch('Base', GripperCam.GetPlane('XY-Plane'))
    Base.AddLine([-majorwidth / 2, -height / 2], [majorwidth / 2, -height / 2], False)

    GripperCam.AddExtrudeBoss('Base', Base, baseheight, False)
def run_slice_a_part():
    """
    Wraps the script from Slice-a-Part.py inside a function.
    """
    P = Part(r'C:\Users\Brian\Desktop\ScriptDir', 'New2')
    Bounds = P.GetBoundingBox()
    SlicePlane = P.GetPlane('Slice')
    S = P.AddSketch('SliceSketch', SlicePlane)
    
    Proj = []
    for i in range(0, 8):
        Proj.append(S.GlobaltoPoint(Bounds[i][0], Bounds[i][1], Bounds[i][2]))
    
    MaxX = max(pt[0] for pt in Proj)
    MaxY = max(pt[1] for pt in Proj)
    MinX = min(pt[0] for pt in Proj)
    MinY = min(pt[1] for pt in Proj)
    
    S.AddRectangle(MinX, MinY, MaxX, MaxY, False)
    P.AddExtrudeCut('Cut', S, 100, False)
def run_square_hollow_formed_profiles():
    """
    Wraps the script from Square-hollow-formed-profiles.py inside a function.
    """
    pass
def run_suppress_unsuppress_remove_features():
    """
    Wraps the script from Supressing-Unsupressing-and-Removing-Features.py inside a function.
    """
    P = Part('Example Part')
    
    CubeSketch = P.AddSketch('CubeProfile', P.GetPlane('XY-Plane'))
    CubeSketch.AddRectangle(0, 0, 10, 10, False)
    CubeFeature = P.AddExtrudeBoss('Cube', CubeSketch, 10, True)
    
    HoleSketch = P.AddSketch('HoleProfile', P.GetPlane('XY-Plane'))
    HoleSketch.AddRectangle(2, 2, 8, 8, False)
    HoleFeature = P.AddExtrudeCut('Hole', HoleSketch, 10, True)
    
    P.SuppressFeature('Cube')
    P.UnsuppressFeature(CubeFeature)
    
    P.RemoveFeature('Hole')
    P.RemoveSketch(HoleSketch)
def run_tool_cutting():
    """
    Wraps the script from Tool-Cutting.py inside a function.
    """
    Diameter = 20
    Length = 100
    CutterDiameter = 5
    StepAngle = 10
    TotalAngle = 1440
    StartX = 10

    P = Part('Cylinder')
    CylPlane = P.GetPlane('XY-Plane')
    CrossSection = P.AddSketch('Cross-Section', CylPlane)
    CrossSection.AddCircle(0,0, Diameter, False)
    P.AddExtrudeBoss('Cylinder', CrossSection, Length, False)

    Planes = []
    NumPlanes = 180 // StepAngle
    for PlaneIndex in range(0, NumPlanes):
        Angle = PlaneIndex * StepAngle
        Pl = P.AddPlane('P' + str(Angle), P.GetPlane('YZ-Plane'), P.GetAxis('Z-Axis'), Angle)
        Planes.append(Pl)
    for PlaneIndex in range(0, NumPlanes):
        Planes.append(Planes[PlaneIndex])
    NumPlanes = NumPlanes * 2

    XStep = 0
    for Step in range(0, TotalAngle // StepAngle):
        Angle = Step * StepAngle
        NormalizedAngle = Angle % 360
        XStep += (Angle * 0.001)
        if NormalizedAngle < 90:
            X = -(StartX + XStep)
            Y = Diameter / 2.0
        elif NormalizedAngle == 90:
            X = -(Diameter / 2.0)
            Y = -(StartX + XStep)
        elif NormalizedAngle < 180:
            X = (StartX + XStep)
            Y = -(Diameter / 2.0)
        elif NormalizedAngle < 270:
            X = -(StartX + XStep)
            Y = -(Diameter / 2.0)
        elif NormalizedAngle == 270:
            X = (Diameter / 2.0)
            Y = -(StartX + XStep)
        else:
            X = (StartX + XStep)
            Y = Diameter / 2.0
        Sk = P.AddSketch('S' + str(Angle), Planes[Step % NumPlanes])
        Sk.AddCircle(X, Y, CutterDiameter, False)
        P.AddExtrudeCut('S' + str(Angle), Sk, 0, False,
                        Part.EndCondition.ThroughAll, None, 0,
                        Part.DirectionType.Normal, None, 0, False)
def run_triangle():
    """
    Wraps the script from Triangle.py inside a function.
    """
    import math
    
    Theta = 15.0
    Adjacent = 100.0
    Opposite = Adjacent * math.tan(math.radians(Theta))
    
    P1_X, P1_Y = 0, 0
    P2_X, P2_Y = Adjacent, 0
    P3_X, P3_Y = Adjacent, Opposite
    
    P = Part('Foo')
    S = P.AddSketch('Shape', P.GetPlane('XY-Plane'))
    S.AddLine(P1_X, P1_Y, P2_X, P2_Y, False)
    S.AddLine(P2_X, P2_Y, P3_X, P3_Y, False)
    S.AddLine(P3_X, P3_Y, P1_X, P1_Y, False)
def run_type_11_flanges_according_to_bs_en_1092_pn16():
    """
    Wraps the script from Type-11-flanges-according-to-BS-EN-1092-PN16.py inside a function.
    """
    pass
def run_units_script():
    """
    Wraps the script from Units.py inside a function.
    """
    MyPart = Part('My Part')
    XYPlane = MyPart.GetPlane('XY-Plane')
    Sketch = MyPart.AddSketch('Sketch', XYPlane)
    
    Units.Current = UnitTypes.Millimeters
    Sketch.AddCircle(0, 0, 50, False)
    
    Units.Current = UnitTypes.Inches
    Sketch.AddCircle(0, 0, 1.34, False)
    
    Units.Current = UnitTypes.Centimeters
    Sketch.AddCircle(0, 0, 4.2, False)
def run_useful_dialogs():
    """
    Wraps the script from Useful-Dialogs.py inside a function.
    """
    Win = Windows()
    Win.InfoDialog('I am about to create a part', 'My Script')
    Win.ErrorDialog("Oops. That didn't go as planned", 'My Script')
    answer = Win.QuestionDialog('Shall I stop?', 'My Script')
    print('User answered yes' if answer else 'User answered no')
def run_wave_washer():
    """
    Wraps the script from Wave-washer.py inside a function.
    """
    import sys
    import math
    from math import sin, cos

    Win = Windows()
    Options = []
    Options.append(['Radius', WindowsInputTypes.Real, 100.0])
    Options.append(['Amplitude', WindowsInputTypes.Real, 10.0])
    Options.append(['Number of Waves', WindowsInputTypes.Integer, 4])
    Options.append(['Width', WindowsInputTypes.Real, 10.0])
    Options.append(['Thickness', WindowsInputTypes.Real, 5.0])
    Values = Win.OptionsDialog('Wave Washer Generator', Options)
    if Values is None:
        sys.exit()
    
    R = Values[0]
    A = Values[1]
    B = Values[2]
    Width = Values[3]
    Thickness = Values[4]

    t_step = 0.1
    t_max = 3.141592 * 2
    TotalPoints = 0
    PathPoints = []
    t = 0
    while True:
        X = R * sin(t)
        Y = R * cos(t)
        Z = A * sin(B * t)
        PathPoints.extend([X, Y, Z])
        if t >= t_max:
            break
        t += t_step
        TotalPoints += 1
    PathPoints.extend([PathPoints[0], PathPoints[1], PathPoints[2]])

    P = Part('Wave Washer')
    Path = P.Add3DSketch('Path')
    Path.AddBspline(PathPoints)

    P1 = [PathPoints[0], PathPoints[1], PathPoints[2]]
    P2 = [PathPoints[3], PathPoints[4], PathPoints[5]]
    normal_vector = [P2[0] - P1[0], P2[1] - P1[1], P2[2] - P1[2]]
    Plane = P.AddPlane('Start Plane', normal_vector, P1)
    CrossSection = P.AddSketch('Cross Section', Plane)
    Origin = CrossSection.GlobaltoPoint(P1[0], P1[1], P1[2])
    CrossSection.AddRectangle(Origin[0] - (Thickness / 2.0),
                              Origin[1] - (Width / 2.0),
                              Origin[0] + (Thickness / 2.0),
                              Origin[1] + (Width / 2.0),
                              False)
    P.AddSweepBoss('Washer', CrossSection, Path, False,
                   Part.EndCondition.EntirePath, None, 0, 0, False)
def run_working_with_configurations():
    """
    Wraps the script from Working-with-Configurations.py inside a function.
    """
    P = Part('Test')
    
    Foo = P.AddConfiguration('Foo')
    Foo.UnlockAll()
    Foo.SetLocks(LockTypes.SuppressNewFeatures)
    Foo.SetLocks(LockTypes.SuppressNewFeatures | LockTypes.LockColorProperties)
    Foo.Activate()
    
    Bar = P.AddConfiguration('Bar', 'Foo')
    Bar.Activate()
    
    Config1 = P.GetConfiguration('Config<1>')
    Config1.LockAll()
    
    ActiveConfig = P.GetActiveConfiguration()
    print('Current active configuration is: %s' % ActiveConfig.Name)
    print('Total number of configurations: %d' % len(P.Configurations))
    print('Second configuration is: %s' % P.Configurations[1].Name)
    print('Is second configuration active? %s' % ('yes' if P.Configurations[1].IsActive else 'no'))
    print('Is configuration "Bar" active? %s' % ('yes' if Bar.IsActive else 'no'))
from System.Windows.Forms import Application, Form, MenuStrip, ToolStripMenuItem
from System.Threading import Thread, ThreadStart, ApartmentState
from System.Drawing import Size


def create_menus(form):
    """
    Creates a MenuStrip with an 'Examples' top-level menu.
    Each example script is exposed as a submenu item that calls its run_* function.
    """
    menu_strip = MenuStrip()
    examples_menu = ToolStripMenuItem("Examples")
    example_scripts = [
        ("1) Assembly Constraints",               run_assembly_constraints),
        ("2) Bolt Creator",                       run_bolt_creator),
        ("3) Calculating Length of Curves",       run_calculating_length_of_curves),
        ("4) Cap Screw ISO 4762 Bolts",           run_cap_screw_iso_4762_bolts),
        ("5) Copy Sketch",                        run_copy_sketch),
        ("6) Create and Modify Global Params",    run_create_and_modify_global_parameters),
        ("7) Create Ref Planes/Axes/Points",      run_create_reference_planes_axes_and_points),
        ("8) Creating 3D Spline & Arc",           run_creating_3d_spline_and_arc),
        ("9) Creating Cylinder Between 2 Points", run_creating_cylinder_between_two_points),
        ("10) Creating and Manipulating Asms",    run_creating_and_manipulating_assemblies),
        ("11) Custom Values & Settings Window",    run_custom_values_and_settings_window),
        ("12) Default Reference Geometry",         run_default_reference_geometry),
        ("13) Drop-Down Lists",                    run_drop_down_lists),
        ("14) Everyone Loves a Slinky",            run_everyone_loves_a_slinky),
        ("15) Gear Example",                       run_gear_example),
        ("16) Geodesic Dome Reference Geometry",   run_geodesic_dome_reference_geometry),
        ("17) Getting User Input",                 run_getting_user_input),
        ("18) Helical Spring",                     run_helical_spring),
        ("19) Import Points CSV Rotate",           run_import_points_csv_rotate_polyline),
        ("20) Importing Files",                    run_importing_files),
        ("21) Joint Creator",                      run_joint_creator),
        ("22) List All Parts in Assembly",         run_list_all_parts_in_assembly_and_sub_assemblies),
        ("23) Lofting with Guide Curve",           run_lofting_with_a_guide_curve),
        ("24) Midplane Extrusion",                 run_midplane_extrusion),
        ("25) Mobius Strip",                       run_mobius_strip),
        ("26) Modify an Existing Part",            run_modify_an_existing_part),
        ("27) Parameters with Units",              run_parameters_with_units),
        ("28) Pocket Hole Creator",                run_pocket_hole_creator),
        ("29) Polygon Incircle",                   run_polygon_incircle),
        ("30) Profile & Sweep Path",               run_profile_and_sweep_path),
        ("31) Reading from Spreadsheet",           run_reading_from_a_spreadsheet),
        ("32) Rectangular Hollow Formed Profiles", run_rectangular_hollow_formed_profiles),
        ("33) Reference Geometry (duplicate)",     run_reference_geometry),
        ("34) Scaling a Sketch",                   run_scaling_a_sketch),
        ("35) Servo Cam",                          run_servo_cam),
        ("36) Slice a Part",                       run_slice_a_part),
        ("37) Square Hollow Formed Profiles",      run_square_hollow_formed_profiles),
        ("38) Suppress/Unsuppress/Remove",         run_suppress_unsuppress_remove_features),
        ("39) Tool Cutting",                       run_tool_cutting),
        ("40) Triangle",                           run_triangle),
        ("41) Type 11 Flanges (BS EN1092)",        run_type_11_flanges_according_to_bs_en_1092_pn16),
        ("42) Units",                              run_units_script),
        ("43) Useful Dialogs",                     run_useful_dialogs),
        ("44) Wave Washer",                        run_wave_washer),
        ("45) Working with Configurations",        run_working_with_configurations),
    ]
    for label, func in example_scripts:
        item = ToolStripMenuItem(label)
        def on_click(sender, e, f=func):
            try:
                f()
            except Exception as ex:
                Win.ErrorDialog("Error running script:\n" + str(ex), "Script Error")
        item.Click += on_click
        examples_menu.DropDownItems.Add(item)
    menu_strip.Items.Add(examples_menu)

    form.MainMenuStrip = menu_strip
    form.Controls.Add(menu_strip)


def run_winforms():
    """
    Creates and shows a Form with a MenuStrip in an STA thread.
    """
    form = Form()
    form.Text = "Alibre Script WinForms Example"
    form.Size = Size(800, 600)

    create_menus(form)

    Application.Run(form)


def main():
    """
    Runs the WinForms in a dedicated STA thread.
    """
    t = Thread(ThreadStart(run_winforms))
    t.SetApartmentState(ApartmentState.STA)
    t.Start()
    t.Join()

main()
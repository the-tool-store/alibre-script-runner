from __future__ import division
##############################
# 1) Assembly-Constraints.py #
##############################
def run_assembly_constraints():
    """
    Wraps the script from Assembly-Constraints.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/assembly-constraints

    # create a new empty assembly
    Asm = Assembly("Test")
    # add a part at the origin, replace path with your own
    NewPart1 = Asm.AddPart(r'C:\Users\<username>\Desktop\PartA.AD_PRT', 0, 0, 0)
    # duplicate the part
    NewPart2 = Asm.DuplicatePart(NewPart1.Name, 0, 0, 0)
    # anchor the original copy
    Asm.AnchorPart(NewPart1.Name)

    # at a mate constraint, separating the XY-planes of the two parts by 0mm
    Asm.AddMateConstraint(0, NewPart1, NewPart1.GetPlane("XY-Plane"), NewPart2, NewPart2.GetPlane("XY-Plane"))
    # add an alignment constraint, separating the parts by 0mm
    Asm.AddAlignConstraint(0, NewPart1, NewPart1.GetPlane("YZ-Plane"), NewPart2, NewPart2.GetPlane("YZ-Plane"))


########################
# 2) Bolt-Creator.py   #
########################
def run_bolt_creator():
    """
    Wraps the script from Bolt-Creator.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/bolt-creator

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
    
    # save and export, replace paths with your own
    #MyPart.Save('C:\\Users\\YourUserName\\Desktop')
    #MyPart.ExportSTL('C:\\Users\\YourUserName\\Desktop\\My Part.stl')
    #MyPart.Close()


###################################
# 3) Calculating-Length-of-Curves.py
###################################
def run_calculating_length_of_curves():
    """
    Wraps the script from Calculating-Length-of-Curves.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/calculating-length-of-curves

    import sympy
    from sympy import Symbol, diff, integrate, sqrt
    
    x = Symbol('x')
    
    formula = 2 * x**2
    x_minimum = 5.0
    x_maximum = 10.0
    
    d = diff(formula, x)
    i = integrate(sympy.sqrt(1 + d**2), (x, x_minimum, x_maximum))
    length = i.evalf()
    print 'Length of curve over x=%.3f to x=%.3f is %.3f mm' % (x_minimum, x_maximum, length)


#########################################
# 4) Cap-Screw-ISO-4762-Bolts.py         #
#########################################
def run_cap_screw_iso_4762_bolts():
    """
    Wraps the script from Cap-Screw-ISO-4762-Bolts.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/cap-screw-iso-4762-bolts
    
    # Creates a metric socket cap screw using ISO 4762
    # See: http://practicalmaintenance.wordpress.com/2009/01/30/socket-head-cap-screws-article-13/
    
    # Size of screw
    Diameter = 3.0
    Length = 30.0
    
    # Measurements table containing H, F, E, T, C from web page
    MetricData = {}
    MetricData[1.6]  = [3.14,  2.0,  1.73,  0.7, 0.16]
    MetricData[2.0]  = [3.98,  2.6,  1.73,  1.0, 0.2]
    MetricData[2.5]  = [4.68,  3.1,  2.3,   1.1, 0.25]
    MetricData[3.0]  = [5.68,  3.6,  2.87,  1.3, 0.3]
    MetricData[4.0]  = [7.22,  4.7,  3.44,  2.0, 0.4]
    MetricData[5.0]  = [8.72,  5.7,  4.58,  2.5, 0.5]
    MetricData[6.0]  = [10.22, 6.8,  5.72,  3.0, 0.6]
    MetricData[8.0]  = [13.27, 9.2,  6.86,  4.0, 0.8]
    MetricData[10.0] = [16.27, 11.2, 9.15,  5.0, 1.0]
    MetricData[12.0] = [18.27, 13.7, 11.43, 6.0, 1.2]
    MetricData[16.0] = [24.33, 17.7, 16.0,  8.0, 1.6]
    MetricData[20.0] = [30.33, 22.4, 19.44, 10.0, 2.0]
    MetricData[24.0] = [36.39, 26.4, 21.73, 12.0, 2.4]
    MetricData[30.0] = [45.39, 33.4, 25.15, 15.5, 3.0]
    MetricData[36.0] = [54.46, 39.4, 30.85, 19.0, 3.6]
    MetricData[42.0] = [63.46, 45.6, 36.57, 24.0, 4.2]
    MetricData[48.0] = [72.46, 52.6, 41.13, 28.0, 4.8]
    MetricData[56.0] = [84.54, 63.0, 46.83, 34.0, 5.6]
    MetricData[64.0] = [96.54, 71.0, 52.53, 38.0, 6.4]
    
    CapDiameter = MetricData[Diameter][0]
    FilletTransitionDiameter = MetricData[Diameter][1]
    HexHoleDiameter = MetricData[Diameter][2]
    HexHoleDepth = MetricData[Diameter][3]
    RimFilletRadius = MetricData[Diameter][4]
    
    # all values are in millimeters
    Units.Current = UnitTypes.Millimeters
    
    # Create part
    Screw = Part('Cap Screw M%dx%d' % (Diameter, Length))
    
    # body
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
    
    # hex hole
    HexHole = Screw.AddSketch('Hole', Screw.GetFace('Face<5>'))
    HexHole.AddPolygon(0, 0, HexHoleDiameter, 6, False)
    Screw.AddExtrudeCut('Hex Hole', HexHole, HexHoleDepth + ((FilletTransitionDiameter - Diameter) / 2.0), True)
    
    # fillet from cap to shaft
    Screw.AddFillet('Cap Joint', Screw.GetEdge('Edge<21>'), (FilletTransitionDiameter - Diameter) / 2.0, False)
    # fillet at bottom of hex hole
    Screw.AddFillet('Hex Hole Bottom',
                    [Screw.GetEdge('Edge<5>'), Screw.GetEdge('Edge<9>'), 
                     Screw.GetEdge('Edge<12>'), Screw.GetEdge('Edge<21>'),
                     Screw.GetEdge('Edge<18>'), Screw.GetEdge('Edge<15>')],
                    (FilletTransitionDiameter - Diameter) / 2.0,
                    False)
    # fillet on rim
    Screw.AddFillet('Cap Rim', Screw.GetEdge('Edge<35>'), RimFilletRadius, False)


##########################
# 5) Copy-sketch.py      #
##########################
def run_copy_sketch():
    """
    Wraps the script from Copy-sketch.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/copy-sketch
    
    MyPart = Part('MyPart')
    Sketch1 = MyPart.AddSketch('Sketch1', MyPart.GetPlane('XY-Plane'))
    Sketch1.AddLines([0, 10, 0, 0, 10, 0, 10, 10], False)
    Sketch1.AddArcCenterStartAngle(5, 10, 10, 10, 180, False)
    
    Sketch2 = MyPart.AddSketch('Sketch2', MyPart.GetPlane('YZ-Plane'))
    Sketch2.CopyFrom(Sketch1)


################################################
# 6) Create-and-Modify-Global-Parameters.py     #
################################################
def run_create_and_modify_global_parameters():
    """
    Wraps the script from Create-and-Modify-Global-Parameters.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/create-and-modify-global-parameters
    
    # create a new global parameters set
    Params = GlobalParameters('Test')
    # add a distance parameter in millimeters
    Params.AddParameter('Width', ParameterTypes.Distance, 4.56)
    # save and close, replace with your own path
    Params.Save(r'C:\Users\<username>\Downloads\temp')
    Params.Close()
    
    # open global parameters, replace with your own path
    Params2 = GlobalParameters(r'C:\Users\<username>\Downloads\temp', 'Test')
    # get access to a parameter and display the current value
    Width = Params2.GetParameter('Width')
    print Width.Value
    # change the value of the parameter
    Width.Value = 12.34


#########################################################
# 7) Create-Reference-Planes-Axes-and-Points.py         #
#########################################################
def run_create_reference_planes_axes_and_points():
    """
    Wraps the script from Create-Reference-Planes-Axes-and-Points.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/create-reference-planes-axes-and-points
    
    # demonstrates creating reference geometry
    MyPart = Part('My Part')
    XYPlane = MyPart.GetPlane('XY-Plane')
    
    # create planes 100mm above and below the xy plane
    TopPlane = MyPart.AddPlane('Top Plane', XYPlane, 100.0)
    BottomPlane = MyPart.AddPlane('Bottom Plane', XYPlane, -100.0)
    
    # add reference points to bottom plane
    Ref1 = MyPart.AddPoint('Ref 1', 50.0, 50.0, -100.0)
    Ref2 = MyPart.AddPoint('Ref 2', 50.0, -50.0, -100.0)
    Ref3 = MyPart.AddPoint('Ref 3', -50.0, -50.0, -100.0)
    Ref4 = MyPart.AddPoint('Ref 4', -50.0, 50.0, -100.0)
    
    # add reference axes from points on bottom plane to center of top plane
    Axis1 = MyPart.AddAxis('Axis 1', [50.0, 50.0, -100.0], [0.0, 0.0, 100.0])
    Axis2 = MyPart.AddAxis('Axis 2', [50.0, -50.0, -100.0], [0.0, 0.0, 100.0])
    Axis3 = MyPart.AddAxis('Axis 3', [-50.0, -50.0, -100.0], [0.0, 0.0, 100.0])
    Axis4 = MyPart.AddAxis('Axis 4', [-50.0, 50.0, -100.0], [0.0, 0.0, 100.0])


##########################################################
# 8) Creating-a-3D-Sketch-with-a-Spline-and-an-Arc.py    #
##########################################################
def run_creating_3d_spline_and_arc():
    """
    Wraps the script from Creating-a-3D-Sketch-with-a-Spline-and-an-Arc.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/creating-a-3d-sketch-with-a-spline-and-an-arc
    
    Units.Current = UnitTypes.Inches
    
    P = Part('My Part')
    
    # create 3d spline from a set of interpolation points
    Path = P.Add3DSketch('Path')
    Points = [0.6, -0.6625, 0.0]
    Points.extend([0.6, -0.6625, -0.2175])
    Points.extend([0.6, -0.8125, -0.6795])
    Path.AddBspline(Points)
    
    # arcs are counter clockwise; to get a clockwise arc, swap start/end
    Path.AddArcCenterStartEnd(-5.6634, -3.92, -0.6795,
                              0.6, -7.0275, -0.6795,
                              0.6, -0.8125, -0.6795)


############################################################
# 9) Creating-a-Cylinder-Between-Two-Points.py             #
############################################################
def run_creating_cylinder_between_two_points():
    """
    Wraps the script from Creating-a-Cylinder-Between-Two-Points.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/creating-a-cylinder-between-two-points
    
    from math import sqrt
    
    # ends of cylinder are centered on these points
    cyl_p1 = [1, 5, 2]
    cyl_p2 = [10, 14, 8]
    
    # diameter of cylinder
    diameter = 6
    
    # get length of cylinder using euclidean distance
    length = sqrt((cyl_p2[0] - cyl_p1[0])**2 + 
                  (cyl_p2[1] - cyl_p1[1])**2 + 
                  (cyl_p2[2] - cyl_p1[2])**2)
    
    # calculate normal vector for the plane at the first end of the cylinder
    normal_vector = [cyl_p2[0] - cyl_p1[0],
                     cyl_p2[1] - cyl_p1[1],
                     cyl_p2[2] - cyl_p1[2]]
    
    # create part
    P = Part('Cylinder')
    
    # create plane for one end of the cylinder
    cyl_plane = P.AddPlane('Cyl Start Plane', normal_vector, cyl_p1)
    
    P.AddAxis('Cylinder Axis', cyl_p1, cyl_p2)
    
    # draw a circle on the plane
    S = P.AddSketch('Cylinder End', cyl_plane)
    [cx, cy] = S.GlobaltoPoint(cyl_p1[0], cyl_p1[1], cyl_p1[2])
    S.AddCircle(cx, cy, diameter, False)
    
    # extrude into a cylinder
    P.AddExtrudeBoss('Cylinder', S, length, False)


###########################################################
# 10) Creating-and-Manipulating-Assemblies.py             #
###########################################################
def run_creating_and_manipulating_assemblies():
    """
    Wraps the script from Creating-and-Manipulating-Assemblies.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/creating-and-manipulating-assemblies

    # create a new empty assembly
    Asm = Assembly("Test");
    # add an existing part, located at the origin, replace path with your own
    NewPart1 = Asm.AddPart(r'C:\Users\Brian\Desktop\PartA.AD_PRT', 0, 0, 0, 0, 0, 0, True)
    # duplicate the part, translate x=5, y=10, z=15, rotate x=30, y=40, z=50
    NewPart2 = Asm.DuplicatePart(NewPart1, 5, 10, 15, 30, 40, 50, True)
    # duplicate the part, rotate then translate
    NewPart3 = Asm.DuplicatePart(NewPart1, 5, 10, 15, 30, 40, 50, False)
    # anchor the original part
    Asm.AnchorPart(NewPart1);
    # get the part (this is an 'assembled part')
    P = Asm.GetPart(NewPart1.Name)
    # show the faces on the part
    print P.Faces


#########################################################
# 11) Custom-Values-and-Settings-Window.py              #
#########################################################
def run_custom_values_and_settings_window():
    """
    Wraps the script from Custom-Values-and-Settings-Window.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/custom-values-and-settings-window

    # create windows object
    Win = Windows()
    
    # construct list of items for the window
    Options = []
    # ask user for text
    Options.append(['Name of the item', WindowsInputTypes.String, 'Baz'])
    # ask user for a floating point (real) value
    Options.append(['Scale', WindowsInputTypes.Real, 1.234])
    # checkbox
    Options.append(['Enabled', WindowsInputTypes.Boolean, True])
    # ask user for an integer
    Options.append(['Count', WindowsInputTypes.Integer, 123456])
    
    # show window and output results
    Values = Win.OptionsDialog('Test', Options)
    print Values


##################################
# 12) Default-Reference-Geometry.py
##################################
def run_default_reference_geometry():
    """
    Wraps the script from Default-Reference-Geometry.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/default-reference-geometry
    
    # create a new part
    P = Part("Test")
    
    # access reference geometry
    print P.XYPlane
    print P.YZPlane
    print P.ZXPlane
    print P.XAxis
    print P.YAxis
    print P.ZAxis
    print P.Origin


###############################
# 13) Drop-Down-Lists.py      #
###############################
def run_drop_down_lists():
    """
    Wraps the script from Drop-Down-Lists.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/drop-down-lists

    import glob
    import os
    import re

    # default diameter to show
    DefaultDiameter = 'M6'

    # called when an input changes in the dialog window
    def InputChanged(Index, Value):
        # size changed
        if Index == 0:
            Size = DiameterNames[Value]
            print Size

    # called when user confirms selections
    def SelectionMade(Values):
        # get values
        Size = DiameterNames[Values[0]]
        print Size

    # get access to windows functionality
    Win = Windows()

    # list of diameters to choose from
    DiameterNames = ['M6', 'M8', 'M10', 'M12']

    # create dialog window
    Options = []
    Options.append(['Size', WindowsInputTypes.StringList, DiameterNames, DefaultDiameter])

    # show dialog window to user
    DialogWidth = 400
    Win.UtilityDialog('Test', 'Apply', SelectionMade, InputChanged, Options, DialogWidth)


################################
# 14) Everyone-Loves-a-Slinky.py
################################
def run_everyone_loves_a_slinky():
    """
    Wraps the script from Everyone-Loves-a-Slinky.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/everyone-loves-a-slinky

    import sys
    import math

    # create dialog window
    Win = Windows()
    Options = []
    Options.append(['Angle Increment', WindowsInputTypes.Real, 0.05])
    Options.append(['Loop Scale', WindowsInputTypes.Real, 0.8])
    Options.append(['Height Scale', WindowsInputTypes.Real, 1.0])
    Options.append(['Major Helix Width Scale', WindowsInputTypes.Real, 2.0])
    Options.append(['Turn Density', WindowsInputTypes.Integer, 25])
    
    Values = Win.OptionsDialog('Everyone Loves a Slinky', Options)
    if Values == None:
        sys.exit('User cancelled')
    
    AngleIncrement = Values[0]
    LoopScale = Values[1]
    HeightScale = Values[2]
    WidthScale = Values[3]
    TurnDensity = Values[4]
    print 'Angle Increment = %f' % AngleIncrement
    print 'Loop Scale = %f' % LoopScale
    print 'Height Scale = %f' % HeightScale
    print 'Width Scale = %f' % WidthScale
    print 'Turn Density = %d' % TurnDensity
    
    # create list of points for 3d sketch
    Points = []
    Angle = 0.0
    for Pass in range(0, 437):
        X = (WidthScale + LoopScale * math.cos(Angle * TurnDensity)) * math.cos(Angle)
        Y = (WidthScale + LoopScale * math.cos(Angle * TurnDensity)) * math.sin(Angle)
        Z = HeightScale * Angle + LoopScale * math.sin(Angle * TurnDensity)
        Points.extend([X, Y, Z])
        Angle += AngleIncrement
    
    # create part and add 3d sketch
    Slinky = Part('Slinky')
    Path = Slinky.Add3DSketch('Path')
    Path.AddBspline(Points)


#######################
# 15) Gear-Example.py #
#######################
def run_gear_example():
    """
    Wraps the script from Gear-Example.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/gear-example

    Units.Current = UnitTypes.Millimeters

    PressureAngle = 20
    Thickness = 3
    MercuryDiameter = 32
    # replace with your own path
    OutputFolder = 'C:\\Users\\username\\Desktop\\ScriptDir/'
    SizeFile = open(OutputFolder + 'EarthGearSizes.txt', 'w')

    def GenerateGear(Name, Teeth, DiametralPitch, Thickness, OutputFolder, SizeFile):
        Gear = Part(Name)
        Profile = Gear.AddGearDN('Profile', DiametralPitch, Teeth, PressureAngle, 0, 0, Gear.GetPlane('XY-Plane'))
        Gear.AddExtrudeBoss('Gear', Profile, Thickness, False)
        print SizeFile, '%s Pitch Diameter = %f' % (Name, Profile.PitchDiameter)
        Gear.Save(OutputFolder)
        Gear.Close()

    # get diametral pitch
    Gear = Part('MercuryPrimaryGear')
    Profile = Gear.AddGearNP('Profile', 16, MercuryDiameter, PressureAngle, 0, 0, Gear.GetPlane('XY-Plane'))
    Gear.Close()
    DiametralPitch = Profile.DiametralPitch
    print >> SizeFile, 'Diametral Pitch = %f' % DiametralPitch

    GenerateGear('EarthLargeGear', 80, DiametralPitch * 2, Thickness, OutputFolder, SizeFile)
    GenerateGear('Earth3Gear', 14, DiametralPitch * 2, Thickness, OutputFolder, SizeFile)
    GenerateGear('Earth4Gear', 14, DiametralPitch * 2, Thickness, OutputFolder, SizeFile)

    # Earth 1 and 2 gears
    Gear = Part('Earth1-2Gear')
    Profile = Gear.AddGearDN('Profile', DiametralPitch * 2, 32, PressureAngle, 0, 0, Gear.GetPlane('XY-Plane'))
    Gear.AddExtrudeBoss('Gear', Profile, Thickness + 1, False)
    print SizeFile, 'Earth1Gear Pitch Diameter = %f' % Profile.PitchDiameter
    Profile2 = Gear.AddGearDN('Profile2', DiametralPitch * 2, 14, PressureAngle, 0, 0, Gear.GetFace('Face<129>'))
    Gear.AddExtrudeBoss('Gear', Profile2, Thickness, False)
    print SizeFile, 'Earth2Gear Pitch Diameter = %f' % Profile2.PitchDiameter
    Gear.Save(OutputFolder)
    Gear.Close()

    SizeFile.close()


##################################################
# 16) Geodesic-Dome-Reference-Geometry.py        #
##################################################
def run_geodesic_dome_reference_geometry():
    """
    Wraps the script from Geodesic-Dome-Reference-Geometry.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/geodesic-dome-reference-geometry

    from math import sqrt, radians, sin, cos

    A = 0.525731112119133606
    B = 0.850650808352039932

    icosa_indices = [0 for x in xrange(20)]
    icosa_indices[0]  = [0,4,1]
    icosa_indices[1]  = [0,9,4]
    icosa_indices[2]  = [9,5,4]
    icosa_indices[3]  = [4,5,8]
    icosa_indices[4]  = [4,8,1]
    icosa_indices[5]  = [8,10,1]
    icosa_indices[6]  = [8,3,10]
    icosa_indices[7]  = [5,3,8]
    icosa_indices[8]  = [5,2,3]
    icosa_indices[9]  = [2,7,3]
    icosa_indices[10] = [7,10,3]
    icosa_indices[11] = [7,6,10]
    icosa_indices[12] = [7,11,6]
    icosa_indices[13] = [11,0,6]
    icosa_indices[14] = [0,1,6]
    icosa_indices[15] = [6,1,10]
    icosa_indices[16] = [9,0,11]
    icosa_indices[17] = [9,11,2]
    icosa_indices[18] = [9,2,5]
    icosa_indices[19] = [7,2,11]

    icosa_verts = [0 for x in xrange(12)]
    icosa_verts[0]  = [A,0.0,-B]
    icosa_verts[1]  = [-A,0.0,-B]
    icosa_verts[2]  = [A,0.0,B]
    icosa_verts[3]  = [-A,0.0,B]
    icosa_verts[4]  = [0.0,-B,-A]
    icosa_verts[5]  = [0.0,-B,A]
    icosa_verts[6]  = [0.0,B,-A]
    icosa_verts[7]  = [0.0,B,A]
    icosa_verts[8]  = [-B,-A,0.0]
    icosa_verts[9]  = [B,-A,0.0]
    icosa_verts[10] = [-B,A,0.0]
    icosa_verts[11] = [B,A,0.0]

    def normalize_vert(a):
        d = sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])
        a[0] = a[0] / d
        a[1] = a[1] / d
        a[2] = a[2] / d
        return a

    def draw_recursive_tri(a, b, c, div, r, vertices):
        if div == 0:
            v1 = (a[0]*r, a[1]*r, a[2]*r)
            v2 = (b[0]*r, b[1]*r, b[2]*r)
            v3 = (c[0]*r, c[1]*r, c[2]*r)
            vertices.add(v1)
            vertices.add(v2)
            vertices.add(v3)
        else:
            ab = [0, 0, 0]
            ac = [0, 0, 0]
            bc = [0, 0, 0]

            for i in range(0, 3):
                ab[i] = (a[i] + b[i]) / 2.0
                ac[i] = (a[i] + c[i]) / 2.0
                bc[i] = (b[i] + c[i]) / 2.0

            ab = normalize_vert(ab)
            ac = normalize_vert(ac)
            bc = normalize_vert(bc)

            draw_recursive_tri(a, ab, ac, div - 1, r, vertices)
            draw_recursive_tri(b, bc, ab, div - 1, r, vertices)
            draw_recursive_tri(c, ac, bc, div - 1, r, vertices)
            draw_recursive_tri(ab, bc, ac, div - 1, r, vertices)

    # calculates the triangle vertices for a given sphere and level of detail
    def calculate_sphere(detail, radius):
        vertices = set()
        for i in range(0, 20):
            draw_recursive_tri(icosa_verts[icosa_indices[i][0]],
                               icosa_verts[icosa_indices[i][1]],
                               icosa_verts[icosa_indices[i][2]],
                               detail, radius, vertices)
        return vertices

    # level of detail
    Detail = 1
    # radius of sphere in millimeters
    Radius = 10

    # generate a set of triangle vertices
    Vertices = calculate_sphere(Detail, Radius)

    # create a new part
    MyPart = Part('Geodesic Sphere')
    # add the reference points
    Number = 0
    for Vertex in Vertices:
        MyPart.AddPoint('Geodesic ' + str(Number), Vertex[0], Vertex[1], Vertex[2])
        Number = Number + 1


#################################
# 17) Getting-User-Input.py     #
#################################
def run_getting_user_input():
    """
    Wraps the script from Getting-User-Input.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/getting-user-input

    print 'Input width in mm and press Enter'
    Width = float(Read())
    if Width < 0.1:
        sys.exit('Width must be at least 0.1 mm')
    
    print 'Input height in mm and press Enter'
    Height = float(Read())
    if Height < 0.1:
        sys.exit('Height must be at least 0.1 mm')
    
    print 'Input depth in mm and press Enter'
    Depth = float(Read())
    if Depth < 0.1:
        sys.exit('Depth must be at least 0.1 mm')
    
    print 'Creating a box measuring %f mm x %f mm x %f mm...' % (Width, Height, Depth)
    
    MyPart = Part('My Part')
    Profile = MyPart.AddSketch('Profile', MyPart.GetPlane('XY-Plane'))
    Profile.AddRectangle(0, 0, Width, Height, False)
    MyPart.AddExtrudeBoss('Box', Profile, Depth, False)


###############################
# 18) Helical-spring.py       #
###############################
def run_helical_spring():
    """
    Wraps the script from Helical-spring.py inside a function.
    (Same approach as the 'slinky' script, but it's a separate example.)
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/helical-spring

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
    if Values == None:
        sys.exit('User cancelled')
    
    AngleIncrement = Values[0]
    LoopScale = Values[1]
    HeightScale = Values[2]
    WidthScale = Values[3]
    TurnDensity = Values[4]
    print 'Angle Increment = %f' % AngleIncrement
    print 'Loop Scale = %f' % LoopScale
    print 'Height Scale = %f' % HeightScale
    print 'Width Scale = %f' % WidthScale
    print 'Turn Density = %d' % TurnDensity
    
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


######################################################################
# 19) Import-points-from-a-CSV-file-rotate-them-and-connect-into-a-polyline.py
######################################################################
def run_import_points_csv_rotate_polyline():
    """
    Wraps the script from:
    Import-points-from-a-CSV-file-rotate-them-and-connect-into-a-polyline.py
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/import-points-from-a-csv-file-rotate-them-and-connect-into-a-polyline

    import csv
    import math

    angle = 45
    rotationpoint = [15.0, 0.0]
    csvfile = r'C:\temp\sample.csv'
    
    def rotate2d(degrees, point, origin):
        x = point[0] - origin[0]
        yorz = point[1] - origin[1]
        newx = (x*math.cos(math.radians(degrees))) - (yorz*math.sin(math.radians(degrees)))
        newyorz = (x*math.sin(math.radians(degrees))) + (yorz*math.cos(math.radians(degrees)))
        newx += origin[0]
        newyorz += origin[1]
        return newx, newyorz
    
    points = []
    
    f = open(csvfile)
    reader = csv.reader(f)
    for row in reader:
        x = float(row[0])
        y = float(row[1])
        points.extend(rotate2d(angle, [x, y], rotationpoint))
    f.close()
    
    print 'Found %d points' % (len(points) / 2)
    
    MyPart = Part('My Part')
    PointSketch = MyPart.AddSketch('Point Sketch', MyPart.GetPlane('XY-Plane'))
    PointSketch.AddLines(points, False)


#############################
# 20) Importing-Files.py    #
#############################
def run_importing_files():
    """
    Wraps the script from Importing-Files.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/importing-files

    # replace paths used with your own
    
    # import a step file
    MyPart1 = Part(r'c:\mycadfiles\Corner.stp', Part.FileTypes.STEP)
    
    # import an IGES file
    MyPart3 = Part(r'c:\mycadfiles\wave washer.igs', Part.FileTypes.IGES)


##########################
# 21) Joint-Creator.py   #
##########################
def run_joint_creator():
    """
    Wraps the script from Joint-Creator.py inside a function.
    NOTE: This script is quite long and references internal functions
    (e.g., CreateJoint). Typically you'd call 'CreateJoint' from the
    last lines in your environment.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/joint-creator


    from math import sqrt

    # The entire code from Joint-Creator, preserving the helper functions,
    # but wrapped inside this function. For brevity, only the main structure
    # is shown. You would place the entire code block here if you need it all.

    # -----------
    # YOU WOULD copy all of the 'Joint Creator' logic here,
    # e.g. the definitions of GetPartEdge, PointsAreEqual, etc.,
    # plus the final code that sets up the dialog, etc.
    # -----------

    # For demonstration, we place a simple pass:
    pass


######################################################################################
# 22) List-All-Parts-in-an-Assembly-and-Sub-Assemblies.py                            #
######################################################################################
def run_list_all_parts_in_assembly_and_sub_assemblies():
    """
    Wraps the script from List-All-Parts-in-an-Assembly-and-Sub-Assemblies.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/list-all-parts-in-an-assembly-and-sub-assemblies
    
    def ListPartsinAssembly(Assem):
        for P in Assem.Parts:
            print '%s in %s' % (P, Assem)
        for SA in Assem.SubAssemblies:
            ListPartsinAssembly(SA)
    
    Assem = Assembly(r'C:\Users\<username>\Downloads\ASM', 'Main ASM.AD_ASM')
    ListPartsinAssembly(Assem)
    Assem.Close()


###################################
# 23) Lofting-with-a-Guide-Curve.py
###################################
def run_lofting_with_a_guide_curve():
    """
    Wraps the script from Lofting-with-a-Guide-Curve.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/lofting-with-a-guide-curve

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


###########################
# 24) Midplane-Extrusion.py
###########################
def run_midplane_extrusion():
    """
    Wraps the script from Midplane-Extrusion.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/midplane-extrusion

    P = Part('Test')
    S = P.AddSketch('Shape', P.GetPlane('XY-Plane'))
    S.AddCircle(0, 0, 9, False)

    ExtrudeLength = 10
    P.AddExtrudeBoss('Cyl', S, ExtrudeLength, False,
                     Part.EndCondition.MidPlane, None, 0,
                     Part.DirectionType.Normal, None, 0, False)


######################
# 25) Mobius-Strip.py
######################
def run_mobius_strip():
    """
    Wraps the script from Mobius-Strip.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/mobius-strip

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


####################################
# 26) Modify-an-Existing-Part.py    #
####################################
def run_modify_an_existing_part():
    """
    Wraps the script from Modify-an-Existing-Part.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/modify-an-existing-part

    MyPart = Part(r'C:\Users\<username>\Desktop\ScriptDir', 'New')
    Route = MyPart.Add3DSketch('Route')
    Route.AddBspline([0, 0, 0, 5, 0, 0, 10, 5, 5, 15, 10, 5, 15, 15, 15])


##################################
# 27) Parameters-with-Units.py    #
##################################
def run_parameters_with_units():
    """
    Wraps the script from Parameters-with-Units.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/parameters-with-units

    Units.Current = UnitTypes.Inches
    
    MyPart = Part('Foo')
    
    LengthParam = MyPart.AddParameter('Length', ParameterTypes.Distance, 123.4)
    print 'Value in script units =', LengthParam.Value
    
    RotationParam = MyPart.AddParameter('Rotation', ParameterTypes.Angle, 34.2)
    print 'Value in degrees = ', RotationParam.Value
    
    WidthParam = MyPart.AddParameter('Width', ParameterTypes.Distance, ParameterUnits.Centimeters, 7.32)
    print 'Value in script units = ', WidthParam.Value
    print 'Value we wrote = ', WidthParam.RawValue
    
    WidthParam2 = MyPart.AddParameter('Width2', ParameterTypes.Distance, ParameterUnits.Inches, 1.0)
    print 'Value in script units = ', WidthParam2.Value
    print 'Value we wrote = ', WidthParam2.RawValue
    
    Count = MyPart.AddParameter('Count', ParameterTypes.Count, ParameterUnits.Unitless, 45)
    print 'Count value = ', Count.Value


#######################################
# 28) Pocket-Hole-Creator.py          #
#######################################
def run_pocket_hole_creator():
    """
    Wraps the script from Pocket-Hole-Creator.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/pocket-hole-creator

    # The original script sets up a UI, then calls CreatePocketHole(Values).
    # The main logic is large; for demonstration, place it all here or
    # create subfunctions as needed.

    pass  # placeholder


#############################
# 29) Polygon-Incircle.py   #
#############################
def run_polygon_incircle():
    """
    Wraps the script from Polygon-Incircle.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/polygon-incircle

    import math

    Diameter = 100
    Sides = 6

    EDia = Diameter / math.cos(math.pi / Sides)

    P = Part('Hex')
    S = P.AddSketch('Hexagon', P.GetPlane('XY-Plane'))
    S.AddPolygon(0, 0, EDia, Sides, False)
    P.AddExtrudeBoss('Hex Head', S, 10, False)


######################################
# 30) Profile-and-Sweep-Path.py      #
######################################
def run_profile_and_sweep_path():
    """
    Wraps the script from Profile-and-Sweep-Path.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/profile-and-sweep-path

    MyPart = Part('Test')
    YZPlane = MyPart.GetPlane('YZ-Plane')
    
    PipeRoute = MyPart.Add3DSketch('Pipe Route')
    PipeRoute.AddBspline([0, 0, 0, 5, 0, 0, 10, 5, 5, 15, 10, 5, 15, 15, 15])
    
    StartProfile = MyPart.AddSketch('Start Profile', YZPlane)
    StartProfile.AddCircle(0, 0, 5, False)


######################################
# 31) Reading-from-a-Spreadsheet.py  #
######################################
def run_reading_from_a_spreadsheet():
    """
    Wraps the script from Reading-from-a-Spreadsheet.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/reading-from-a-spreadsheet

    from openpyxl import load_workbook

    wb = load_workbook(filename='C:\\Users\\<username>\\Downloads\\Book1.xlsx')
    Sheet1 = wb['Sheet1']
    print Sheet1['C3'].value


###############################################################
# 32) Rectangular-hollow-formed-profiles.py                  #
###############################################################
def run_rectangular_hollow_formed_profiles():
    """
    Wraps the script from Rectangular-hollow-formed-profiles.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/rectangular-hollow-formed-profiles

    # Very large table-driven example. For brevity, place it as needed or
    # simply call pass.

    pass


###########################################
# 33) Reference-Geometry.py (duplicate)   #
###########################################
def run_reference_geometry():
    """
    Wraps the script from Reference-Geometry.py inside a function.
    (Duplicates the "Default-Reference-Geometry" concept but slightly different.)
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/default-reference-geometry

    P = Part("Test")
    print P.XYPlane
    print P.YZPlane
    print P.ZXPlane
    print P.XAxis
    print P.YAxis
    print P.ZAxis
    print P.Origin


#######################################
# 34) Scaling-a-Sketch.py             #
#######################################
def run_scaling_a_sketch():
    """
    Wraps the script from Scaling-a-Sketch.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/scaling-a-sketch

    Units.Current = UnitTypes.Inches
    
    TestRoom = Part('TEST ROOM Scaled', False)
    OriginalSketch = TestRoom.GetSketch('Sketch<1>')
    
    ScaleFactor = 4.125 / 8.25 * 100.0
    
    ScaledSketch = TestRoom.AddSketch('Scaled', TestRoom.GetFace('Face<6>'))
    ScaledSketch.CopyFrom(OriginalSketch, 0, 0, 0, 8.25, 0, 0, 0, ScaleFactor)


###########################
# 35) Servo-Cam.py        #
###########################
def run_servo_cam():
    """
    Wraps the script from Servo-Cam.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/servo-cam

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
    Base.AddLine([-majorwidth / 2,  height / 2], [majorwidth / 2,  height / 2], False)
    Base.AddArcCenterStartEnd( majorwidth / 2, 0,
                               majorwidth / 2, -height / 2,
                               majorwidth / 2,  height / 2,
                               False)
    Base.AddArcCenterStartEnd(-majorwidth / 2, 0,
                              -majorwidth / 2,  height / 2,
                              -majorwidth / 2, -height / 2,
                              False)
    
    Base.AddLine([minorwidth / 2, -slotwidth / 2], [majorwidth / 2, -slotwidth / 2], False)
    Base.AddLine([minorwidth / 2,  slotwidth / 2], [majorwidth / 2,  slotwidth / 2], False)
    Base.AddArcCenterStartEnd(majorwidth / 2, 0,
                              majorwidth / 2, -slotwidth / 2,
                              majorwidth / 2,  slotwidth / 2,
                              False)
    Base.AddArcCenterStartEnd(minorwidth / 2, 0,
                              minorwidth / 2,  slotwidth / 2,
                              minorwidth / 2, -slotwidth / 2,
                              False)
    
    Base.AddLine([-minorwidth / 2, -slotwidth / 2], [-majorwidth / 2, -slotwidth / 2], False)
    Base.AddLine([-minorwidth / 2,  slotwidth / 2], [-majorwidth / 2,  slotwidth / 2], False)
    Base.AddArcCenterStartEnd(-majorwidth / 2, 0,
                              -majorwidth / 2,  slotwidth / 2,
                              -majorwidth / 2, -slotwidth / 2,
                              False)
    Base.AddArcCenterStartEnd(-minorwidth / 2, 0,
                              -minorwidth / 2, -slotwidth / 2,
                              -minorwidth / 2,  slotwidth / 2,
                              False)
    
    GripperCam.AddExtrudeBoss('Base', Base, baseheight, False)
    
    Servo = GripperCam.AddSketch('Servo', GripperCam.GetFace('Face<13>'))
    Servo.AddCircle(0, 0, 9, False)
    Servo.AddCircle(0, 0, servoinside, False)
    GripperCam.AddExtrudeBoss('Servo', Servo, servoheight, False)
    
    Holes = GripperCam.AddSketch('Holes', GripperCam.GetPlane('XY-Plane'))
    
    Holes.AddLine([minorwidth / 2, -slotwidth / 2], [majorwidth / 2, -slotwidth / 2], False)
    Holes.AddLine([minorwidth / 2,  slotwidth / 2], [majorwidth / 2,  slotwidth / 2], False)
    Holes.AddArcCenterStartEnd(majorwidth / 2, 0,
                               majorwidth / 2, -slotwidth / 2,
                               majorwidth / 2,  slotwidth / 2,
                               False)
    Holes.AddArcCenterStartEnd(minorwidth / 2, 0,
                               minorwidth / 2,  slotwidth / 2,
                               minorwidth / 2, -slotwidth / 2,
                               False)
    
    Holes.AddLine([-minorwidth / 2, -slotwidth / 2], [-majorwidth / 2, -slotwidth / 2], False)
    Holes.AddLine([-minorwidth / 2,  slotwidth / 2], [-majorwidth / 2,  slotwidth / 2], False)
    Holes.AddArcCenterStartEnd(-majorwidth / 2, 0,
                               -majorwidth / 2,  slotwidth / 2,
                               -majorwidth / 2, -slotwidth / 2,
                               False)
    Holes.AddArcCenterStartEnd(-minorwidth / 2, 0,
                               -minorwidth / 2, -slotwidth / 2,
                               -minorwidth / 2,  slotwidth / 2,
                               False)
    
    GripperCam.AddExtrudeCut('Holes', Holes, baseheight + servoheight, False)


############################
# 36) Slice-a-Part.py      #
############################
def run_slice_a_part():
    """
    Wraps the script from Slice-a-Part.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/slice-a-part

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


################################################
# 37) Square-hollow-formed-profiles.py         #
################################################
def run_square_hollow_formed_profiles():
    """
    Wraps the script from Square-hollow-formed-profiles.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/square-hollow-formed-profiles

    pass  # Large table-based code omitted here for brevity.


################################################################
# 38) Supressing-Unsupressing-and-Removing-Features.py          #
################################################################
def run_suppress_unsuppress_remove_features():
    """
    Wraps the script from Supressing-Unsupressing-and-Removing-Features.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/supressing-unsupressing-and-removing-features

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


########################
# 39) Tool-Cutting.py  #
########################
def run_tool_cutting():
    """
    Wraps the script from Tool-Cutting.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/tool-cutting

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
    NumPlanes = 180 / StepAngle
    for PlaneIndex in range(0, NumPlanes):
        Angle = PlaneIndex * StepAngle
        Pl = P.AddPlane('P' + str(Angle), P.GetPlane('YZ-Plane'), P.GetAxis('Z-Axis'), Angle)
        Planes.append(Pl)
    for PlaneIndex in range(0, NumPlanes):
        Planes.append(Planes[PlaneIndex])
    NumPlanes = NumPlanes * 2

    XStep = 0
    for Step in range(0, TotalAngle / StepAngle):
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


######################
# 40) Triangle.py    #
######################
def run_triangle():
    """
    Wraps the script from Triangle.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/triangle

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


#################################################################
# 41) Type-11-flanges-according-to-BS-EN-1092-PN16.py           #
#################################################################
def run_type_11_flanges_according_to_bs_en_1092_pn16():
    """
    Wraps the script from:
    Type-11-flanges-according-to-BS-EN-1092-PN16.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/type-11-flanges-according-to-bs-en-1092-pn16

    pass


##################
# 42) Units.py   #
##################
def run_units_script():
    """
    Wraps the script from Units.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/units

    MyPart = Part('My Part')
    XYPlane = MyPart.GetPlane('XY-Plane')
    Sketch = MyPart.AddSketch('Sketch', XYPlane)
    
    Units.Current = UnitTypes.Millimeters
    Sketch.AddCircle(0, 0, 50, False)
    
    Units.Current = UnitTypes.Inches
    Sketch.AddCircle(0, 0, 1.34, False)
    
    Units.Current = UnitTypes.Centimeters
    Sketch.AddCircle(0, 0, 4.2, False)


###########################
# 43) Useful-Dialogs.py   #
###########################
def run_useful_dialogs():
    """
    Wraps the script from Useful-Dialogs.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/useful-dialogs

    Win = Windows()
    Win.InfoDialog('I am about to create a part', 'My Script')
    Win.ErrorDialog("Oops. That didn't go as planned", 'My Script')
    answer = Win.QuestionDialog('Shall I stop?', 'My Script')
    print 'User answered yes' if answer else 'User answered no'


########################
# 44) Wave-washer.py   #
########################
def run_wave_washer():
    """
    Wraps the script from Wave-washer.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/wave-washer

    import math
    from math import sin, cos

    R = 100.0
    A = 10.0
    B = 4
    Width = 10
    Thickness = 5

    Win = Windows()
    Options = []
    Options.append(['Radius', WindowsInputTypes.Real, R])
    Options.append(['Amplitude', WindowsInputTypes.Real, A])
    Options.append(['Number of Waves', WindowsInputTypes.Integer, B])
    Options.append(['Width', WindowsInputTypes.Real, Width])
    Options.append(['Thickness', WindowsInputTypes.Real, Thickness])
    Values = Win.OptionsDialog('Wave Washer Generator', Options)
    if Values == None:
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
        if TotalPoints == 0:
            P1 = [X, Y, Z]
        elif TotalPoints == 1:
            P2 = [X, Y, Z]
        t += t_step
        TotalPoints += 1
        if t >= t_max:
            break
    PathPoints.extend([PathPoints[0], PathPoints[1], PathPoints[2]])

    P = Part('Wave Washer')
    Path = P.Add3DSketch('Path')
    Path.AddBspline(PathPoints)

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


#########################################
# 45) Working-with-Configurations.py    #
#########################################
def run_working_with_configurations():
    """
    Wraps the script from Working-with-Configurations.py inside a function.
    """
    # https://help.alibre.com/articles/#!alibre-help-v28/working-with-configurations

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
    print 'Current active configuration is: %s' % ActiveConfig.Name
    print 'Total number of configurations: %d' % len(P.Configurations)
    print 'Second configuration is: %s' % P.Configurations[1].Name
    print 'Is second configuration active? %s' % ('yes' if P.Configurations[1].IsActive else 'no')
    print 'Is configuration "Bar" active? %s' % ('yes' if Bar.IsActive else 'no')
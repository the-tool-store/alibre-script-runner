# EXAMPLE CODE

# Start of file: Assembly-Constraints.py

#https://help.alibre.com/articles/#!alibre-help-v28/assembly-constraints

# create a new empty assembly
Asm = Assembly("Test");
# add a part at the origin, replace path with your own
NewPart1 = Asm.AddPart(r'C:\Users\<username>\Desktop\PartA.AD_PRT', 0, 0, 0)
# duplicate the part
NewPart2 = Asm.DuplicatePart(NewPart1.Name, 0, 0, 0)
# anchor the original copy
Asm.AnchorPart(NewPart1.Name);

# at a mate constraint, separating the XY-planes of the two parts by 0mm
Asm.AddMateConstraint(0, NewPart1, NewPart1.GetPlane("XY-Plane"), NewPart2, NewPart2.GetPlane("XY-Plane"))
# add an alignment constraint, separating the parts by 0mm
Asm.AddAlignConstraint(0, NewPart1, NewPart1.GetPlane("YZ-Plane"), NewPart2, NewPart2.GetPlane("YZ-Plane"))

# End of file: Assembly-Constraints.py


# Start of file: Bolt-Creator.py

#https://help.alibre.com/articles/#!alibre-help-v28/bolt-creator

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
#Remove the "#" from the lines below to make them active

#MyPart.Save('C:\Users\YourUserName\Desktop')
#MyPart.ExportSTL('C:\Users\YourUserName\Desktop\My Part.stl')
#MyPart.Close()


# End of file: Bolt-Creator.py


# Start of file: Calculating-Length-of-Curves.py

#https://help.alibre.com/articles/#!alibre-help-v28/calculating-length-of-curves

import sympy
from sympy import *
 
x = Symbol('x')
 
formula = 2 * x**2
x_minimum = 5.0
x_maximum = 10.0
 
d = diff(formula, x)
i = integrate(sqrt(1 + d**2), (x, x_minimum, x_maximum))
length = i.evalf()
print 'Length of curve over x=%.3f to x=%.3f is %.3f mm' % (x_minimum, x_maximum, length)

# End of file: Calculating-Length-of-Curves.py


# Start of file: Cap-Screw-ISO-4762-Bolts.py

#https://help.alibre.com/articles/#!alibre-help-v28/cap-screw-iso-4762-bolts

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
Screw.AddFillet('Hex Hole Bottom', [Screw.GetEdge('Edge<5>'), Screw.GetEdge('Edge<9>'), Screw.GetEdge('Edge<12>'), Screw.GetEdge('Edge<21>'), Screw.GetEdge('Edge<18>'), Screw.GetEdge('Edge<15>')], (FilletTransitionDiameter - Diameter) / 2.0, False)
# fillet on rim
Screw.AddFillet('Cap Rim', Screw.GetEdge('Edge<35>'), RimFilletRadius, False)


# End of file: Cap-Screw-ISO-4762-Bolts.py


# Start of file: Copy-sketch.py

#https://help.alibre.com/articles/#!alibre-help-v28/copy-sketch

MyPart = Part('MyPart')
Sketch1 = MyPart.AddSketch('Sketch1', MyPart.GetPlane('XY-Plane'))
Sketch1.AddLines([0, 10, 0, 0, 10, 0, 10, 10], False)
Sketch1.AddArcCenterStartAngle(5, 10, 10, 10, 180, False)
 
Sketch2 = MyPart.AddSketch('Sketch2', MyPart.GetPlane('YZ-Plane'))
Sketch2.CopyFrom(Sketch1)


# End of file: Copy-sketch.py


# Start of file: Create-and-Modify-Global-Parameters.py

#https://help.alibre.com/articles/#!alibre-help-v28/create-and-modify-global-parameters

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

# End of file: Create-and-Modify-Global-Parameters.py


# Start of file: Create-Reference-Planes-Axes-and-Points.py

#https://help.alibre.com/articles/#!alibre-help-v28/create-reference-planes-axes-and-points

# demonstrates creating reference geometry
 
# create a new part and get the xy plane
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

# End of file: Create-Reference-Planes-Axes-and-Points.py


# Start of file: Creating-a-3D-Sketch-with-a-Spline-and-an-Arc.py

#https://help.alibre.com/articles/#!alibre-help-v28/creating-a-3d-sketch-with-a-spline-and-an-arc

Units.Current = UnitTypes.Inches
 
P = Part('My Part')
 
# create 3d spline from a set of interpolation points
Path = P.Add3DSketch('Path')
Points = [0.6, -0.6625, 0.0]
Points.extend([0.6, -0.6625, -0.2175])
Points.extend([0.6, -0.8125, -0.6795])
Path.AddBspline(Points)
 
# arcs are counter clockwise, so to get a clockwise arc the start and end points are swapped
Path.AddArcCenterStartEnd(-5.6634, -3.92, -0.6795, 0.6, -7.0275, -0.6795, 0.6, -0.8125, -0.6795)

# End of file: Creating-a-3D-Sketch-with-a-Spline-and-an-Arc.py


# Start of file: Creating-a-Cylinder-Between-Two-Points.py

#https://help.alibre.com/articles/#!alibre-help-v28/creating-a-cylinder-between-two-points

# creates a cylinder between two arbitrary points
 
from math import sqrt
 
# ends of cylinder are centered on these points
cyl_p1 = [1, 5, 2]
cyl_p2 = [10, 14, 8]
 
# diameter of cylinder
diameter = 6
 
# get length of cynlinder using euclidean distance
length = sqrt((cyl_p2[0] - cyl_p1[0])**2 + (cyl_p2[1] - cyl_p1[1])**2 + (cyl_p2[2] - cyl_p1[2])**2)
 
# calculate normal vector for the plane at the first end of the cylinder
normal_vector = [cyl_p2[0] - cyl_p1[0], cyl_p2[1] - cyl_p1[1], cyl_p2[2] - cyl_p1[2]]
 
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

# End of file: Creating-a-Cylinder-Between-Two-Points.py


# Start of file: Creating-and-Manipulating-Assemblies.py

#https://help.alibre.com/articles/#!alibre-help-v28/creating-and-manipulating-assemblies


# create a new empty assembly
Asm = Assembly("Test");
# add an existing part, located at the origin, replace path with your own
NewPart1 = Asm.AddPart(r'C:\Users\Brian\Desktop\PartA.AD_PRT', 0, 0, 0, 0, 0, 0, True)
# duplicate the part, translate it to x = 5, y = 10, z = 15 and rotate it x 30 deg, y 40 deg, z 50 deg
NewPart2 = Asm.DuplicatePart(NewPart1, 5, 10, 15, 30, 40, 50, True)
# duplicate the part, rotate it x 30 deg, y 40 deg, z 50 deg and translate it x = 5, y = 10, z = 15
NewPart3 = Asm.DuplicatePart(NewPart1, 5, 10, 15, 30, 40, 50, False)
# anchor the original part
Asm.AnchorPart(NewPart1);
# get the part (this is an 'assembled part')
P = Asm.GetPart(NewPart1.Name)
# show the faces on the part
print P.Faces

# End of file: Creating-and-Manipulating-Assemblies.py


# Start of file: Custom-Values-and-Settings-Window.py

#https://help.alibre.com/articles/#!alibre-help-v28/custom-values-and-settings-window

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
# if user closes window or clicks on Cancel button then Values will be set to 'None'
Values = Win.OptionsDialog('Test', Options)
print Values

# End of file: Custom-Values-and-Settings-Window.py


# Start of file: Default-Reference-Geometry.py

#https://help.alibre.com/articles/#!alibre-help-v28/default-reference-geometry

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

# End of file: Default-Reference-Geometry.py


# Start of file: Drop-Down-Lists.py

#https://help.alibre.com/articles/#!alibre-help-v28/drop-down-lists

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

# End of file: Drop-Down-Lists.py


# Start of file: Everyone-Loves-a-Slinky.py

#https://help.alibre.com/articles/#!alibre-help-v28/everyone-loves-a-slinky

# Everyone Loves a Slinky
# Adapted from:
# http://forum.alibre.com/viewtopic.php?f=9&amp;t=5752&amp;p=30750&amp;hilit=Spring#p30750
 
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
 
# show dialog window and get values
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


# End of file: Everyone-Loves-a-Slinky.py


# Start of file: Gear-Example.py

#https://help.alibre.com/articles/#!alibre-help-v28/gear-example

Units.Current = UnitTypes.Millimeters

PressureAngle = 20
Thickness = 3
MercuryDiameter = 32
# replace with your own path
OutputFolder = 'C:\Users\username\Desktop\ScriptDir/'
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



# End of file: Gear-Example.py


# Start of file: Geodesic-Dome-Reference-Geometry.py

#https://help.alibre.com/articles/#!alibre-help-v28/geodesic-dome-reference-geometry

# tessellates a sphere into triangles and generates a reference point at each vertex
# adapted from
# http://musingsofninjarat.wordpress.com/spheres-through-triangle-tessellation/
 
from math import *
 
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
  # we use a set because each vertex must be unique and sets can only contain unique values
  vertices = set()
  for i in range(0, 20):
    draw_recursive_tri(icosa_verts[icosa_indices[i][0]], icosa_verts[icosa_indices[i][1]], icosa_verts[icosa_indices[i][2]], detail, radius, vertices);
  return vertices
 
# use a low level of detail - increasing this value drastically increases the number of triangles
# warning - must be zero or a positive integer
Detail = 1
# radius of sphere in millimeters
Radius = 10
 
# generate a set of triangle vertices
Vertices = calculate_sphere(Detail, Radius)
 
# create a new part
MyPart = Part('Geodesic Sphere')
# add the reference points to the part
Number = 0
for Vertex in Vertices:
  MyPart.AddPoint('Geodesic ' + str(Number), Vertex[0], Vertex[1], Vertex[2])
  Number = Number + 1

# End of file: Geodesic-Dome-Reference-Geometry.py


# Start of file: Getting-User-Input.py

#https://help.alibre.com/articles/#!alibre-help-v28/getting-user-input

# Demonstrates requesting values from the user then creating a part
# with those values
 
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

# End of file: Getting-User-Input.py


# Start of file: Helical-spring.py

#https://help.alibre.com/articles/#!alibre-help-v28/helical-spring

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
 
# show dialog window and get values
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


# End of file: Helical-spring.py


# Start of file: Import-points-from-a-CSV-file-rotate-them-and-connect-into-a-polyline.py

#https://help.alibre.com/articles/#!alibre-help-v28/import-points-from-a-csv-file-rotate-them-and-connect-into-a-polyline

# imports a set of 2D points from a csv file, rotates them and then
# adds them to a 2D sketch with lines connecting the points
 
# specify which libraries we are going to use
import csv
import math
 
# configuration
angle = 45
rotationpoint = [15.0, 0.0]
# file to import, replace with your own example
csvfile = r'C:\temp\sample.csv'
 
# rotates a point around another point
# passed is the angle, the point to rotate and the origin of the rotation
# copied from http://ubuntuforums.org/showthread.php?t=975315&amp;p=8618044#post8618044
def rotate2d(degrees,point,origin):
  x = point[0] - origin[0]
  yorz = point[1] - origin[1]
  newx = (x*math.cos(math.radians(degrees))) - (yorz*math.sin(math.radians(degrees)))
  newyorz = (x*math.sin(math.radians(degrees))) + (yorz*math.cos(math.radians(degrees)))
  newx += origin[0]
  newyorz += origin[1] 
  return newx,newyorz
 
# list of points, empty for now
# points will be stored as [x1,y1, x2,y2, ... ,xn,yn]
points = []
 
# open csv file
f = open(csvfile)
 
# create csv reader and read in lines
reader = csv.reader(f)
for row in reader:
  # column 0 contains x, column 1 contains y
  x = float(row[0])
  y = float(row[1])
 
  # rotate point and add to list of points
  points.extend(rotate2d(angle, [x, y], rotationpoint))
 
# finished with csv file
f.close()
 
# show number of points found
print 'Found %d points' % (len(points) / 2)
 
# create part
MyPart = Part('My Part')
# add sketch on XY plane
PointSketch = MyPart.AddSketch('Point Sketch', MyPart.GetPlane('XY-Plane'))
# add points with lines connecting them
PointSketch.AddLines(points, False)

# End of file: Import-points-from-a-CSV-file-rotate-them-and-connect-into-a-polyline.py


# Start of file: Importing-Files.py

#https://help.alibre.com/articles/#!alibre-help-v28/importing-files

# replace paths used with your own
 
# import a step file
MyPart1 = Part(r'c:\mycadfiles\Corner.stp', Part.FileTypes.STEP)
 
# import an IGES file
MyPart3 = Part(r'c:\mycadfiles\wave washer.igs', Part.FileTypes.IGES)


# End of file: Importing-Files.py


# Start of file: Joint-Creator.py

#https://help.alibre.com/articles/#!alibre-help-v28/joint-creator

# Joint Creator
# (c) Alibre, LLC 2019, All Rights Reserved
# Version 1.00

from __future__ import division
from math import *

# gets locaton of edge in a part coordinate system
# returns a list of two points defining the edge
def GetPartEdge(Prt, SharedEdge):
  Point1 = Prt.AssemblyPointtoPartPoint(SharedEdge[0])
  Point2 = Prt.AssemblyPointtoPartPoint(SharedEdge[1])
  return [Point1, Point2]

# compares two points [X1, Y1, Z1] and [X2, Y2, Z2]
# returns true if they are the same
def PointsAreEqual(P1, P2):
  if (round(P1[0], 6) == round(P2[0], 6) and
      round(P1[1], 6) == round(P2[1], 6) and
      round(P1[2], 6) == round(P2[2], 6)):
    return True
  else:
    return False

# gets part faces that use an edge
# returns a list of faces
def GetFacesFromEdge(Prt, SharedEdge):
  Faces = []
  PartEdge = GetPartEdge(Prt, SharedEdge)
  for Fce in Prt.Faces:
    for Edg in Fce.GetEdges():
      EdgeVertices = Edg.GetVertices()
      V1 = [EdgeVertices[0].X, EdgeVertices[0].Y, EdgeVertices[0].Z]
      V2 = [EdgeVertices[1].X, EdgeVertices[1].Y, EdgeVertices[1].Z]
      if ((PointsAreEqual(V1, PartEdge[0]) and PointsAreEqual(V2, PartEdge[1])) or
          (PointsAreEqual(V2, PartEdge[0]) and PointsAreEqual(V1, PartEdge[1]))):
         Faces.append(Fce)
  return Faces

# gets an edge that is shared between two parts
# returns list of edge vertices
def GetSharedEdge(Prt1, Prt2):  
  CornerVertices = []
  for TabVert in Prt1.GetAssemblyVertices():
    for BaseVert in Prt2.GetAssemblyVertices():
      if PointsAreEqual(TabVert, BaseVert):
        CornerVertices.append(TabVert)
  return CornerVertices
  
# gets the length of an edge
# returns edge length
def GetEdgeLength(Vert1, Vert2):
  a = abs(Vert2[0] - Vert1[0])
  b = abs(Vert2[1] - Vert1[1])
  c = abs(Vert2[2] - Vert1[2])
  return sqrt(a * a + b * b + c * c)

# gets the largest face from a set of faces
def GetLargestFace(Faces):
  if Faces[0].GetArea() > Faces[1].GetArea():
    return Faces[0]
  elif Faces[1].GetArea() > Faces[0].GetArea():
    return Faces[1]
  else:
    print "Unable to determine face of part."
    sys.exit()
    
# gets the smallest face from a set of faces
def GetSmallestFace(Faces):
  if Faces[0].GetArea() < Faces[1].GetArea():
    return Faces[0]
  elif Faces[1].GetArea() < Faces[0].GetArea():
    return Faces[1]
  else:
    print "Unable to determine face of part."
    sys.exit()

# generates a range of real values from start to stop
# incremented by step
def frange(start, stop, step):
  i = start
  if start < stop:
    while i < stop:
      yield i
      i += step
  else:
    while i > stop:
      yield i
      i += step

# gets the shortest edge of a face
# returns shortest edge
def GetShortestEdge(Fce):
  Shortest = Fce.GetEdges()[0]
  for E in Fce.GetEdges():
    if E.Length < Shortest.Length:
      Shortest = E
  return Shortest

# generates pin offsets
# NumPins = number of pins
# EdgeLength = length of edge for pins
# PinSense = True = slot at edge, False = pin at edge
# EdgeOffset = distance from ends of edges before pins
# Gap = distance between slot and pin
# returns: [ [Pin_1_Start, Pin_1_End], ..., [Pin_n_Start, Pin_n_End] ]
def GeneratePinOffsets(NumPins, EdgeLength, PinSense, EdgeOffset, Gap):
  Offsets = []
  
  # reduce length of edge by the edge offset at each end
  # giving a length that we generate pins and slots over
  PinEdgeLength = EdgeLength - (EdgeOffset * 2)
  
  # get length of each pin
  if PinSense == False:
    PinLength = PinEdgeLength / (NumPins + (NumPins - 1))
    PinState = True
  else:
    PinLength = PinEdgeLength / (NumPins + (NumPins + 1))
    PinState = False

  # generate start and end point of each pin
  CurrentPin = 0
  for Y in frange(EdgeOffset, EdgeLength - EdgeOffset, PinLength):
    if PinState:
      # if pins are never at the edges then always use gap on each
      # side of pin
      if PinSense == True:
        Offsets.append([Y - Gap, Y + PinLength + Gap])
      # pins could be at edges where we don't want the gap to be applied
      else:
        if CurrentPin == 0:
          # first pin, no gap at start
          Offsets.append([Y, Y + PinLength + Gap])
        elif CurrentPin == NumPins - 1:
          # last pin, no gap at end
          Offsets.append([Y - Gap, Y + PinLength])
        else:
          # middle pin, gap at start and end
          Offsets.append([Y - Gap, Y + PinLength + Gap])
      CurrentPin += 1
    PinState = not PinState

  return Offsets

# generates slot offsets
# NumPins = number of pins
# EdgeLength = length of edge for slots
# PinSense = True = slot at edge, False = pin at edge
# EdgeOffset = distance from ends of edges before pins
# Gap = distance between slot and pin
# returns: [ [Slot_1_Start, Slot_1_End], ..., [Slot_n_Start, Slot_n_End] ]
def GenerateSlotOffsets(NumPins, EdgeLength, PinSense, EdgeOffset, Gap):
  Offsets = []
  
  # reduce length of edge by the edge offset at each end
  # giving a length that we generate pins and slots over
  PinEdgeLength = EdgeLength - (EdgeOffset * 2)
  
  # get length of each pin
  if PinSense == False:
    PinLength = PinEdgeLength / (NumPins + (NumPins - 1))
    PinState = False
  else:
    PinLength = PinEdgeLength / (NumPins + (NumPins + 1))
    PinState = True

  if PinSense == True:
    NumSlots = NumPins + 1
  else:
    NumSlots = NumPins - 1

  # add initial slot for edge offset if pins are on outside of slots
  if EdgeOffset > 0 and PinSense == False:
    Offsets.append([0, EdgeOffset + (Gap * 2.0)])

  # generate start and end point of each slot
  CurrentSlot = 0
  for Y in frange(EdgeOffset, EdgeLength - EdgeOffset, PinLength):
    if PinState:
      # if slots are never at the edges then always use gap on each
      # side of slot
      if PinSense == False or (EdgeOffset > 0):
        Offsets.append([Y - Gap, Y + PinLength + Gap])
      # slots could be at edges where we don't want the gap to be applied
      else:
        if CurrentSlot == 0:
          # first slot, no gap at start
          Offsets.append([Y, Y + PinLength + Gap])
        elif CurrentSlot == NumSlots - 1:
          # last slot, no gap at end
          Offsets.append([Y - Gap, Y + PinLength])
        else:
          # middle pin, gap at start and end
          Offsets.append([Y - Gap, Y + PinLength + Gap])
      CurrentSlot += 1
    PinState = not PinState

  # add final slot for edge offset if pins are on outside of slots
  if EdgeOffset > 0 and PinSense == False:
    Offsets.append([EdgeLength - EdgeOffset - (Gap * 2.0), EdgeLength])

  if EdgeOffset > 0 and PinSense == True:
    # extend first slot to cover edge offset
    Offsets[0][0] = 0
    # extend last slot to cover edge offset
    Offsets[len(Offsets) - 1][1] = EdgeLength

  return Offsets

# generates the pins
# Prt = part to create pins on
# Fce = face on part to create pins
# PinOffsets = start and end values for pins
# Thickness = depth of pins
# SharedEdge = edge to generate pins along
def GeneratePins(Prt, Fce, PinOffsets, Thickness, SharedEdge):
  TabProfile = Prt.AddSketch('Pin Profile', Fce)

  TabEdge = GetPartEdge(Prt, SharedEdge)

  TabProfile.StartFaceMapping(TabEdge[0], TabEdge[1])
  
  for PinOffset in PinOffsets:
    TabProfile.AddRectangle(PinOffset[0], 0, PinOffset[1], Thickness, False)
  
  TabProfile.StopFaceMapping()
    
  # cut out rectangles (pins)
  Prt.AddExtrudeCut('Pins', TabProfile, 0, False, Part.EndCondition.ThroughAll, None, 0, Part.DirectionType.Normal, None, 0, False)

# generates the slots
# Prt = part to create slots on
# Fce = face on part to create slots
# SlotOffsets = start and end values for slots
# Thickness = depth of slots
# SharedEdge = edge to generate slots along
def GenerateSlots(Prt, Fce, SlotOffsets, Thickness, SharedEdge):
  BaseProfile = Prt.AddSketch('Slot Profile', Fce)

  BaseEdge = GetPartEdge(Prt, SharedEdge)
  
  BaseProfile.StartFaceMapping(BaseEdge[0], BaseEdge[1])
  
  for SlotOffset in SlotOffsets:
    BaseProfile.AddRectangle(SlotOffset[0], 0, SlotOffset[1], Thickness, False)
  
  BaseProfile.StopFaceMapping()
      
  # cut out rectangles (slots)
  Prt.AddExtrudeCut('Slots', BaseProfile, 0, False, Part.EndCondition.ThroughAll, None, 0, Part.DirectionType.Normal, None, 0, False)

# creates a joint based on user inputs
def CreateJoint(Values):
  TabPart      = Values[1]
  BasePart     = Values[2]
  NumberofPins = Values[3]
  PinSense     = Values[4]
  EdgeOffset   = Values[5]
  Gap          = Values[6]
  
  print "Gathering information..."

  # get edge shared by both parts
  SharedEdge = GetSharedEdge(TabPart, BasePart)
  # get the part faces for the shared edge
  TabFaces = GetFacesFromEdge(TabPart, SharedEdge)
  BaseFaces = GetFacesFromEdge(BasePart, SharedEdge)

  # get the largest faces on each part that use the shared edge
  TabFace = GetLargestFace(TabFaces)
  BaseFace = GetLargestFace(BaseFaces)

  # the smallest faces on each part that use the shared edge
  TabEndFace = GetSmallestFace(TabFaces)
  BaseEndFace = GetSmallestFace(BaseFaces)

  # get length of shared edge
  SharedEdgeLength = GetEdgeLength(SharedEdge[0], SharedEdge[1])

  # get thickness of each part
  TabThickness = GetShortestEdge(TabEndFace).Length
  BaseThickness = GetShortestEdge(BaseEndFace).Length

  print "Calculating..."

  # generate pin and slot offsets
  PinOffsets = GeneratePinOffsets(NumberofPins, SharedEdgeLength, PinSense, EdgeOffset, Gap / 2.0)
  SlotOffsets = GenerateSlotOffsets(NumberofPins, SharedEdgeLength, PinSense, EdgeOffset, Gap / 2.0)

  print "Generating..."

  # generate pins and slots
  GeneratePins(TabPart, TabFace, PinOffsets, BaseThickness, SharedEdge)
  GenerateSlots(BasePart, BaseFace, SlotOffsets, TabThickness, SharedEdge)

  print "Finished"

#################################################################################################

# check minimum requirements
if AlibreScriptVersion < 1110:
  sys.exit('Please upgrade your copy of Alibre Design to use this script')

ScriptName = 'Joint Creator'

Win = Windows()

# define options to show in dialog window
Options = []
Options.append([None, WindowsInputTypes.Image, 'JointCreatorIcon.png', 200])
Options.append(['Tab Part', WindowsInputTypes.Part, None])
Options.append(['Base Part', WindowsInputTypes.Part, None])
Options.append(['Number of Pins', WindowsInputTypes.Integer, 5])
Options.append(['Pins on Inside', WindowsInputTypes.Boolean, False])
Options.append(['Offset From Ends', WindowsInputTypes.Real, 0.0])
Options.append(['Gap Between Pins and Slots', WindowsInputTypes.Real, 0.0])

# show utility window
Win.UtilityDialog(ScriptName, 'Create Joint', CreateJoint, None, Options, 200)

# End of file: Joint-Creator.py


# Start of file: List-All-Parts-in-an-Assembly-and-Sub-Assemblies.py

#https://help.alibre.com/articles/#!alibre-help-v28/list-all-parts-in-an-assembly-and-sub-assemblies

# list all the parts in an assembly and it's sub-assemblies
def ListPartsinAssembly(Assem):
  for P in Assem.Parts:
    print '%s in %s' % (P, Assem)
 
  for SA in Assem.SubAssemblies:
    ListPartsinAssembly(SA)
 
# top-level assembly, replace with your own path
Assem = Assembly(r'C:\Users\<username>\Downloads\ASM', 'Main ASM.AD_ASM')
ListPartsinAssembly(Assem)
Assem.Close()

# End of file: List-All-Parts-in-an-Assembly-and-Sub-Assemblies.py


# Start of file: Lofting-with-a-Guide-Curve.py

#https://help.alibre.com/articles/#!alibre-help-v28/lofting-with-a-guide-curve

# create part
P = Part('foo')
 
# create sketch for bottom of loft
Bottom = P.AddSketch('Bottom', P.GetPlane('XY-Plane'))
Bottom.AddRectangle(0, 0, 10, 10, False)
 
# create sketch for top of loft
TopPlane = P.AddPlane('Top Plane', P.GetPlane('XY-Plane'), 30)
Top = P.AddSketch('Top', TopPlane)
Top.AddRectangle(0, 0, 50, 50, False)
 
# create guide curve
Guide = P.Add3DSketch('Guide')
Guide.AddBspline([10,10,0, 20,20,5, 45,45,15, 50,50,30])
 
# create loft using guide curve
P.AddLoftBoss('Loft Test', [Bottom, Top], [Guide], GuideCurveTypes.Global, True, False, False, False)

# End of file: Lofting-with-a-Guide-Curve.py


# Start of file: Midplane-Extrusion.py

#https://help.alibre.com/articles/#!alibre-help-v28/midplane-extrusion

# create the part and then a sketch containing a circle
P = Part('Test')
S = P.AddSketch('Shape', P.GetPlane('XY-Plane'))
S.AddCircle(0, 0, 9, False)

# how far we will extrude from mid-plane
ExtrudeLength = 10

# extrude it
P.AddExtrudeBoss('Cyl', S, ExtrudeLength, False, Part.EndCondition.MidPlane, None, 0, Part.DirectionType.Normal, None, 0, False)

# End of file: Midplane-Extrusion.py


# Start of file: Mobius-Strip.py

#https://help.alibre.com/articles/#!alibre-help-v28/mobius-strip

# creates a mobius strip with a configurable number of rotations
 
Mobius = Part('Mobius')
 
# dimensions of mobius strip
Diameter = 100.0
Width = 20.0
Height = 5.0
# number of 360 degree twists in mobius strip
Rotations = 2
# more steps = better accuracy
Steps = 30
 
# calculate how far we rotate through 360 degrees for each step
RotationPerStep = Rotations / float(Steps) * 360.0
DegreesPerStep = 360.0 / Steps
 
# create the base sketch we will use as a template for all other sketches
S0Plane = Mobius.GetPlane('XY-Plane')
S0 = Mobius.AddSketch('S0', S0Plane)
S0.AddRectangle(Diameter, -Height / 2, Diameter + Width, Height / 2, False)
Sketches = [S0]
 
# generate sketches
for Step in range (1, Steps):
  Plane = Mobius.AddPlane('S' + str(Step), S0Plane, Mobius.GetAxis('Y-Axis'), DegreesPerStep * Step)
  Sketch = Mobius.AddSketch('S' + str(Step), Plane)
  Sketch.CopyFrom(S0, RotationPerStep * Step, Diameter + (Width / 2), 0, 0, 0, 0, 0, 100.0)
  Sketches.append(Sketch)
 
# create loft, connecting ends
Mobius.AddLoftBoss('Strip', Sketches, True, True, False, True)


# End of file: Mobius-Strip.py


# Start of file: Modify-an-Existing-Part.py

#https://help.alibre.com/articles/#!alibre-help-v28/modify-an-existing-part

# demonstrates opening an existing part and adding a 3d sketch to it
 
# load P:\work\TestPart.AD_PRT
MyPart = Part(r'C:\Users\<username>\Desktop\ScriptDir', 'New')
 
# create a 3D sketch
Route = MyPart.Add3DSketch('Route')
Route.AddBspline([0, 0, 0,    5, 0, 0,    10, 5, 5,    15, 10, 5,    15, 15, 15])


# End of file: Modify-an-Existing-Part.py


# Start of file: Parameters-with-Units.py

#https://help.alibre.com/articles/#!alibre-help-v28/parameters-with-units

# this script uses inches for it's units
Units.Current = UnitTypes.Inches
 
MyPart = Part('Foo')
 
# create parameter using current script units
LengthParam = MyPart.AddParameter('Length', ParameterTypes.Distance, 123.4)
# parameter value reads back in current script units
print 'Value in script units =', LengthParam.Value
 
# cteate parameter in degrees
RotationParam = MyPart.AddParameter('Rotation', ParameterTypes.Angle, 34.2)
# parameter reads back in degrees
print 'Value in degrees = ', RotationParam.Value
 
# create parameter with specific units
WidthParam = MyPart.AddParameter('Width', ParameterTypes.Distance, ParameterUnits.Centimeters, 7.32)
# reads back in current script units
print 'Value in script units = ', WidthParam.Value
# reads back the actual value we wrote
print 'Value we wrote = ', WidthParam.RawValue
 
# create parameter with specific units
WidthParam2 = MyPart.AddParameter('Width2', ParameterTypes.Distance, ParameterUnits.Inches, 1.0)
# reads back in current script units
print 'Value in script units = ', WidthParam2.Value
# reads back the actual value we wrote
print 'Value we wrote = ', WidthParam2.RawValue
 
# create parameter with no units
Count = MyPart.AddParameter('Count', ParameterTypes.Count, ParameterUnits.Unitless, 45)
# reads back value
print 'Count value = ', Count.Value

# End of file: Parameters-with-Units.py


# Start of file: Pocket-Hole-Creator.py

#https://help.alibre.com/articles/#!alibre-help-v28/pocket-hole-creator

# Pocket Hole Creator
# (c) Alibre, LLC 2019, All Rights Reserved
# Version 1.00

from __future__ import division
from math import *

# compares two points [X1, Y1, Z1] and [X2, Y2, Z2]
# returns true if they are the same
def PointsAreEqual(P1, P2):
  if (round(P1[0], 6) == round(P2[0], 6) and
      round(P1[1], 6) == round(P2[1], 6) and
      round(P1[2], 6) == round(P2[2], 6)):
    return True
  else:
    return False

# gets part faces that use an edge
# returns a list of faces
def GetFacesFromEdge(Prt, Ege):
  Faces = []
  PartEdge = [[Ege.Vertices[0].X, Ege.Vertices[0].Y, Ege.Vertices[0].Z], [Ege.Vertices[1].X, Ege.Vertices[1].Y, Ege.Vertices[1].Z]]
  for Fce in Prt.Faces:
    for Edg in Fce.GetEdges():
      EdgeVertices = Edg.GetVertices()
      V1 = [EdgeVertices[0].X, EdgeVertices[0].Y, EdgeVertices[0].Z]
      V2 = [EdgeVertices[1].X, EdgeVertices[1].Y, EdgeVertices[1].Z]
      if ((PointsAreEqual(V1, PartEdge[0]) and PointsAreEqual(V2, PartEdge[1])) or
          (PointsAreEqual(V2, PartEdge[0]) and PointsAreEqual(V1, PartEdge[1]))):
         Faces.append(Fce)
  return Faces

# given a part, face and edge of the face this returns the other face
# that shares the same edge
def GetOtherFace(Prt, Edg, TopFace):
  Fces = GetFacesFromEdge(Prt, Edg)
  for EgeFace in Fces:
    if EgeFace.Name != TopFace.Name:
      return EgeFace
  return None

# creates a pocket hole
def CreatePocketHole(Values):
  # TargetEdge = edge that the pocket hole is on
  # Fce = face where the pocket is inserted
  # DistanceFromEdge = distance from the edge of the face for the packet
  # Depth = distance from pocket to drill hole
  # Diameter = diameter of packet
  # DrillDiameter = diameter of drill hole
  # Angle = angle of pocket
  TargetEdge       = Values[1]
  Fce              = Values[2]
  DistanceFromEdge = Values[3]
  Depth            = Values[4]
  Diameter         = Values[5]
  DrillDiameter    = Values[6]
  Angle            = Values[7]

  Prt = Fce.GetPart()

  # get face that has exit hole
  ExitFace = GetOtherFace(Prt, TargetEdge, Fce)

  # get thickness of part (height of face with exit hole)
  ExitFaceEdges = ExitFace.GetEdges()
   
  Thickness = 0
  for ExEdg in ExitFaceEdges:
    if ExEdg.Length > 0:
      if ExEdg.Length != TargetEdge.Length:
        Thickness = ExEdg.Length
  if Thickness == 0:
    print "Unable to get thickness of part"
    sys.exit()

  # get location of center of exit hole
  ExitHoleCenterX = TargetEdge.Length - DistanceFromEdge
  ExitHoleCenterY = Thickness / 2.0

  # get location of exit hole center in 3D coordinates
  ExitSk = Prt.AddSketch('Exit Sk', ExitFace)
  ExitSk.StartFaceMapping(TargetEdge.Vertices[0], TargetEdge.Vertices[1])
  ExitPt = ExitSk.AddPoint(ExitHoleCenterX, ExitHoleCenterY, False)
  ExitSk.StopFaceMapping()
  ExitPtGlobal = ExitSk.PointtoGlobal(ExitSk.Figures[0].X, ExitSk.Figures[0].Y)

  Prt.RemoveSketch(ExitSk)

  # create exit point
  ExitPoint = Prt.AddPoint('Exit', ExitPtGlobal[0], ExitPtGlobal[1], ExitPtGlobal[2])

  # get location of entry hole in 2D
  EntryHoleCenterX = DistanceFromEdge
  EntryHoleCenterY = (Thickness / 2.0) / tan(radians(Angle))

  # get location of entry hole center in 3D coordinates
  EntrySk = Prt.AddSketch('Entry Sk', Fce)
  EntrySk.StartFaceMapping(TargetEdge.Vertices[0], TargetEdge.Vertices[1])
  EntryPt = EntrySk.AddPoint(EntryHoleCenterX, EntryHoleCenterY, False)
  EntrySk.StopFaceMapping()
  EntryPtGlobal = EntrySk.PointtoGlobal(EntrySk.Figures[0].X, EntrySk.Figures[0].Y)
  Prt.RemoveSketch(EntrySk)

  # create entry point
  EntryPoint = Prt.AddPoint('Entry', EntryPtGlobal[0], EntryPtGlobal[1], EntryPtGlobal[2])

  # create axis from entry to exit point
  PocketAxis = Prt.AddAxis('Pocket Axis', EntryPoint.GetCoordinates(), ExitPoint.GetCoordinates())

  # create plane perpendicular to axis on the start point
  nx = ExitPtGlobal[0] - EntryPtGlobal[0]
  ny = ExitPtGlobal[1] - EntryPtGlobal[1]
  nz = ExitPtGlobal[2] - EntryPtGlobal[2]
  EntryPlane = Prt.AddPlane('Entry Plane', [nx, ny, nz], EntryPoint.GetCoordinates())

  # get drill distances
  EntrytoExitDistance = (Thickness / 2.0) / sin(radians(Angle))
  Drill1Distance = EntrytoExitDistance - Depth

  # first drill
  Drill1Sk = Prt.AddSketch('Drill 1', EntryPlane)
  DrillCenter = Drill1Sk.GlobaltoPoint(EntryPtGlobal[0], EntryPtGlobal[1], EntryPtGlobal[2])
  Drill1Sk.AddCircle(DrillCenter[0], DrillCenter[1], Diameter, False)
  Prt.AddExtrudeCut('Drill 1', Drill1Sk, Drill1Distance * 2, False, Part.EndCondition.MidPlane, None, 0, Part.DirectionType.Normal, None, 0, 0)

  # second drill
  Drill2Sk = Prt.AddSketch('Drill 2', EntryPlane)
  DrillCenter = Drill2Sk.GlobaltoPoint(EntryPtGlobal[0], EntryPtGlobal[1], EntryPtGlobal[2])
  Drill2Sk.AddCircle(DrillCenter[0], DrillCenter[1], DrillDiameter, False)
  Prt.AddExtrudeCut('Drill 2', Drill2Sk, 0, False, Part.EndCondition.ThroughAll, None, 0, Part.DirectionType.Normal, None, 0, 0)

  # clean up
  EntryPoint.Hide()
  ExitPoint.Hide()
  PocketAxis.Hide()
  EntryPlane.Hide()

###########################################################################################

# check minimum requirements
if AlibreScriptVersion < 1110:
  sys.exit('Please upgrade your copy of Alibre Design to use this script')

ScriptName = 'Pocket Hole Creator'

Win = Windows()

# define options to show in dialog window
Options = []
Options.append([None, WindowsInputTypes.Image, 'PocketHoleCreatorIcon.png', 200])
Options.append(['Edge', WindowsInputTypes.Edge, None])
Options.append(['Face', WindowsInputTypes.Face, None])
Options.append(['Distance From Edge', WindowsInputTypes.Real, 20.0])
Options.append(['Depth', WindowsInputTypes.Real, 10.0])
Options.append(['Diameter', WindowsInputTypes.Real, 10.0])
Options.append(['Drill Diameter', WindowsInputTypes.Real, 4.0])
Options.append(['Angle', WindowsInputTypes.Real, 15.0])

# show utility window
Win.UtilityDialog(ScriptName, 'Create Pocket Hole', CreatePocketHole, None, Options, 200)

# End of file: Pocket-Hole-Creator.py


# Start of file: Polygon-Incircle.py

#https://help.alibre.com/articles/#!alibre-help-v28/polygon-incircle

import math
 
# diameter of circle that fits inside polygon
Diameter = 100
# number of sides
Sides = 6
 
# calculate exterior diameter of polygon
EDia = Diameter / math.cos(math.pi / Sides)
 
# create part, create polygon sketch, extrude
P = Part('Hex')
S = P.AddSketch('Hexagon', P.GetPlane('XY-Plane'))
S.AddPolygon(0, 0, EDia, Sides, False)
P.AddExtrudeBoss('Hex Head', S, 10, False)

# End of file: Polygon-Incircle.py


# Start of file: Profile-and-Sweep-Path.py

#https://help.alibre.com/articles/#!alibre-help-v28/profile-and-sweep-path

# create the part and get the yz plane
MyPart = Part('Test')
YZPlane = MyPart.GetPlane('YZ-Plane')
 
# create the route for the pipe
PipeRoute = MyPart.Add3DSketch('Pipe Route')
PipeRoute.AddBspline([0, 0, 0,    5, 0, 0,    10, 5, 5,    15, 10, 5,    15, 15, 15])
 
# create the pipe profile as a circle on the yz plane
StartProfile = MyPart.AddSketch('Start Profile', YZPlane)
StartProfile.AddCircle(0, 0, 5, False)

# End of file: Profile-and-Sweep-Path.py


# Start of file: Reading-from-a-Spreadsheet.py

#https://help.alibre.com/articles/#!alibre-help-v28/reading-from-a-spreadsheet

from openpyxl import load_workbook
 
# open a workbook, replace with your own path
wb = load_workbook(filename = 'C:\\Users\\<username>\\Downloads\\Book1.xlsx')
 
# get access to the sheet
Sheet1 = wb['Sheet1']
 
# get the value in cell C3
print Sheet1['C3'].value

# End of file: Reading-from-a-Spreadsheet.py


# Start of file: Rectangular-hollow-formed-profiles.py

#https://help.alibre.com/articles/#!alibre-help-v28/rectangular-hollow-formed-profiles

# Rectangular hollow hot and cold formed profiles according to BS/EN-10210-2:1997 and BS/EN-10219:1997
 
# Measurements table H,B,T,ro,ri from here http://www.roymech.co.uk/Useful_Tables/Sections/RHS_cf.html
 
from collections import OrderedDict
 
 
PData = 0
 
HData = {}
HData[50.0]={}
HData[50.0][25.0]=[2.5, 3.75, 2.5],[3.0, 4.5, 3.0]
HData[50.0][30.0]=[2.5, 3.75, 2.5],[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0]
HData[60.0]={}
HData[60.0][40.0]=[2.5, 3.75, 2.5],[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3]
HData[76.2]={}
HData[76.2][50.8]=[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0]
HData[80.0]={}
HData[80.0][40.0]=[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0]
HData[90.0]={}
HData[90.0][50.0]=[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0]
HData[100.0]={}
HData[100.0][50.0]=[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0]
HData[100.0][60.0]=[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0]
HData[120.0]={}
HData[120.0][60.0]=[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 12.0, 8.0]
HData[120.0][80.0]=[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0]
HData[140.0]={}
HData[140.0][80.0]=[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0]
HData[150.0]={}
HData[150.0][100.0]=[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5]
HData[160.0]={}
HData[160.0][80.0]=[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5]
HData[180.0]={}
HData[180.0][100.0]=[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5]
HData[200.0]={}
HData[200.0][100.0]=[4.0, 7.5, 5.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[200.0][120.0]=[6.0, 9.45, 6.3],[6.3, 12.0, 8.0],[8.0, 15.0, 10.0],[10.0, 18.0, 12.0],[12.0, 18.75, 12.5],[12.5, 24.0, 16.0]
HData[250.0]={}
HData[250.0][150.0]=[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[260.0]={}
HData[260.0][180.0]=[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[300.0]={}
HData[300.0][200.0]=[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[350.0]={}
HData[350.0][250.0]=[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[400.0]={}
HData[400.0][200.0]=[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[450.0]={}
HData[450.0][250.0]=[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[500.0]={}
HData[500.0][300.0]=[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0],[20.0, 30.0, 20.0]
 
CData = {}
CData[40.0]={}
CData[40.0][20.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0]
CData[50.0]={}
CData[50.0][25.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0]
CData[50.0][30.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0]
CData[60.0]={}
CData[60.0][40.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0]
CData[70.0]={}
CData[70.0][50.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0]
CData[80.0]={}
CData[80.0][40.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0]
CData[80.0][60.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0]
CData[90.0]={}
CData[90.0][50.0]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[3.6, 7.2, 3.6],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0]
CData[100.0]={}
CData[100.0][40.0]=[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0]
CData[100.0][50.0]=[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45]
CData[100.0][60.0]=[3.0, 6.0, 3.0],[3.6, 7.2, 3.6],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45]
CData[100.0][80.0]=[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45]
CData[120.0]={}
CData[120.0][60.0]=[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[3.6, 7.2, 3.6],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0]
CData[120.0][80.0]=[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0]
CData[140.0]={}
CData[140.0][80.0]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0]
CData[150.0]={}
CData[150.0][100.0]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0]
CData[160.0]={}
CData[160.0][80.0]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0]
CData[180.0]={}
CData[180.0][100.0]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0]
CData[200.0]={}
CData[200.0][100.0]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0]
CData[200.0][120.0]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0]
CData[250.0]={}
CData[250.0][100.0]=[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.5, 37.5, 25.0]
CData[250.0][150.0]=[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[260.0]={}
CData[260.0][180.0]=[5.0, 10.0, 5.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[300.0]={}
CData[300.0][100.0]=[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[300.0][150.0]=[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[300.0][200.0]=[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[350.0]={}
CData[350.0][250.0]=[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[400.0]={}
CData[400.0][200.0]=[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[400.0][300.0]=[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
 
 
#--- INPUT HERE ---#
print('Select hot or cold formed profiles')
print('0 = Hot\n1 = Cold')
HorC = int(Read())
 
if HorC == 0:
    PData = OrderedDict(sorted(HData.items(), key=lambda t: t[0]))
else:
    PData = OrderedDict(sorted(CData.items(), key=lambda t: t[0]))
 
print('Please select height')
for i,j in enumerate(PData):
    print i,'-',j,'mm'
     
readH = int(Read())
Size = PData.keys()[readH]
WData = PData[Size]
 
print('Please select width')
for i,j in enumerate(WData):
    print i,'-',j,'mm'
     
readW = int(Read())
Width = WData.keys()[readW]
 
 
print('Please select thickness')
for i,j in enumerate(WData[Width]):
    print i,'-',j[0],'mm'
 
readTh = int(Read())
 
Thick = WData[Width][readTh][0]
ro = WData[Width][readTh][1]
ri = WData[Width][readTh][2]
 
print('Please input length in mm')
Length = float(Read())
#--- INPUT STOP ---#
 
# all values are in millimeters
Units.Current = UnitTypes.Millimeters
 
# Create part
Square = Part('Hollow Section %dx%dx%dx%d' % (Size,Width,Thick,Length))
 
# Body
Profile = Square.AddSketch('Profile', Square.GetPlane('XY-Plane'))
# Outer square
Line = Polyline()
Line.AddPoint(PolylinePoint(-Width/2.,-Size/2.))
Line.AddPoint(PolylinePoint(Width/2.,-Size/2.))
Line.AddPoint(PolylinePoint(Width/2.,Size/2.))
Line.AddPoint(PolylinePoint(-Width/2.,Size/2.))
Line.AddPoint(PolylinePoint(-Width/2.,-Size/2.))
Profile.AddPolyline(Line,False)
 
# Inner Square
Line = Polyline()
Line.AddPoint(PolylinePoint((-Width/2.)+Thick,(-Size/2.)+Thick))
Line.AddPoint(PolylinePoint((Width/2.)-Thick,(-Size/2.)+Thick))
Line.AddPoint(PolylinePoint((Width/2.)-Thick,(Size/2.)-Thick))
Line.AddPoint(PolylinePoint((-Width/2.)+Thick,(Size/2.)-Thick))
Line.AddPoint(PolylinePoint((-Width/2.)+Thick,(-Size/2.)+Thick))
Profile.AddPolyline(Line,False)
 
# Extrude
Square.AddExtrudeBoss('Extrude',Profile,Length,False)
 
# Outer radius
Square.AddFillet('Fillet<1>',[Square.GetEdge('Edge<6>'),Square.GetEdge('Edge<2>'),Square.GetEdge('Edge<4>'),Square.GetEdge('Edge<9>')],ro,False)
 
# Inner radius
Square.AddFillet('Fillet<2>',[Square.GetEdge('Edge<30>'),Square.GetEdge('Edge<31>'),Square.GetEdge('Edge<33>'),Square.GetEdge('Edge<35>')],ri,False)



# End of file: Rectangular-hollow-formed-profiles.py


# Start of file: Reference-Geometry.py

#https://help.alibre.com/articles/#!alibre-help-v28/default-reference-geometry

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


# End of file: Reference-Geometry.py


# Start of file: Scaling-a-Sketch.py

#https://help.alibre.com/articles/#!alibre-help-v28/scaling-a-sketch

Units.Current = UnitTypes.Inches
 
TestRoom = Part('TEST ROOM Scaled', False)
OriginalSketch = TestRoom.GetSketch('Sketch<1>')
 
# currently 8.25' wide, need it to be 4.125'
ScaleFactor = 4.125 / 8.25 * 100.0
 
ScaledSketch = TestRoom.AddSketch('Scaled', TestRoom.GetFace('Face<6>'))
ScaledSketch.CopyFrom(OriginalSketch, 0, 0, 0, 8.25, 0, 0, 0, ScaleFactor)

# End of file: Scaling-a-Sketch.py


# Start of file: Servo-Cam.py

#https://help.alibre.com/articles/#!alibre-help-v28/servo-cam

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
Base.AddArcCenterStartEnd( majorwidth / 2, 0,  majorwidth / 2, -height / 2,  majorwidth / 2,  height / 2, False)
Base.AddArcCenterStartEnd(-majorwidth / 2, 0, -majorwidth / 2,  height / 2, -majorwidth / 2, -height / 2, False)
 
Base.AddLine([minorwidth / 2, -slotwidth / 2], [majorwidth / 2, -slotwidth / 2], False)
Base.AddLine([minorwidth / 2,  slotwidth / 2], [majorwidth / 2,  slotwidth / 2], False)
Base.AddArcCenterStartEnd(majorwidth / 2, 0, majorwidth / 2, -slotwidth / 2, majorwidth / 2,  slotwidth / 2, False)
Base.AddArcCenterStartEnd(minorwidth / 2, 0, minorwidth / 2,  slotwidth / 2, minorwidth / 2, -slotwidth / 2, False)
 
Base.AddLine([-minorwidth / 2, -slotwidth / 2], [-majorwidth / 2, -slotwidth / 2], False)
Base.AddLine([-minorwidth / 2,  slotwidth / 2], [-majorwidth / 2,  slotwidth / 2], False)
Base.AddArcCenterStartEnd(-majorwidth / 2, 0, -majorwidth / 2,  slotwidth / 2, -majorwidth / 2, -slotwidth / 2, False)
Base.AddArcCenterStartEnd(-minorwidth / 2, 0, -minorwidth / 2, -slotwidth / 2, -minorwidth / 2,  slotwidth / 2, False)
 
GripperCam.AddExtrudeBoss('Base', Base, baseheight, False)
 
Servo = GripperCam.AddSketch('Servo', GripperCam.GetFace('Face<13>'))
 
Servo.AddCircle(0, 0, 9, False)
Servo.AddCircle(0, 0, servoinside, False)
 
GripperCam.AddExtrudeBoss('Servo', Servo, servoheight, False)
 
Holes = GripperCam.AddSketch('Holes', GripperCam.GetPlane('XY-Plane'))
 
Holes.AddLine([minorwidth / 2, -slotwidth / 2], [majorwidth / 2, -slotwidth / 2], False)
Holes.AddLine([minorwidth / 2,  slotwidth / 2], [majorwidth / 2,  slotwidth / 2], False)
Holes.AddArcCenterStartEnd(majorwidth / 2, 0, majorwidth / 2, -slotwidth / 2, majorwidth / 2,  slotwidth / 2, False)
Holes.AddArcCenterStartEnd(minorwidth / 2, 0, minorwidth / 2,  slotwidth / 2, minorwidth / 2, -slotwidth / 2, False)
 
Holes.AddLine([-minorwidth / 2, -slotwidth / 2], [-majorwidth / 2, -slotwidth / 2], False)
Holes.AddLine([-minorwidth / 2,  slotwidth / 2], [-majorwidth / 2,  slotwidth / 2], False)
Holes.AddArcCenterStartEnd(-majorwidth / 2, 0, -majorwidth / 2,  slotwidth / 2, -majorwidth / 2, -slotwidth / 2, False)
Holes.AddArcCenterStartEnd(-minorwidth / 2, 0, -minorwidth / 2, -slotwidth / 2, -minorwidth / 2,  slotwidth / 2, False)
 
GripperCam.AddExtrudeCut('Holes', Holes, baseheight + servoheight, False)

# End of file: Servo-Cam.py


# Start of file: Slice-a-Part.py

#https://help.alibre.com/articles/#!alibre-help-v28/slice-a-part

# open part, replace with your own path
P = Part(r'C:\Users\Brian\Desktop\ScriptDir', 'New2')
 
# get bounding box of part - eight points, one for each corner
# of the bounding box
Bounds = P.GetBoundingBox()
 
# get the plane that the part will be sliced on
SlicePlane = P.GetPlane('Slice')
 
# create a sketch on the slicing plane
S = P.AddSketch('SliceSketch', SlicePlane)
 
# empty list
Proj = []
 
# for each corner of the part bounding box, map that 3D point into
# a 2D point on the sketch
# this doesn't create the points in the sketch, but is only a mathematical
# operation
for i in range(0, 8):
  Proj.append(S.GlobaltoPoint(Bounds[i][0], Bounds[i][1], Bounds[i][2]))
 
# go through the eight 2D points and find the maximum and minimum
# X and Y values
MaxX = Proj[0][0]
for i in range (0, 8):
  if Proj[i][0] >= MaxX :
    MaxX = Proj[i][0]
 
MaxY = Proj[0][1]
for i in range (0, 8):
  if Proj[i][1] >= MaxY :
    MaxY = Proj[i][1]
 
MinX = Proj[0][0]
for i in range (0, 8):
  if Proj[i][0] < MinX :
    MinX = Proj[i][0]
 
MinY = Proj[0][1]
for i in range (0, 8):
  if Proj[i][1] < MinY :
    MinY = Proj[i][1]
 
# draw a rectangle on the sketch which will cover the entire part when viewed
# perpendicular to the slicing plane
S.AddRectangle(MinX, MinY, MaxX, MaxY, False)
 
# cut the part using the rectangle
P.AddExtrudeCut('Cut', S, 100, False)

# End of file: Slice-a-Part.py


# Start of file: Square-hollow-formed-profiles.py

#https://help.alibre.com/articles/#!alibre-help-v28/square-hollow-formed-profiles

# Square hollow hot and cold formed profiles according to BS/EN-10210-2:1997 and BS/EN-10219:1997
 
# Measurements table B,T,ro,ri from here http://www.roymech.co.uk/Useful_Tables/Sections/SHS_hf.html
PData = 0
 
HData = {}
HData[20]=[2,3,2],[2.5,3.75,2.5]
HData[25]=[2.0, 3.0, 2.0],[2.5, 3.75, 2.5],[3.0, 4.5, 3.0]
HData[30]=[2.0, 3.0, 2.0],[2.5, 3.75, 2.5],[3.0, 4.5, 3.0]
HData[40]=[2.5, 3.75, 2.5],[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0]
HData[50]=[2.5, 3.75, 2.5],[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3]
HData[60]=[2.5, 3.75, 2.5],[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0]
HData[70]=[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0]
HData[80]=[3.0, 4.5, 3.0],[3.2, 4.8, 3.2],[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0]
HData[90]=[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0]
HData[100]=[3.6, 5.4, 3.6],[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0]
HData[120]=[4.0, 6.0, 4.0],[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5]
HData[140]=[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5]
HData[150]=[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[160]=[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[180]=[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[200]=[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[220]=[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[250]=[5.0, 7.5, 5.0],[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[260]=[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[300]=[6.0, 9.0, 6.0],[6.3, 9.45, 6.3],[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[350]=[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0]
HData[400]=[8.0, 12.0, 8.0],[10.0, 15.0, 10.0],[12.0, 18.0, 12.0],[12.5, 18.75, 12.5],[16.0, 24.0, 16.0],[20.0, 30.0, 20.0]
 
CData = {}
CData[20]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5]
CData[25]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0]
CData[30]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0]
CData[40]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0]
CData[50]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0]
CData[60]=[2.0, 4.0, 2.0],[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45]
CData[70]=[2.5, 5.0, 2.5],[3.0, 6.0, 3.0],[3.6, 7.2, 3.6],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45]
CData[80]=[3.0, 6.0, 3.0],[3.6, 7.2, 3.6],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0]
CData[90]=[3.0, 6.0, 3.0],[3.6, 7.2, 3.6],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0]
CData[100]=[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0]
CData[120]=[3.0, 6.0, 3.0],[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0]
CData[140]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0]
CData[150]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[160]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[180]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[200]=[4.0, 8.0, 4.0],[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[220]=[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[250]=[5.0, 10.0, 5.0],[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[260]=[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[300]=[6.0, 12.0, 6.0],[6.3, 15.75, 9.45],[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[350]=[8.0, 20.0, 12.0],[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
CData[400]=[10.0, 25.0, 15.0],[12.0, 36.0, 24.0],[12.5, 37.5, 25.0],[16.0, 48.0, 32.0]
 
 
#--- INPUT HERE ---#
print('Select hot or cold formed profiles')
print('0 = Hot\n1 = Cold')
HorC = int(Read())
 
if HorC == 0:
    PData = HData
else:
    PData = CData
 
 
print('Input dimension in mm, only integers')
print sorted(PData, key=lambda key: PData[key])
Size = int(Read())
 
 
print('Please select thickness')
for i,j in enumerate(PData[Size]):
    print i,'-',j[0],'mm'
 
readTh = int(Read())
 
Thick = PData[Size][readTh][0]
ro = PData[Size][readTh][1]
ri = PData[Size][readTh][2]
 
print('Please input length in mm')
Length = float(Read())
#--- INPUT STOP ---#
 
# all values are in millimeters
Units.Current = UnitTypes.Millimeters
 
# Create part
Square = Part('Hollow Section %dx%dx%d' % (Size,Thick,Length))
 
# Body
Profile = Square.AddSketch('Profile', Square.GetPlane('XY-Plane'))
# Outer square
Line = Polyline()
Line.AddPoint(PolylinePoint(-Size/2.,-Size/2))
Line.AddPoint(PolylinePoint(Size/2.,-Size/2))
Line.AddPoint(PolylinePoint(Size/2.,Size/2))
Line.AddPoint(PolylinePoint(-Size/2.,Size/2))
Line.AddPoint(PolylinePoint(-Size/2.,-Size/2))
Profile.AddPolyline(Line,False)
 
# Inner Square
scaleFactor = ((Size-(Thick*2.))/Size)*100.0
#print scaleFactor
Profile.CopyFrom(Profile,0,0,0,0,0,0,0,scaleFactor)
 
# Extrude
Square.AddExtrudeBoss('Extrude',Profile,Length,False)
 
# Outer radius
Square.AddFillet('Fillet<1>',[Square.GetEdge('Edge<6>'),Square.GetEdge('Edge<2>'),Square.GetEdge('Edge<4>'),Square.GetEdge('Edge<9>')],ro,False)
 
# Inner radius
Square.AddFillet('Fillet<2>',[Square.GetEdge('Edge<30>'),Square.GetEdge('Edge<31>'),Square.GetEdge('Edge<33>'),Square.GetEdge('Edge<35>')],ri,False)



# End of file: Square-hollow-formed-profiles.py


# Start of file: Supressing-Unsupressing-and-Removing-Features.py

#https://help.alibre.com/articles/#!alibre-help-v28/supressing-unsupressing-and-removing-features

# create a part
P = Part('Example Part')
 
# create a cube
CubeSketch = P.AddSketch('CubeProfile', P.GetPlane('XY-Plane'))
CubeSketch.AddRectangle(0, 0, 10, 10, False)
CubeFeature = P.AddExtrudeBoss('Cube', CubeSketch, 10, True)
 
# cut a hole in the cube
HoleSketch = P.AddSketch('HoleProfile', P.GetPlane('XY-Plane'))
HoleSketch.AddRectangle(2, 2, 8, 8, False)
HoleFeature = P.AddExtrudeCut('Hole', HoleSketch, 10, True)
 
# suppress the cube using the name of the feature
P.SuppressFeature('Cube')
# unsuppress the cube using the feature object
P.UnsuppressFeature(CubeFeature)
 
# remove the hole using the name of the feature
P.RemoveFeature('Hole')
# remove the hole sketch using the sketch object
P.RemoveSketch(HoleSketch)

# End of file: Supressing-Unsupressing-and-Removing-Features.py


# Start of file: Tool-Cutting.py

#https://help.alibre.com/articles/#!alibre-help-v28/tool-cutting

# cylinder dimensions
Diameter = 20
Length = 100

# cutter dimensions
CutterDiameter = 5

# angle to increase by on each pass of the cutter, in degrees
# must be a whole divisor of 180
StepAngle = 10

# total angle of cutting around the cylinder
TotalAngle = 1440

# starting distance from end of cylinder
StartX = 10

# create the cylinder
P = Part('Cylinder')
CylPlane = P.GetPlane('XY-Plane')
CrossSection = P.AddSketch('Cross-Section', CylPlane)
CrossSection.AddCircle(0,0, Diameter, False)
P.AddExtrudeBoss('Cylinder', CrossSection, Length, False)

# create the planes
Planes = []
NumPlanes = 180 / StepAngle
for PlaneIndex in range(0, NumPlanes):
  Angle = PlaneIndex * StepAngle
  Pl = P.AddPlane('P' + str(Angle), P.GetPlane('YZ-Plane'), P.GetAxis('Z-Axis'), Angle)
  Planes.append(Pl)
for PlaneIndex in range(0, NumPlanes):
  Planes.append(Planes[PlaneIndex])
NumPlanes = NumPlanes * 2

# start of helix has no offset along cylinder
XStep = 0

# create circle sketches then extrude cut 'through all'
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
  P.AddExtrudeCut('S' + str(Angle), Sk, 0, False, Part.EndCondition.ThroughAll, None, 0, Part.DirectionType.Normal, None, 0, False)

# End of file: Tool-Cutting.py


# Start of file: Triangle.py

#https://help.alibre.com/articles/#!alibre-help-v28/triangle

# Create triangle with angles 90, 15, 75
 
import math
 
# set up parameters
Theta = 15.0
Adjacent = 100.0
 
# calculate side
Opposite = Adjacent * math.tan(math.radians(Theta))
 
# generate three vertices of triangle
P1_X = 0
P1_Y = 0
 
P2_X = Adjacent
P2_Y = 0
 
P3_X = Adjacent
P3_Y = Opposite
 
# create part and sketch
P = Part('Foo')
S = P.AddSketch('Shape', P.GetPlane('XY-Plane'))
 
# draw it
S.AddLine(P1_X, P1_Y, P2_X, P2_Y, False)
S.AddLine(P2_X, P2_Y, P3_X, P3_Y, False)
S.AddLine(P3_X, P3_Y, P1_X, P1_Y, False)

# End of file: Triangle.py


# Start of file: Type-11-flanges-according-to-BS-EN-1092-PN16.py

#https://help.alibre.com/articles/#!alibre-help-v28/type-11-flanges-according-to-bs-en-1092-pn16


from math import cos,sin,radians
 
# Size of Flange TYPE 11 According to BS/EN-1092 PN16
 
#--- INPUT HERE ---#
print('Input DN Flange size: 10, 15, 20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600')
DN = int(Read())
#--- INPUT STOP ---#
 
# Measurements table D,C2,H2,H3,R,A,N1,d1,f1,K,L,N from here
#http://www.roymech.co.uk/Useful_Tables/Flanges/BSEN1092_16_Dimensions.html

DNData = {}
DNData[10] = [90,14,35,6,4,17.2,28,40,2,60,14,4]
DNData[15] = [95,14,35,6,4,21.3,32,45,2,65,14,4]
DNData[20] = [105,14,38,6,4,26.9,39,58,2,75,14,4]
DNData[25] = [115,16,38,6,4,33.7,46,68,2,85,14,4]
DNData[32] = [140,16,40,6,6,42.4,56,78,2,100,18,4]
DNData[40] = [150,16,42,7,6,48.3,64,88,2,110,18,4]
DNData[50] = [165,18,45,8,6,60.3,75,102,2,125,18,4]
DNData[65] = [185,18,45,10,6,76.1,90,122,2,145,18,4]
DNData[80] = [200,20,50,10,8,88.9,105,138,2,160,18,8]
DNData[100] = [220,20,52,12,8,114.3,131,158,2,180,18,8]
DNData[125] = [250,22,55,12,8,139.7,156,188,2,210,18,8]
DNData[150] = [285,22,55,12,10,168.3,192,212,2,240,22,8]
DNData[200] = [340,24,62,16,10,219.1,235,268,2,295,22,12]
DNData[250] = [405,26,70,16,12,273,292,320,2,355,26,12]
DNData[300] = [460,28,78,16,12,323.9,344,378,2,410,26,12]
DNData[350] = [520,30,82,16,12,355.6,390,438,2,470,26,16]
DNData[400] = [580,32,85,16,12,406.4,445,490,2,525,30,16]
DNData[450] = [640,40,87,16,12,457,490,550,2,585,30,20]
DNData[500] = [715,44,90,16,12,508,548,610,2,650,33,20]
DNData[600] = [840,54,95,18,12,610,652,725,2,770,36,20]
DNData[700] = [910,36,100,18,12,711,755,795,2,840,36,24]
DNData[800] = [1025,38,105,20,12,813,855,900,2,950,39,24]
DNData[900] = [1125,40,110,20,12,914,955,1000,2,1050,39,28]
DNData[1000] = [1255,42,120,22,16,1016,1058,1115,2,1170,42,28]
DNData[1200] = [1485,48,130,30,16,1219,1262,1330,2,1390,48,32]
DNData[1400] = [1685,52,145,30,16,1420,1465,1530,2,1590,48,36]
DNData[1600] = [1930,58,160,35,16,1620,1668,1750,2,1820,56,40]
 
 
D = DNData[DN][0]
C2 = DNData[DN][1]
H2 = DNData[DN][2]
H3 = DNData[DN][3]
R = DNData[DN][4]
A = DNData[DN][5]
N1 = DNData[DN][6]
d1 = DNData[DN][7]
f1 = DNData[DN][8]
K = DNData[DN][9]
L = DNData[DN][10]
N = DNData[DN][11]
 
# all values are in millimeters
Units.Current = UnitTypes.Millimeters
 
# Create part
Flange = Part('DN%d Flange PN16' % (DN))
 
# body
Profile = Flange.AddSketch('Profile', Flange.GetPlane('XY-Plane'))
Line = Polyline()
Line.AddPoint(PolylinePoint(DN/2.,0))
Line.AddPoint(PolylinePoint(d1/2.,0))
Line.AddPoint(PolylinePoint(d1/2.,f1))
Line.AddPoint(PolylinePoint(D/2.,f1))
Line.AddPoint(PolylinePoint(D/2.,C2))
Line.AddPoint(PolylinePoint(N1/2.,C2))
Line.AddPoint(PolylinePoint(A/2.,H2-H3))
Line.AddPoint(PolylinePoint(A/2.,H2))
Line.AddPoint(PolylinePoint(DN/2.,H2))
Line.AddPoint(PolylinePoint(DN/2.,0))
Profile.AddPolyline(Line,False)
Flange.AddRevolveBoss('Body', Profile, Flange.GetAxis('Y-Axis'),360)
 
#Chamfer
Flange.AddChamfer('Chamfer<1>',Flange.GetFace('Face<2>'),1,False)
 
#Fillet
Flange.AddFillet('Fillet<1>',[Flange.GetEdge('Edge<6>'),Flange.GetEdge('Edge<7>')],R,False)
 
# Hole
Hole = Flange.AddSketch('Hole',Flange.GetFace('Face<8>'))
for i in xrange(N):
    Ang = (360/N)*i
    Hole.AddCircle(sin(radians(Ang))*K/2.,cos(radians(Ang))*K/2.,L,False)
Flange.AddExtrudeCut('Flange Hole',Hole,C2,True)



# End of file: Type-11-flanges-according-to-BS-EN-1092-PN16.py


# Start of file: Units.py

#https://help.alibre.com/articles/#!alibre-help-v28/units

# demonstrates using multiple units in a script
 
# create a part and a sketch
MyPart = Part('My Part')
XYPlane = MyPart.GetPlane('XY-Plane')
Sketch = MyPart.AddSketch('Sketch', XYPlane)
 
# set units to mm - this is implied at the start of every script
Units.Current = UnitTypes.Millimeters
 
# create circle 50mm in diameter
Sketch.AddCircle(0, 0, 50, False)
 
# set units to inches
# all values from now on are in inches
Units.Current = UnitTypes.Inches
 
# create a circle 1.34 inches in diameter
Sketch.AddCircle(0, 0, 1.34, False)
 
# switch to cm
# now all values from this point until the next units change are in cm
Units.Current = UnitTypes.Centimeters
 
# create a circle 4.2cm in diameter
Sketch.AddCircle(0, 0, 4.2, False)

# End of file: Units.py


# Start of file: Useful-Dialogs.py

#https://help.alibre.com/articles/#!alibre-help-v28/useful-dialogs

Win = Windows()
 
Win.InfoDialog('I am about to create a part', 'My Script')
 
Win.ErrorDialog("Oops. That didn't go as planned", 'My Script')
 
# returns True for 'yes' and False for 'no'
print Win.QuestionDialog('Shall I stop?', 'My Script')

# End of file: Useful-Dialogs.py


# Start of file: Wave-washer.py

#https://help.alibre.com/articles/#!alibre-help-v28/wave-washer

import math
from math import *
 
# radius
R = 100.0
# amplitude
A = 10.0
# number of waves (must be a whole number)
B = 4
 
# width
Width = 10
# thickness
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
 
# path accuracy = lower number = more points calculated
t_step = 0.1
 
# complete circle = PI x 2
t_max = 3.141592 * 2
 
# keep track of the total points we have calculated
TotalPoints = 0
 
# calculate points for 3D sketch
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
 
  t = t + t_step
  TotalPoints = TotalPoints + 1
  if t >= t_max:
    break
 
# close path
PathPoints.extend([PathPoints[0], PathPoints[1], PathPoints[2]])
 
# create part and add 3d sketch
P = Part('Wave Washer')
Path = P.Add3DSketch('Path')
Path.AddBspline(PathPoints)
 
# calculate normal vector for the plane at the start of the path
normal_vector = [P2[0] - P1[0], P2[1] - P1[1], P2[2] - P1[2]]
 
# create plane at the start of the path
Plane = P.AddPlane('Start Plane', normal_vector, P1)
 
CrossSection = P.AddSketch('Cross Section', Plane)
 
Origin = CrossSection.GlobaltoPoint(P1[0], P1[1], P1[2])
 
CrossSection.AddRectangle(Origin[0] - (Thickness / 2.0), Origin[1] - (Width / 2.0), Origin[0] + (Thickness / 2.0), Origin[1] + (Width / 2.0), False)
 
P.AddSweepBoss('Washer', CrossSection, Path, False, Part.EndCondition.EntirePath, None, 0, 0, False)

# End of file: Wave-washer.py


# Start of file: Working-with-Configurations.py

#https://help.alibre.com/articles/#!alibre-help-v28/working-with-configurations

# create a new part
P = Part('Test')
 
# create a new configuration
Foo = P.AddConfiguration('Foo')
# it's already unlocked by default but this is how to unlock a configuration
Foo.UnlockAll()
# set a single lock
Foo.SetLocks(LockTypes.SuppressNewFeatures)
# set multiple locks
Foo.SetLocks(LockTypes.SuppressNewFeatures | LockTypes.LockColorProperties)
# activate the configuration
Foo.Activate()
 
# create a new configuration using 'Foo' as a base
Bar = P.AddConfiguration('Bar', 'Foo')
# activate it
Bar.Activate()
 
# get access to the default configuration and apply all locks to it
Config1 = P.GetConfiguration('Config<1>')
Config1.LockAll()
 
# show the name of the active configuration
ActiveConfig = P.GetActiveConfiguration()
print 'Current active configuration is: %s' % ActiveConfig.Name
 
# show the total number of configurations
print 'Total number of configurations: %d' % len(P.Configurations)
 
# show the name of the second configuration
print 'Second configuration is: %s' % P.Configurations[1].Name
 
# check if a couple of the confgurations are active
print 'Is second configuration active? %s' % ('yes' if P.Configurations[1].IsActive == True else 'no')
print 'Is configuration "Bar" active? %s' % ('yes' if Bar.IsActive == True else 'no')

# End of file: Working-with-Configurations.py

#lab 3 Построение параболойда

from math import pi

from OCC.Core.TColgp import TColgp_Array2OfPnt
from OCC.Core.TopoDS import TopoDS_Face
from OCC.Core.gp import gp_Pnt2d, gp_XOY, gp_Lin2d, gp_Ax3, gp_Dir2d, gp_Pnt
from OCC.Core.AIS import AIS_Shape
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeFace, BRepBuilderAPI_MakeShape
from OCC.Core.Geom import Geom_BezierSurface
from OCC.Core.GCE2d import GCE2d_MakeSegment

from OCC.Display.SimpleGui import init_display

display, start_display, add_menu, add_function_to_menu = init_display()

def decimal_range(start, stop, increment):
    while start < stop:
        yield start
        start += increment

# points
arraySize = 25
points = TColgp_Array2OfPnt(0, arraySize-1, 0, arraySize-1)
a = 5
b = 5
for i in range(0, arraySize):
    for j in range(0, arraySize):
        x = i - arraySize // 2
        y = j - arraySize // 2
        z = ((x * x) / (2 * a)) + ((y * y) / (2 * b))
        points.SetValue(i, j, gp_Pnt(x, y, z))

# Build paraboloid
paraboloid = Geom_BezierSurface(points)
face = BRepBuilderAPI_MakeFace(paraboloid, 0.05).Face()
# display.DisplayShape(face, update=True)
# start_display()

ais_shp = AIS_Shape(face)
ais_shp.SetWidth(1)

ais_context = display.GetContext()
ais_context.Display(ais_shp, True)

display.View_Iso()
display.FitAll()
start_display()
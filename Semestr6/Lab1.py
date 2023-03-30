from OCC.Core.AIS import AIS_Shape
from OCC.Core.gp import gp_Pnt
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeVertex, BRepBuilderAPI_MakePolygon, BRepBuilderAPI_MakeFace

from OCC.Display.SimpleGui import init_display
from OCC.Extend.TopologyUtils import TopologyExplorer

display, start_display, add_menu, add_function_to_menu = init_display()

#Задаем точки
point1 = gp_Pnt(1, 0, 0)
point2 = gp_Pnt(0, 1, 0)
point3 = gp_Pnt(0, 0, 1)

#Строим вертексы
v1 = BRepBuilderAPI_MakeVertex(point1).Vertex()
v2 = BRepBuilderAPI_MakeVertex(point2).Vertex()
v3 = BRepBuilderAPI_MakeVertex(point3).Vertex()

#Wire
wire1 = BRepBuilderAPI_MakePolygon(v1, v2, v3, True).Wire()

#Строим 1 треугольник
triangle1 = BRepBuilderAPI_MakeFace(wire1).Face()
ais_shp = AIS_Shape(triangle1)
ais_shp.SetWidth(1)

#display
ais_context = display.GetContext()
ais_context.Display(ais_shp, True)

display.View_Iso()
display.FitAll()
start_display()
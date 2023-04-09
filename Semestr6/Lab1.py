from OCC.Core.AIS import AIS_Shape
from OCC.Core.Quantity import Quantity_Color, Quantity_NameOfColor
from OCC.Core.gp import gp_Pnt
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeVertex, BRepBuilderAPI_MakePolygon, BRepBuilderAPI_MakeFace
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Common, BRepAlgoAPI_Section


from OCC.Display.SimpleGui import init_display
from OCC.Extend.TopologyUtils import TopologyExplorer

display, start_display, add_menu, add_function_to_menu = init_display()

#Задаем точки
point1 = gp_Pnt(0, 0, 10)
point2 = gp_Pnt(10, 0, 0)
point3 = gp_Pnt(0, 0, 0)

#Строим вертексы
v1 = BRepBuilderAPI_MakeVertex(point1).Vertex()
v2 = BRepBuilderAPI_MakeVertex(point2).Vertex()
v3 = BRepBuilderAPI_MakeVertex(point3).Vertex()

#Wire
wire1 = BRepBuilderAPI_MakePolygon(v1, v2, v3, True).Wire()

#Строим 1 треугольник
triangle1 = BRepBuilderAPI_MakeFace(wire1).Face()
ais_shp1 = AIS_Shape(triangle1)
ais_shp1.SetWidth(1)
ais_shp1.SetColor(Quantity_Color(Quantity_NameOfColor.Quantity_NOC_BLUE))

#Задаем точки
point4 = gp_Pnt(0, 7, 1)
point5 = gp_Pnt(15, -5, 0)
point6 = gp_Pnt(5, 0, 10)

#Строим вертексы
v4 = BRepBuilderAPI_MakeVertex(point4).Vertex()
v5 = BRepBuilderAPI_MakeVertex(point5).Vertex()
v6 = BRepBuilderAPI_MakeVertex(point6).Vertex()

#Wire
wire2 = BRepBuilderAPI_MakePolygon(v4, v5, v6, True).Wire()

#Строим 2 треугольник
triangle2 = BRepBuilderAPI_MakeFace(wire2).Face()
ais_shp2 = AIS_Shape(triangle2)
ais_shp2.SetWidth(1)
ais_shp2.SetColor(Quantity_Color(Quantity_NameOfColor.Quantity_NOC_GREEN))

#Ищем пересечение треугольников
common = BRepAlgoAPI_Common(triangle1, triangle2)
section = BRepAlgoAPI_Section(triangle1, triangle2)
section.ComputePCurveOn1(True)
section.Approximation(True)
section.Build()
ais_shp3 = AIS_Shape(section.Shape())
ais_shp3.SetWidth(5)
ais_shp3.SetColor(Quantity_Color(Quantity_NameOfColor.Quantity_NOC_RED))

#дисплей
ais_context = display.GetContext()
ais_context.Display(ais_shp1, True)
ais_context.Display(ais_shp2, True)
ais_context.Display(ais_shp3, True)

display.View_Iso()
display.FitAll()
start_display()

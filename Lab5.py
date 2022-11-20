#Построение конструктивных элементов


from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.Graphic3d import Graphic3d_NameOfMaterial, Graphic3d_NOM_COPPER, Graphic3d_MaterialAspect
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Core.AIS import AIS_Shape, AIS_Shaded


from OCC.Display.SimpleGui import init_display

display, start_display, add_menu, add_function_to_menu = init_display()

#Основное
boxmain = BRepPrimAPI_MakeBox(140.0, 280.0, 30.0).Shape()
axe1 = gp_Ax2(gp_Pnt(110, 30, 0), gp_Dir(0, 0, 1))
cylinder1 = BRepPrimAPI_MakeCylinder(axe1, 15, 30).Shape()
cut1 = BRepAlgoAPI_Cut(boxmain, cylinder1).Shape()
axe2 = gp_Ax2(gp_Pnt(110,30,30), gp_Dir(0, 0, 1))
cylinder2 = BRepPrimAPI_MakeCylinder(axe2, 30, 45).Shape()
cylinder3 = BRepPrimAPI_MakeCylinder(axe2, 15, 45).Shape()
cut2 = BRepAlgoAPI_Cut(cylinder2, cylinder3).Shape()
fuse1 = BRepAlgoAPI_Fuse(cut1, cut2).Shape()


#Стенки
Box1 = BRepPrimAPI_MakeBox(30.0, 280.0, 100.0).Shape()
Box2 = BRepPrimAPI_MakeBox(gp_Pnt(0, 250, 0),140.0, 30, 100.0).Shape()
fuse2 = BRepAlgoAPI_Fuse(fuse1, Box1).Shape()
fuse3 = BRepAlgoAPI_Fuse(fuse2, Box2).Shape()


#Вырез полуокружности
Box3 = BRepPrimAPI_MakeBox(gp_Pnt(0, 125, 80),30, 50, 100.0).Shape()
axe3 = gp_Ax2(gp_Pnt(0, 150, 80), gp_Dir(1, 0, 0))
cylinder4 = BRepPrimAPI_MakeCylinder(axe3, 25, 30).Shape()
fuse4 = BRepAlgoAPI_Fuse(Box3, cylinder4).Shape()
cut3 = BRepAlgoAPI_Cut(fuse3, fuse4).Shape()


#скос углов






aisShape = AIS_Shape(cut3)

ais_context = display.GetContext()
ais_context.Display(aisShape, True)

display.View_Iso()
display.FitAll()
start_display()
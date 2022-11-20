#Построение деталей

from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.Graphic3d import Graphic3d_NameOfMaterial, Graphic3d_NOM_COPPER, Graphic3d_MaterialAspect
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Core.AIS import AIS_Shape, AIS_Shaded

from OCC.Display.SimpleGui import init_display

display, start_display, add_menu, add_function_to_menu = init_display()

axe1 = gp_Ax2(gp_Pnt(2.5, 2.5, 0), gp_Dir(0, 0, 1))
box1 = BRepPrimAPI_MakeBox(50.0, 50.0, 50.0).Shape()
box2 = BRepPrimAPI_MakeBox(axe1, 45.0, 45.0, 45.0).Shape()
cut = BRepAlgoAPI_Cut(box1, box2).Shape()
axe2 = gp_Ax2(gp_Pnt(25, 25, 50), gp_Dir(0, 0, 1))
cylinder = BRepPrimAPI_MakeCylinder(axe2, 15, 50).Shape()
fuse = BRepAlgoAPI_Fuse(cut, cylinder).Shape()



aisShape = AIS_Shape(fuse)

ais_context = display.GetContext()
ais_context.Display(aisShape, True)

display.View_Iso()
display.FitAll()
start_display()
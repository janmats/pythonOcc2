from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.Graphic3d import Graphic3d_NameOfMaterial, Graphic3d_NOM_COPPER, Graphic3d_MaterialAspect
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Core.AIS import AIS_Shape, AIS_Shaded


from OCC.Display.SimpleGui import init_display

display, start_display, add_menu, add_function_to_menu = init_display()

box = BRepPrimAPI_MakeBox(50.0, 50.0, 10.0).Shape()
axe = gp_Ax2(gp_Pnt(25, 25, 10), gp_Dir(0, 0, 1))
cylinder1 = BRepPrimAPI_MakeCylinder(axe, 12.5, 40).Shape()
cylinder2 = BRepPrimAPI_MakeCylinder(axe, 7.5, 40).Shape()
cut = BRepAlgoAPI_Cut(cylinder1, cylinder2).Shape()
fuse = BRepAlgoAPI_Fuse(box, cut).Shape()

aisShape = AIS_Shape(fuse)
copper = Graphic3d_NameOfMaterial(Graphic3d_NOM_COPPER)
material = Graphic3d_MaterialAspect(copper)
aisShape.SetMaterial(material)
aisShape.SetDisplayMode(AIS_Shaded)
aisShape.SetTransparency(0)

ais_context = display.GetContext()
ais_context.Display(aisShape, True)

display.View_Iso()
display.FitAll()
start_display()

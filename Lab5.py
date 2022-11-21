#Построение конструктивных элементов


from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeFillet, BRepFilletAPI_MakeChamfer
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.Graphic3d import Graphic3d_NameOfMaterial, Graphic3d_NOM_COPPER, Graphic3d_MaterialAspect
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Core.AIS import AIS_Shape, AIS_Shaded
from OCC.Core.GC import GC_MakeArcOfCircle, GC_MakeSegment


from OCC.Display.SimpleGui import init_display
from OCC.Extend.TopologyUtils import TopologyExplorer

display, start_display, add_menu, add_function_to_menu = init_display()

#Основное
boxmain = BRepPrimAPI_MakeBox(140.0, 280.0, 30.0).Shape()

#rake
rake = BRepFilletAPI_MakeFillet(boxmain)
expl = list(TopologyExplorer(boxmain).edges())
rake.Add(30, 30, expl[4])
rake.Build()
evolved_boxmain = rake.Shape()

axe1 = gp_Ax2(gp_Pnt(110, 30, 0), gp_Dir(0, 0, 1))
cylinder1 = BRepPrimAPI_MakeCylinder(axe1, 15, 30).Shape()


cut1 = BRepAlgoAPI_Cut(evolved_boxmain, cylinder1).Shape()
axe2 = gp_Ax2(gp_Pnt(110,30,30), gp_Dir(0, 0, 1))
cylinder2 = BRepPrimAPI_MakeCylinder(axe2, 30, 45).Shape()

#chamfer cylinder2
chamfer3 = BRepFilletAPI_MakeChamfer(cylinder2)
expl = list(TopologyExplorer(cylinder2).edges())
cylinder2faces = list(TopologyExplorer(cylinder2).faces())
chamfer3.Add(4.0, 4.0, expl[0], cylinder2faces[0])
chamfer3.Build()
evolved_cylinder2 = chamfer3.Shape()

cylinder3 = BRepPrimAPI_MakeCylinder(axe2, 17, 45).Shape()

#rake_cylinder3
rake1 = BRepFilletAPI_MakeFillet(cylinder3)
expl = list(TopologyExplorer(cylinder3).edges())
rake1.Add(2, 0, expl[2])
rake1.Build()
evolved_cylinder3 = rake1.Shape()

cut2 = BRepAlgoAPI_Cut(evolved_cylinder2, evolved_cylinder3).Shape()
fuse1 = BRepAlgoAPI_Fuse(cut1, cut2).Shape()


#Стенки
Box1 = BRepPrimAPI_MakeBox(30.0, 280.0, 100.0).Shape()

#chamfer box1
chamfer1 = BRepFilletAPI_MakeChamfer(Box1)
expl = list(TopologyExplorer(Box1).edges())
box1faces = list(TopologyExplorer(Box1).faces())
chamfer1.Add(15.0, 30.0, expl[9], box1faces[0])
chamfer1.Build()
evolved_box1 = chamfer1.Shape()

Box2 = BRepPrimAPI_MakeBox(gp_Pnt(0, 250, 0), 140.0, 30, 100.0).Shape()

#chamfer box1
chamfer2 = BRepFilletAPI_MakeChamfer(Box2)
expl = list(TopologyExplorer(Box2).edges())
box2faces = list(TopologyExplorer(Box2).faces())
chamfer2.Add(20.0, 20.0, expl[5], box2faces[0])
chamfer2.Build()
evolved_box2 = chamfer2.Shape()

fuse2 = BRepAlgoAPI_Fuse(fuse1, evolved_box1).Shape()
fuse3 = BRepAlgoAPI_Fuse(fuse2, evolved_box2).Shape()


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
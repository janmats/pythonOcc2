from tkinter import simpledialog, Tk

from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeFillet, BRepFilletAPI_MakeChamfer
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.Graphic3d import Graphic3d_NameOfMaterial, Graphic3d_NOM_COPPER, Graphic3d_MaterialAspect
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir, gp_Ax1
from OCC.Core.AIS import AIS_Shape, AIS_Shaded
from OCC.Core.GC import GC_MakeArcOfCircle, GC_MakeSegment
from OCC.Core.GProp import GProp_GProps
from OCC.Core.BRepGProp import BRepGProp_EdgeTool_Value, BRepGProp_EdgeTool, brepgprop_LinearProperties

from OCC.Display.SimpleGui import init_display
from OCC.Extend.TopologyUtils import TopologyExplorer


def line_clicked(shp, *kwargs):
    for edge in shp: # this should be a TopoDS_Edge
      print("Edge selected: ", edge)
      props = GProp_GProps()
      brepgprop_LinearProperties(edge, props)
      length = props.Mass()
      print("Длина: %f" % length)


def buildfigure(x: float):

    #Нижняя площадка
    boxmain = BRepPrimAPI_MakeBox(42.0/70.0*x, 26.0/70.0*x, 7.0/70.0*x).Shape()

    chamfer1 = BRepFilletAPI_MakeChamfer(boxmain)
    expl = list(TopologyExplorer(boxmain).edges())
    boxmainfaces = list(TopologyExplorer(boxmain).faces())
    chamfer1.Add(4.0/70.0*x, 30.0/70.0*x, expl[4], boxmainfaces[0])
    chamfer1.Add(4.0/70.0*x, 30.0/70.0*x, expl[6], boxmainfaces[0])
    chamfer1.Build()
    evolved_box1 = chamfer1.Shape()

    #вырезание полукруга

    axe1 = gp_Ax2(gp_Pnt(34/70.0*x, 8/70.0*x, 0), gp_Dir(0, 0, 1))
    box1 = BRepPrimAPI_MakeBox(axe1, 8.0/70.0*x, 10.0/70.0*x, 7.0/70.0*x).Shape()
    cut1 = BRepAlgoAPI_Cut(evolved_box1, box1).Shape()
    axe2 = gp_Ax2(gp_Pnt(34/70.0*x, 13/70.0*x, 0/70.0*x), gp_Dir(0, 0, 1))
    cylinder1 = BRepPrimAPI_MakeCylinder(axe2, 5.0/70.0*x, 7.0/70.0*x).Shape()
    cut2 = BRepAlgoAPI_Cut(cut1, cylinder1).Shape()
    box2 = BRepPrimAPI_MakeBox(7.0/70.0*x, 26.0/70.0*x, 28.0/70.0*x,).Shape()
    fuse1 = BRepAlgoAPI_Fuse(cut2, box2).Shape()
    axe3 = gp_Ax2(gp_Pnt(-14.0/70.0*x, 8.0/70.0*x, 0.0/70.0*x), gp_Dir(0, 0, 1))
    box3 = BRepPrimAPI_MakeBox(axe3, 14.0/70.0*x, 10.0/70.0*x, 28.0/70.0*x).Shape()
    axe4 = gp_Ax2(gp_Pnt(-14.0/70.0*x, 8.0/70.0*x, 14.0/70.0*x), gp_Dir(0, 1, 0))
    cylinder2 = BRepPrimAPI_MakeCylinder(axe4, 14.0/70.0*x, 10.0/70.0*x).Shape()
    fuse2 = BRepAlgoAPI_Fuse(fuse1, box3).Shape()
    fuse3 = BRepAlgoAPI_Fuse(fuse2, cylinder2).Shape()
    cylinder3 = BRepPrimAPI_MakeCylinder(axe4, 7.0/70.0*x, 10.0/70.0*x).Shape()
    cut3 = BRepAlgoAPI_Cut(fuse3, cylinder3).Shape()

    aisShape = AIS_Shape(cut3)

    ais_context = display.GetContext()
    ais_context.Display(aisShape, True)

    display.View_Iso()
    display.FitAll()
    return display


if __name__ ==  "__main__":
    display, start_display, add_menu, add_function_to_menu = init_display()
    #x = 70.0
    Tk().withdraw()
    x = simpledialog.askfloat("Введите размер", "x")
    display = buildfigure(x)
    display.SetSelectionModeEdge()  # switch to edge selection mode
    display.register_select_callback(line_clicked)
    start_display()
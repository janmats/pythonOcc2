#lab1 Запуск OCC на пайтон

from OCC.Display.SimpleGui import init_display
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox

display, start_display, add_menu, add_function_to_menu = init_display()
box1 = BRepPrimAPI_MakeBox(10., 10., 10.).Shape()

display.DisplayShape(box1, update=True)
start_display()
from OCC.Extend.DataExchange import STEPControl_Reader
from OCC.Display.SimpleGui import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from OCC.Extend.DataExchange import read_iges_file


def open_stp (event=None):
    Tk().withdraw()
    filename = askopenfilename()
    step_reader = STEPControl_Reader()
    step_reader.ReadFile(filename)
    step_reader.TransferRoot()
    myshape = step_reader.Shape()

    display.DisplayShape(myshape, update=True)

def open_IGES (event=None):
    Tk().withdraw()
    filename = askopenfilename()
    myshape = read_iges_file(filename)

    display.DisplayShape(myshape, update=True)


def erase_all (event=None):
    display.EraseAll()

def exit (event=None):
    sys.exit()


if __name__ == '__main__':


    display, start_display, add_menu, add_function_to_menu = init_display()

    add_menu ('menu')
    add_function_to_menu ('menu',open_stp)
    add_function_to_menu('menu', open_IGES)
    add_function_to_menu ('menu',erase_all)
    add_function_to_menu ('menu',exit)


    start_display()
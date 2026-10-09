import ctypes
from customtkinter import *

def remove_topBar(parent):
      parent.overrideredirect(True)

def round_corners(parent):
        parent.update_idletasks()
        parent.update()
        
        hwnd = ctypes.windll.user32.GetParent(parent.winfo_id())

        DWMWA_WINDOW_CORNER_PREFERENCE = 33
        DWMWCP_ROUND = 2

        preference = ctypes.c_int(DWMWCP_ROUND)

        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            hwnd,
            DWMWA_WINDOW_CORNER_PREFERENCE,
            ctypes.byref(preference),
            ctypes.sizeof(preference)
        )

def reduceAppWithNoTopBar(parent):
    parent.overrideredirect(False)
    parent.update_idletasks() 
    parent.iconify()
    parent.bind("<Map>", lambda event: getAppReady(event, parent))

def getAppReady(event, parent):
    if event.widget is not parent:
        return
    parent.unbind("<Map>")
    parent.after(10, lambda: ShowApp(parent))

def ShowApp(parent):
    parent.overrideredirect(True)
    round_corners(parent)



def bold():
    return CTkFont(family="Arial", size=13, weight="bold")
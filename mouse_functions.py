import win32api
import win32con
import time


def left_click():
    win32api.mouse_event(win32.con.MOUSEEVENT_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32.con.MOUSEEVENT_LEFTUP, 0, 0)


def move_mouse(cords):
    win32api.SetCursosPos(cords)


def get_cords():
    x, y = win32api.GetCursorPos()
    return x, y

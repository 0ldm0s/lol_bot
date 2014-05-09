import win32api
import win32con
import time


def left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def move_mouse(cords):
    win32api.SetCursorPos(cords)


def get_cords():
    x, y = win32api.GetCursorPos()
    return x, y

if __name__ == '__main__':
	print get_cords()
	time.sleep(10)

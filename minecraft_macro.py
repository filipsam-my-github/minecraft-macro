import keyboard
import win32api
import win32con
import time
import threading
import sys,pyautogui

click_info = {"right": False, "left": False}
def on_press(key):
    try:
        if key.name == "r":
            click_info["right"] = not click_info["right"]
        elif key.name == "f":
            click_info["left"] = not click_info["left"]
    except:
        pass
 
def clicking():
    while True: 
        if click_info["right"]:
            time.sleep(0.0155)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            time.sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        elif click_info["left"]:
            time.sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            time.sleep(0.001)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
        else:
            time.sleep(0.01)

keyboard.on_press(on_press)

threading.Thread(target=clicking).start()


from re import match
import pyautogui, pygetwindow as gw 
from pywinauto.application import Application as ap
import os
from datetime import datetime

def get_window(title):
    try:
        # Finds title within a string, activates the window if found
        find_title = next(filter(lambda p: title in p, gw.getAllTitles()))
        match = gw.getWindowsWithTitle(find_title)[0]
        return match
    except Exception as e:
        print(f"Window not found: {e}")
        return None
        
def activate_window(window):
    try:
        app = ap().connect(handle=window._hWnd)
        app.top_window().set_focus()
        
        return True
    except Exception as e:
        print(f"Window not found: {e}")
        return False

def kill_window(window):
    try:
        win = ap().connect(handle=window._hWnd)
        if ap.kill(self=win):
            return True
    except Exception as e:
        print(f"Window was not found {e}")
        return False 

def move_window(window,x,y):
    try:
        window.moveTo(x,y)
        
    except Exception as e:
        print(f"Error: {e}")

def resize_window(window, x, y):
    try:
        window.resize(x,y)
    except Exception as e:
        print(f"Error {e}")

# Screenshots given window and puts it in the "Screenshots" folder
def screenshot_window(window, name, retImg):
    try:
        x,y = window.topleft
        
        if name is None:
            str(name)
            name = f"{window.title}-{str.replace(str.replace(str(datetime.now().time()), ".", "_"),":","-")}.png"
        absDir = os.path.abspath(__file__)
        relDir = f"{os.path.dirname(os.path.dirname(absDir))}\\Screenshots"
        fullPath = os.path.join(relDir, name)
        screenshot_image = pyautogui.screenshot(imageFilename=fullPath, region=[x,y,window.width,window.height],allScreens=False)
        if retImg:
            return screenshot_image
    except Exception as e:
        print(f"Error {e}")

def clear_screenshot_cache():
    screen_path = f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\\Screenshots"
    for e in os.listdir(screen_path):
        os.remove(f"{screen_path}\\{e}")


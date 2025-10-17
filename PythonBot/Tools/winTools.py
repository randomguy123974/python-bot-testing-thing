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
        #Gets top left for region
        x,y = window.topleft

        #If not given a name, window title + time of screenshot is given as name.
        if name is None:
            time_stamp = str.replace(datetime.now().strftime("%D-%H-%M-%S"),"/","_")
            name = f"{window.title}-{time_stamp}.png"
        
        # Getting the path for "Screenshots folder"
        absDir = os.path.abspath(__file__)
        relDir = os.path.join(os.path.dirname(os.path.dirname(absDir)),"Screenshots")
        
        os.makedirs(relDir, exist_ok=True) # If it doesn't exist create new folder

        #Create path for image directory/name
        fullPath = os.path.join(relDir, name)
        screenshot_image = pyautogui.screenshot(imageFilename=fullPath, region=[x,y,window.width,window.height],allScreens=False)
        
        if retImg: # If image needs to be returned, return (for image detection or smth)
            return screenshot_image
        
    except Exception as e:
        print(f"{window.title} experienced an error when screenshotting : {e}")

def clear_screenshot_cache():
    screen_path = f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\\Screenshots"
    for e in os.listdir(screen_path):
        os.remove(f"{screen_path}\\{e}")

clear_screenshot_cache()
window = gw.getActiveWindow()
screenshot_window(window=window, name=None, retImg=False)

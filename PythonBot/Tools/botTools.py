from pyautogui import *
import time
import keyboard
import pyautogui
import random
import win32api, win32con, win32gui


# Variables
GameStarted = False # Variable to track if the game has started
BotOn = False # Variable to control the bot state

# Methods

def click_image(imageDirectory, confidence, grayscale):
    try:
        imageDirectory = "Resource\\" + imageDirectory
        if pyautogui.locateOnScreen(imageDirectory, grayscale=grayscale, confidence=confidence) is not None:
            image_location = pyautogui.locateOnScreen(imageDirectory, grayscale=grayscale, confidence=confidence)
            image_center = pyautogui.center(image_location)
            click(image_center.x, image_center.y)
            print("Image Clicked")
    except Exception as e:
        print(f"Error locating image: {e}")

def click(x,y,delay): # Set curser position and click
    if not delay:
        delay = random.uniform(0.01,0.1) # Random delay between 10-100ms if not chosen
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(delay) # Click delay
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

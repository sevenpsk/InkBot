from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import datetime
import os

def locateMainScreen():
    location = pyautogui.locateOnScreen('vdoPromo.png', region=(0,30,450,815))
    return location

def locateExitAdScreen():
    location = None
    if pyautogui.locateOnScreen('ad1.png', region=(0,30,450,80)) != None:
        location = pyautogui.locateOnScreen('ad1.png', region=(0,30,450,80))
        print(f'found it at {location}')
    else:
        print('I cannot find')
    return location

def locateFreeInk():
    location = pyautogui.locateOnScreen('freeinkbtn.png', confidence=0.8, region=(116,32,755,810))
    return location

def locateExitAdScreen2():
    path = 'C:\\Users\\SEVEN\\Desktop\\Tutorial\\adCloseBtn'
    files = os.listdir(path)
    location = None
    for f in files:
        location = pyautogui.locateOnScreen('adCloseBtn\\'+str(f), confidence=0.8, region=(416,32,455,210))
        if location != None:
            return location
            quit
    return location



print(locateExitAdScreen2())
keyboard.send('Esc')
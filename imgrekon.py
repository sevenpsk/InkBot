from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    location = pyautogui.locateOnScreen('vdoPromo.png', region=(0,30,450,815))
    if location != None:
        print(f'I can see it at {location}')
        time.sleep(1)
    else:
        print('I am unable to see it')
        time.sleep(1)
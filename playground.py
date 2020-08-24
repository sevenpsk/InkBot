from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import datetime
import os

def locate_exit_ad_screen2():
    print('execute exit ad screen')
    path = 'C:\\Users\\SEVEN\\Desktop\\Project\\InkBot\\adCloseBtn\\'
    print(path)
    files = os.listdir(path)
    for f in files:
        print(f)
        location = pyautogui.locateOnScreen(path+str(f), confidence=0.8, region=(233,253,152,47))
    return location


loc = locate_exit_ad_screen2()

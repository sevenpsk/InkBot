from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import datetime
import os


def save_scope_image():
    iml = pyautogui.screenshot(region=(screen_left,screen_top,screen_width,screen_height))
    iml.save(r"C:\Users\SEVEN\Desktop\Project\InkBot\area.png")

def locate_main_screen():
    location = pyautogui.locateOnScreen('vdoPromo.png',confidence=0.8, region=(screen_left,screen_top,screen_width,screen_height))
    return location

def locate_exit_claim_ink():
    location = pyautogui.locateOnScreen('okbtn.png', confidence=0.8, region=(screen_left,screen_top,screen_width,screen_height))
    return location

def locate_spill_ink():
    location = pyautogui.locateOnScreen('spillink.png', confidence=0.9, region=(screen_left,screen_top,screen_width,screen_height))
    return location

def locate_exit_ad_screen2():
    path = 'C:\\Users\\SEVEN\\Desktop\\Tutorial\\adCloseBtn'
    files = os.listdir(path)
    for f in files:
        location = pyautogui.locateOnScreen('adCloseBtn\\'+str(f), confidence=0.8, region=(screen_left,screen_top,screen_width,screen_height))
        if location != None:
            return location


def locate_free_ink():
    location = pyautogui.locateOnScreen('freeinkbtn.png', confidence=0.8, region=(screen_left,screen_top,screen_width,screen_height))
    return location

def locate_gplay():
    location = pyautogui.locateOnScreen('gplayheader.PNG', confidence=0.8, region=(screen_left,screen_top,screen_width,screen_height))
    return location

def click_back():
    backbtn = pyautogui.locateOnScreen('backbtn.png', region=(screen_left+screen_width,screen_top,screen_width+50,screen_height))
    if backbtn != None:
        click(backbtn.left+10,backbtn.top+10)
    else:
        keyboard.send('Esc')
    time.sleep(1.5)

def click_close_top_right():
    click(764,56)

def capture_stuck_screen(filename):
    iml = pyautogui.screenshot(region=(116,32,755,810))
    iml.save(r"C:\\Users\\SEVEN\Desktop\\Tutorial\\StuckScreen\\"+str(filename)+".png")
    print(f'image no {stuck_img_counter} saved')



#identify app screen
scope = pyautogui.locateOnScreen('mainscreen.png', confidence=0.6, region=(0,0,1000,850))
if(scope!=None):
    screen_left = scope.left
    screen_top = scope.top
    screen_width = scope.width
    screen_height = scope.height
    print(scope)
else:
    print('scope not found')
    #debug scope injection
    screen_left = 176
    screen_top = 33
    screen_width = 455
    screen_height = 808

#save_scope_image()


scope = pyautogui.locateOnScreen('mainscreen.png', confidence=0.6, region=(0,0,1000,850))
print(scope)
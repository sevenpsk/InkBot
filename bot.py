from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import datetime
import os


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

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

def identify_app_screen():
    scope = pyautogui.locateOnScreen('mainscreen.png', confidence=0.6, region=(0,0,1000,850))
    if(scope!=None):
        return scope
    else:
        return None


StuckCounter = 0
stuck_img_counter = 0

#identify app screen
scope = identify_app_screen()
if(scope == None):
    print('App screen not found :(')
else:
    print('App screen has been identified')
    screen_left = scope.left
    screen_top = scope.top
    screen_width = scope.width
    screen_height = scope.height

print(scope)

#while ((keyboard.is_pressed('q') == False)):
while (keyboard.is_pressed('q') == False):
    try:
        #write picture what it see
        #save_scope_image()

        #Main program
        if locate_spill_ink() != None:
            claimSpillInk = locate_spill_ink()
            print(f'I can see unclaim Ink at{claimSpillInk}')
            sleep(0.5)
            click(claimSpillInk.left+20,claimSpillInk.top+50)
            time.sleep(1)
            #locate back btn and click
            click_back()
            
        elif locate_gplay() != None:
            googleplayscreen = locate_gplay()
            print('I can see GooglePlay')
            time.sleep(0.5)
            click_back()
            time.sleep(1)
        
        elif locate_exit_claim_ink() != None:
            exitClaimInk = locate_exit_claim_ink()
            print(f'I can see "OK button" at {exitClaimInk}')
            time.sleep(0.5)
            click(exitClaimInk.left+30,exitClaimInk.top+10)
            time.sleep(1.5)
            if datetime.datetime.now().minute == 0 :
                click_back()
            
        elif locate_main_screen() != None:
            location = locate_main_screen()
            print(f'I can see "WatchVDO buttton" at {location}')
            time.sleep(0.5)
            click(location.left+80,location.top+50)
            time.sleep(5)
            StuckCounter = 0

        elif locate_free_ink() != None:
            freeInkBtn = locate_free_ink()
            print(f'I can see "Free ink button" at {freeInkBtn}')
            time.sleep(0.5)
            click(freeInkBtn.left+50,freeInkBtn.top+20)

        elif locate_exit_ad_screen2() != None:
            exitAdsScreen = locate_exit_ad_screen2()
            print(f'I can see "close button" at {exitAdsScreen}')
            time.sleep(1)
            click(exitAdsScreen.left+10,exitAdsScreen.top+10)
            time.sleep(3)
            StuckCounter=0
        
        elif datetime.datetime.now().minute == 1:
            click_back()
            print('click_back for refresh')

        elif pyautogui.locateOnScreen('hourlyMax.png', confidence=0.8, region=(116,32,755,810)) != None:
            print(f'hourly max! {StuckCounter}/15')
            sleep(5)
            StuckCounter+=1
            if StuckCounter > 15:
                print('too long try to refresh')
                click_back()
                StuckCounter = 0

        else:
            print(f'nope {StuckCounter}/20')
            sleep(1)
            StuckCounter+=1
            if(StuckCounter>20):
                stuck_img_counter += 1
                if stuck_img_counter < 20:
                    capture_stuck_screen(stuck_img_counter)
                click_back()
                click_close_top_right()
                StuckCounter=0
    except:
        pass


            
        
        


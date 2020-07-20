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

def locate_main_screen():
    location = pyautogui.locateOnScreen('vdoPromo.png',confidence=0.8, region=(116,32,755,810))
    return location

def locate_exit_claim_ink():
    location = pyautogui.locateOnScreen('okbtn.png', confidence=0.8, region=(116,32,755,810))
    return location

def locate_spill_ink():
    location = pyautogui.locateOnScreen('spillink.png', confidence=0.9, region=(116,32,755,810))
    return location

def locate_exit_ad_screen():
    if pyautogui.locateOnScreen('adCloseBtn\\ad1.png', confidence=0.6, region=(416,32,455,210)) != None:
        location = pyautogui.locateOnScreen('adCloseBtn\\ad1.png', confidence=0.6, region=(416,32,455,210))
    elif pyautogui.locateOnScreen('adCloseBtn\\ad2.png', region=(416,32,455,210)) != None:
        location = pyautogui.locateOnScreen('adCloseBtn\\ad2.png', region=(416,32,455,210))
    elif pyautogui.locateOnScreen('adCloseBtn\\ad3.png', confidence=0.7, region=(416,32,455,210)) != None:
        location = pyautogui.locateOnScreen('adCloseBtn\\ad3.png', confidence=0.7, region=(416,32,455,210))
    elif pyautogui.locateOnScreen('adCloseBtn\\ad4.png', confidence=0.9, region=(416,32,455,210)) != None:
        location = pyautogui.locateOnScreen('adCloseBtn\\ad4.png', confidence=0.9, region=(416,32,455,210)) 
    elif pyautogui.locateOnScreen('adCloseBtn\\ad5.png', confidence=0.6, region=(416,32,455,210)) != None:
        location = pyautogui.locateOnScreen('adCloseBtn\\ad5.png', confidence=0.6, region=(416,32,455,210)) 
    elif pyautogui.locateOnScreen('adCloseBtn\\ad6.png', confidence=0.8, region=(416,32,455,210)) != None:
        location = pyautogui.locateOnScreen('adCloseBtn\\ad6.png', confidence=0.8, region=(416,32,455,210)) 
    elif pyautogui.locateOnScreen('adCloseBtn\\ad7.png', region=(116,32,755,210)) != None:
        location = pyautogui.locateOnScreen('adCloseBtn\\ad7.png', region=(116,32,755,210))
    elif pyautogui.locateOnScreen('adCloseBtn\\ad8.png', confidence=0.8, region=(416,32,455,210)) != None:
        location = pyautogui.locateOnScreen('adCloseBtn\\ad8.png', confidence=0.8, region=(416,32,455,210))
    elif pyautogui.locateOnScreen('adCloseBtn\\ad9.png', confidence=0.8, region=(416,32,455,210)) != None:
        location = pyautogui.locateOnScreen('adCloseBtn\\ad9.png', confidence=0.8, region=(416,32,455,210))
    elif pyautogui.locateOnScreen('adCloseBtn\\ad10.png', confidence=0.7, region=(416,32,455,210)) != None:
        location = pyautogui.locateOnScreen('adCloseBtn\\ad10.png', confidence=0.7, region=(416,32,455,210))
    elif pyautogui.locateOnScreen('adCloseBtn\\ad11.png', confidence=0.7, region=(416,32,455,210)) != None:
        location = pyautogui.locateOnScreen('adCloseBtn\\ad11.png', confidence=0.7, region=(416,32,455,210))
    elif pyautogui.locateOnScreen('adCloseBtn\\ad12.png', confidence=0.7, region=(416,32,455,210)) != None:
        location = pyautogui.locateOnScreen('adCloseBtn\\ad12.png', confidence=0.7, region=(416,32,455,210)) 
    elif pyautogui.locateOnScreen('adCloseBtn\\ad13.png', confidence=0.8, region=(416,32,455,210)) != None:
        location = pyautogui.locateOnScreen('adCloseBtn\\ad13.png', confidence=0.9, region=(416,32,455,210)) 
    elif pyautogui.locateOnScreen('adCloseBtn\\ad14.png', confidence=0.9, region=(416,32,455,210)) != None:
        location = pyautogui.locateOnScreen('adCloseBtn\\ad14.png', confidence=0.9, region=(416,32,455,210))
    else:
        location = None
    return location

def locate_exit_ad_screen2():
    path = 'C:\\Users\\SEVEN\\Desktop\\Tutorial\\adCloseBtn'
    files = os.listdir(path)
    for f in files:
        location = pyautogui.locateOnScreen('adCloseBtn\\'+str(f), confidence=0.8, region=(416,32,865,200))
        if location != None:
            return location


def locate_free_ink():
    location = pyautogui.locateOnScreen('freeinkbtn.png', confidence=0.8, region=(116,32,755,810))
    return location

def locate_gplay():
    location = pyautogui.locateOnScreen('gplayheader.PNG', confidence=0.8, region=(116,32,755,810))
    return location

def click_back():
    backbtn = pyautogui.locateOnScreen('backbtn.png', region=(670,520,200,350))
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


StuckCounter = 0
stuck_img_counter = 0
while keyboard.is_pressed('q') == False:
    try:
        #locate everything
        #location = locate_main_screen()
        #exitAdsScreen = locate_exit_ad_screen2()
        #exitClaimInk = locate_exit_claim_ink()
        #claimSpillInk = locate_spill_ink()
        #freeInkBtn = locate_free_ink()
        #googleplayscreen = locate_gplay()
        

        #write picture what it see
        #iml = pyautogui.screenshot(region=(116,32,755,810))
        #iml.save(r"C:\Users\SEVEN\Desktop\Tutorial\whatISee.png")

        #condition
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
            
        
        


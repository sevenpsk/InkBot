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

def locateMainScreen():
    location = pyautogui.locateOnScreen('vdoPromo.png',confidence=0.8, region=(116,32,755,810))
    return location

def locateExitClaimInk():
    location = pyautogui.locateOnScreen('okbtn.png', confidence=0.8, region=(116,32,755,810))
    return location

def locateSpillInk():
    location = pyautogui.locateOnScreen('spillink.png', confidence=0.9, region=(116,32,755,810))
    return location

def locateExitAdScreen():
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

def locateExitAdScreen2():
    path = 'C:\\Users\\SEVEN\\Desktop\\Tutorial\\adCloseBtn'
    files = os.listdir(path)
    for f in files:
        location = pyautogui.locateOnScreen('adCloseBtn\\'+str(f), confidence=0.8, region=(416,32,865,200))
        if location != None:
            return location


def locateFreeInk():
    location = pyautogui.locateOnScreen('freeinkbtn.png', confidence=0.8, region=(116,32,755,810))
    return location

def locateGPlay():
    location = pyautogui.locateOnScreen('gplayheader.PNG', confidence=0.8, region=(116,32,755,810))
    return location

def clickback():
    backbtn = pyautogui.locateOnScreen('backbtn.png', region=(670,520,200,350))
    if backbtn != None:
        click(backbtn.left+10,backbtn.top+10)
    else:
        keyboard.send('Esc')
    time.sleep(1.5)

def randomclickclose():
    click(764,56)

def captureStuck(filename):
    iml = pyautogui.screenshot(region=(116,32,755,810))
    iml.save(r"C:\\Users\\SEVEN\Desktop\\Tutorial\\StuckScreen\\"+str(filename)+".png")
    print(f'image no {stuck_img_counter} saved')


StuckCounter = 0
stuck_img_counter = 0
while keyboard.is_pressed('q') == False:
    try:
        #locate everything
        #location = locateMainScreen()
        #exitAdsScreen = locateExitAdScreen2()
        #exitClaimInk = locateExitClaimInk()
        #claimSpillInk = locateSpillInk()
        #freeInkBtn = locateFreeInk()
        #googleplayscreen = locateGPlay()
        

        #write picture what it see
        #iml = pyautogui.screenshot(region=(116,32,755,810))
        #iml.save(r"C:\Users\SEVEN\Desktop\Tutorial\whatISee.png")

        #condition
        if locateSpillInk() != None:
            claimSpillInk = locateSpillInk()
            print(f'I can see unclaim Ink at{claimSpillInk}')
            sleep(0.5)
            click(claimSpillInk.left+20,claimSpillInk.top+50)
            time.sleep(1)
            #locate back btn and click
            clickback()
            
        elif locateGPlay() != None:
            googleplayscreen = locateGPlay()
            print('I can see GooglePlay')
            time.sleep(0.5)
            clickback()
            time.sleep(1)
        
        elif locateExitClaimInk() != None:
            exitClaimInk = locateExitClaimInk()
            print(f'I can see "OK button" at {exitClaimInk}')
            time.sleep(0.5)
            click(exitClaimInk.left+30,exitClaimInk.top+10)
            time.sleep(1.5)
            if datetime.datetime.now().minute == 0 :
                clickback()
            
        elif locateMainScreen() != None:
            location = locateMainScreen()
            print(f'I can see "WatchVDO buttton" at {location}')
            time.sleep(0.5)
            click(location.left+80,location.top+50)
            time.sleep(5)
            StuckCounter = 0

        elif locateFreeInk() != None:
            freeInkBtn = locateFreeInk()
            print(f'I can see "Free ink button" at {freeInkBtn}')
            time.sleep(0.5)
            click(freeInkBtn.left+50,freeInkBtn.top+20)

        elif locateExitAdScreen2() != None:
            exitAdsScreen = locateExitAdScreen2()
            print(f'I can see "close button" at {exitAdsScreen}')
            time.sleep(1)
            click(exitAdsScreen.left+10,exitAdsScreen.top+10)
            time.sleep(3)
            StuckCounter=0
        
        elif datetime.datetime.now().minute == 1:
            clickback()
            print('clickback for refresh')

        elif pyautogui.locateOnScreen('hourlyMax.png', confidence=0.8, region=(116,32,755,810)) != None:
            print(f'hourly max! {StuckCounter}/15')
            sleep(5)
            StuckCounter+=1
            if StuckCounter > 15:
                print('too long try to refresh')
                clickback()
                StuckCounter = 0

        else:
            print(f'nope {StuckCounter}/20')
            StuckCounter+=1
            if(StuckCounter>20):
                stuck_img_counter += 1
                if stuck_img_counter < 20:
                    captureStuck(stuck_img_counter)
                clickback()
                randomclickclose()
                StuckCounter=0
    except:
        pass
            
        
        


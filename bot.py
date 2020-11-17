from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con    

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(1300, 590)[0] == 0:
        click(1300, 590)
    if pyautogui.pixel(1400, 590)[0] == 0:
        click(1400, 590)
    if pyautogui.pixel(1500, 590)[0] == 0:
        click(1500, 590)
    if pyautogui.pixel(1600, 590)[0] == 0:
        click(1600, 590)


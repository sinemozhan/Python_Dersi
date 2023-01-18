import pyautogui
import time

time.sleep(2)

def mesaj ():
    pyautogui.write("t")
    pyautogui.press('enter')

while True:
    mesaj()
    time.sleep(0)
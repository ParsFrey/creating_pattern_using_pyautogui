import pyautogui
import sys
import time
time.sleep(2)
a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
for i in a:
    if i == 1:
        pyautogui.click()

    for j in range(20):
        pyautogui.press("right")
    for j in range(20):
        pyautogui.press("up")
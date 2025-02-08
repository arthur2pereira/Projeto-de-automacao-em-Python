import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")

pyautogui.write("https://www.deepseek.com/")
pyautogui.press("enter")

pyautogui.click(x=523, y=743)

pyautogui.write("Oi, Deepseek")
pyautogui.press("enter")
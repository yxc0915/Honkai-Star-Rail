import time
import pyautogui
def teleport():
    # 自动传送
    pyautogui.keyDown('t')
    time.sleep(1)
    pyautogui.keyUp('t')
    time.sleep(1)
    pyautogui.typewrite('home')
    time.sleep(1)
    pyautogui.press('enter')

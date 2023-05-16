import time
import pyautogui
def fight():
    # 读取路径并自动寻路
    with open('path.txt', 'r') as f:
        path = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]for pos in path:
        pyautogui.moveTo(pos)
        time.sleep(0.1)
        pyautogui.click()# 自动打怪
        while True:
            if pyautogui.locateOnScreen('enemy.png', confidence=0.9) is not None:
                # 找到敌人，自动进入战斗
                pyautogui.click()
                time.sleep(1)
            else:
                # 没有敌人，自动寻路
                break

import time
import pyautogui
def fight():
    # 读取路径并自动寻路
    with open('path.txt', 'r') as f:
        path = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]for pos in path:
        pyautogui.moveTo(pos)
        time.sleep(0.1)
        if pyautogui.locateOnScreen('enemy1.png', confidence=0.9) is not None:
            # 找到敌人1，自动进入战斗
            fight_enemy1()
            time.sleep(1)
        elif pyautogui.locateOnScreen('enemy2.png', confidence=0.9) is not None:
            # 找到敌人2，自动进入战斗
            fight_enemy2()
            time.sleep(1)
        else:
            # 没有敌人，自动寻路
            breakdef fight_enemy1():
    # 自动打敌人1
    pyautogui.click()
    time.sleep(1)def fight_enemy2():
    # 自动打敌人2
    pyautogui.click()
    time.sleep(1)

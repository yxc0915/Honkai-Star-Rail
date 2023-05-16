import time
import pyautogui
def find_path():
    # 录制路径
    path = []
    while True:
        if pyautogui.locateOnScreen('enemy.png', confidence=0.9) is not None:
            # 找到敌人，自动进入战斗
            pyautogui.click()
            time.sleep(1)
        else:
            # 没有敌人，记录路径
            path.append(pyautogui.position())
            pyautogui.keyDown('w')
            time.sleep(1)
            pyautogui.keyUp('w')
            if len(path) >= 10:
                # 记录完毕，保存路径
                with open('path.txt', 'w') as f:
                    for pos in path:
                        f.write(f'{pos[0]},{pos[1]}\n')
                break

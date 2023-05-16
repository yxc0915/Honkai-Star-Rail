import time
import pyautogui
import pathfinding
import fighting
import teleporting# 获取屏幕分辨率
screen_width, screen_height = pyautogui.size()# 进入游戏
pyautogui.click(int(screen_width * 0.1), int(screen_height * 0.1))# 自动寻路
pathfinding.find_path()# 自动打怪
fighting.fight()# 自动传送
teleporting.teleport()

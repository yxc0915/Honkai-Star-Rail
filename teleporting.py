import time
import pyautoguidef teleport():
    # 按下M键打开地图
    pyautogui.press('m')
    time.sleep(1)
    # 自动识别地图中的传送点
    teleport_points = [{'name': 'point1', 'icon': 'point1.png'},
                       {'name': 'point2', 'icon': 'point2.png'},
                       {'name': 'point3', 'icon': 'point3.png'}]
    for point in teleport_points:
        # 查找所有传送点的位置
        point_locations = pyautogui.locateAllOnScreen(point['icon'])
        for point_location in point_locations:
            # 点击传送点
            pyautogui.click(point_location)
            time.sleep(1)
            # 在地图右下角的弹窗中点击传送
            teleport_location = pyautogui.locateOnScreen('teleport.png')
            if teleport_location is not None:
                pyautogui.click(teleport_location)
                break

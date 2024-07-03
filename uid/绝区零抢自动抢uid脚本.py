
import keyboard
import pyautogui
import cv2                              
import numpy                           
from PIL import ImageGrab               
import sys, time, ctypes                
from random import random               

img_templ = cv2.imread(r'C:\Users\26652\Desktop\uid\play_button.jpg' ) #自定义文件路径
THRESHOLD = 0.97


def mainLoop():
    img_src = ImageGrab.grab( bbox=(920, 917, 1244, 977) ) # x1, y1, x2, y2l 截图位置
    img_src = cv2.cvtColor(numpy.asarray(img_src), cv2.COLOR_RGB2BGR)
    time.sleep(0.3)
    result = cv2.matchTemplate(img_src, img_templ, cv2.TM_CCOEFF_NORMED)
    min_max = cv2.minMaxLoc(result)  
    print('result.min_max:', min_max)

    if min_max[1] > THRESHOLD :
        print('处于对话状态，模拟鼠标单击')
        pyautogui.click(1128,940,button="left")
        time.sleep(9 + 1* random())
        pyautogui.click(2000,940,button="left")

if __name__ == '__main__':
    if ctypes.windll.shell32.IsUserAnAdmin() :
        print('当前已是管理员权限')
        while True:
            mainLoop()
            time.sleep(0.2 +  0.1* random())
            if keyboard.is_pressed('l'):  #绑健结束循环
                print("检测到 'l' 键被按下，中断循环...")  
                break  # 跳出循环  

    else:
        print('当前不是管理员权限，以管理员权限启动新进程...')
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
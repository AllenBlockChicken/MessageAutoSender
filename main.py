import pyautogui
import random
import time


class Message(object):

    def __init__(self):
        self.txt = input("请输入刷屏文本（必须为英文）")
        self.time = int(input("请输入刷屏次数"))

    def execute(self):
        time.sleep(2)
        for i in range(self.time):
            pyautogui.typewrite(self.txt)
            pyautogui.press("enter")



sendMessage = Message()
sendMessage.execute()

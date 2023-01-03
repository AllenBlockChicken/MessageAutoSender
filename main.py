import pyautogui
import random
import time
import pygame
import sys

pygame.init()

mainScreen = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("Message Auto Sender")
background = pygame.image.load("./resources/background.png")
mainScreen.blit(background, (0, 0))


class Button(object):

    def __init__(self):
        pass

    def update(self, imagePath: str, PosX: int, PosY: int):
        image = pygame.image.load(imagePath)
        self.PosX = PosX
        self.PosY = PosY
        mainScreen.blit(image, (PosX, PosY))

    def onClick(self, mouseX: int, mouseY: int):
        if self.PosX <= mouseX <= self.PosX + 100 and self.PosY <= mouseY <= self.PosY + 50:
            return True

        else:
            return False


class Message(object):

    def __init__(self):
        self.txt = input("请输入刷屏文本（必须为英文）")
        self.time = int(input("请输入刷屏次数"))

    def execute(self):
        time.sleep(2)
        for i in range(self.time):
            pyautogui.typewrite(self.txt)
            pyautogui.press("enter")

message = Message()

button1 = Button()
button1.update(imagePath="./resources/buttons/button1.png", PosX=50, PosY=50)

while True:
    mainScreen.blit(background, (0, 0))
    button1.update(imagePath="./resources/buttons/button1.png", PosX=50, PosY=50)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(())

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            if button1.onClick(mouseX=mouseX, mouseY=mouseY) == True:
                message.execute()

            else:
                print("sorry man")

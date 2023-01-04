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


class InputBox:
    def __init__(self, rect: pygame.Rect = pygame.Rect(100, 100, 140, 32)) -> None:
        """
        rect，传入矩形实体，传达输入框的位置和大小
        """
        self.boxBody: pygame.Rect = rect
        self.color_inactive = pygame.Color('lightskyblue3')  # 未被选中的颜色
        self.color_active = pygame.Color('dodgerblue2')  # 被选中的颜色
        self.color = self.color_inactive  # 当前颜色，初始为未激活颜色
        self.active = False
        self.text = ''
        self.done = False
        self.font = pygame.font.Font(None, 32)

    def dealEvent(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.boxBody.collidepoint(event.pos):  # 若按下鼠标且位置在文本框
                self.active = not self.active
            else:
                self.active = False
            if self.active:
                self.color = self.color_active
            else:
                self.color = self.color_inactive

        if event.type == pygame.KEYDOWN:  # 键盘输入响应
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    return str(self.text)
                    # self.text=''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen: pygame.surface.Surface):
        txtSurface = self.font.render(
            self.text, True, self.color)  # 文字转换为图片
        width = max(200, txtSurface.get_width() + 10)  # 当文字过长时，延长文本框
        self.boxBody.w = width
        screen.blit(txtSurface, (self.boxBody.x + 5, self.boxBody.y + 5))
        pygame.draw.rect(screen, self.color, self.boxBody)


class Message(object):

    def __init__(self, txt, times):
        self.txt = txt
        self.time = times

    def execute(self):
        time.sleep(2)
        for i in range(self.times):
            pyautogui.typewrite(self.txt)
            pyautogui.press("enter")


textInputBox = InputBox(pygame.Rect(50, 20, 140, 32))
timesInputBox = InputBox(pygame.Rect(50, 60, 140, 72))
buttonBegin = Button()

while True:
    mainScreen.blit(background, (0, 0))
    buttonBegin.update(imagePath="./resources/buttons/buttonBegin.png", PosX=200, PosY=50)
    pygame.display.update()
    textInputBox.draw(mainScreen)
    timesInputBox.draw(mainScreen)

    for event in pygame.event.get():
        textInputBox.dealEvent(event)
        timesInputBox.dealEvent(event)
        if event.type == pygame.QUIT:
            sys.exit(())

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            if buttonBegin.onClick(mouseX=mouseX, mouseY=mouseY) == True:
                message = Message(textInputBox.text, timesInputBox.text)
                message.execute()

            else:
                print("sorry man")


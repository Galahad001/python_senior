import time
from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *


class DinoBot:
 def __init__(self, replaybtn):
    self.replaybtn = replaybtn
 def restartgame(self):
    pyautogui.click(self.replaybtn)

 def jump(self):
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')

 def grabimage(self):
        box = (198, 332, 224, 367)
        image = ImageGrab.grab(box)
        grayImage = ImageOps.grayscale(image)
        a = array(grayImage.getcolors())
        return a.sum()

 def start(self):
    self.restartgame()

def main():
 bot = DinoBot((333, 449))
 bot.start()
 while True:
        print(str(bot.grabimage()))




main()

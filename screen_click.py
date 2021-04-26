import pyautogui
import time
import random
import os

logos = 'C:/Users/bruce/Documents/GitHub/screen_click_on_event/channelLogos'
points = 'C:/Users/bruce/Documents/GitHub/screen_click_on_event/channelPoints'
start = time.time()
collectionOfChannels = []


class TwitchChannel:
    def __init__(self, name, channelPoints=0):
        self.channelPoints = channelPoints
        self.name = name

    def addPoints(self):
        self.channelPoints += 50


def channelLogoLookUp(screen):
    for filename in os.listdir(logos):
        if filename.endswith(".PNG"):
            channel = pyautogui.locateOnScreen(filename)
        if channel != None:
            print("Channel found", filename)


while True:
    for filename in os.listdir(points):
        if filename.endswith(".PNG"):
            location = pyautogui.locateOnScreen(filename)
            print(location)
            if location != None:
                break
            continue
        else:
            # look at what channel is being watched
            # check array of channel obj for current channel
            # if channel obj isn't made make obj
            continue
    if location != None:
        randomTime = random.randrange(1, 5, 1)
        print('i am waiting', randomTime)
        mouseLocation = pyautogui.position()
        time.sleep(randomTime)
        pyautogui.click(location)
        pyautogui.moveTo(mouseLocation)
        end = time.time()
        print((end - start)/60)
        start = time.time()

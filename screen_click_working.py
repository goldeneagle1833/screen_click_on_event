import pyautogui
import time
import random
import os
# from tkinter import *

# root = Tk()
# myLabel = Label(root, text="hello world")
# myLabel.pack()
# root.mainloop()
logos = 'C:/Users/bruce/Documents/GitHub/screen_click_on_event/channelLagos'
directory = 'C:/Users/bruce/Documents/GitHub/screen_click_on_event'
start = time.time()
collectionOfChannels = []


class TwitchChannel:
    def __init__(self, name, channelPoints):
        self.channelPoints = channelPoints
        self.name = name

    def addPoints(self):
        self.channelPoints += 50

    def clickOnPoints(self, location):
        mouseLocation = pyautogui.position()
        pyautogui.click(location)
        pyautogui.moveTo(mouseLocation)

    # need a method to create and store object data for restarting program


def pointsButtonCheck():
    for filename in os.listdir(directory):
        if "PointBox" in filename:
            print(filename)
            location = pyautogui.locateOnScreen(filename)
            if location != None:
                return location


def channelLogoLookUp():
    for filename in os.listdir(directory):
        if "Logo" in filename:
            channel = pyautogui.locateOnScreen(filename)
        else:
            channel = None
        if channel != None:
            print("Channel found", filename)
            return filename.replace('Logo.PNG', "")


def createChannelObj(name):
    if any(x.name == name for x in collectionOfChannels):
        print(f'{x.name} already created')
    else:
        name = TwitchChannel(name, 0)
        collectionOfChannels.append(name)
        print(f'{name.name} created', collectionOfChannels)


def clickPoints(location):
    mouseLocation = pyautogui.position()
    pyautogui.click(location)
    pyautogui.moveTo(mouseLocation)


def resultsLog():
    results = open("Results.txt", "a+")
    for x in collectionOfChannels:
        results.write(f"\n{str(x.channelPoints)} {x.name}")
    results.write("\n ---------------")


while True:
    location = pointsButtonCheck()
    if location != None:
        nameOfChannel = channelLogoLookUp()
        createChannelObj(nameOfChannel)
        for x in collectionOfChannels:
            if x.name == nameOfChannel:
                x.addPoints()
                print(x.channelPoints)
                print(x.name)
        randomTime = random.randrange(1, 10, 1)
        print('i am waiting', randomTime)
        time.sleep(randomTime)
        clickPoints(location)
        resultsLog()
    else:
        print('None')

import pyautogui
import time
import random
import os
from tkinter import *


from logicForEvents import logic

root = Tk()

# buttons
infoButton = Button(root, text="Show current Points Count",
                    command=logic.showCurrentPoints)
infoButton.pack()

mainLoopButton = Button(
    root, text="Start watching twitch", command=logic.startWatching)
mainLoopButton.pack()

stopWatching = Button(root, text="Stop watching Twitch",
                      command=logic.stopWatching)
stopWatching.pack()

if __name__ == "__main__":
    root.mainloop()

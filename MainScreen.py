## This is the main screen for the final project
## top left corner will be "Play"
## top right corner will be "Train"
## bottom left corner will be "Sleep"
## bottom right corner will be "Feed"
from graphics import *
from button import Button
from PIL import Image as pilImage
from time import *


class PetMain:
    def __init__(self):
        win = self.win = GraphWin("Let's Play!", 600, 600)
        win.setCoords(0,0,2,3)

        ## adding buttons
        play = Button(win, Point(0.5, 0.75), 0.6, 0.4, "Play Fetch!")
        train = Button(win, Point(0.5, 0.3), 0.6, 0.4, "Training")
        sleep = Button(win, Point(1.5, 0.75), 0.6, 0.4, "Nap Time")
        feed = Button(win, Point(1.5, 0.3), 0.6, 0.4, "Feed Me!")
        exit = Button(win, Point(1.75, 2.5), 0.2, 0.2, "EXIT")

    def choose(self, choices):
        buttons = self.buttons

        ## activating the choices for play/train/sleep/eat
        for b in buttons:
            if b.getlabel() in choices:
                b.activate()
            else:
                b.deactivate()

        ## getting the mouse clicks on active buttons
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()

    def close(self):
        self.win.close()

def main():
    petMain = PetMain()
    petMain.win.getMouse()
    petMain.close()

main()

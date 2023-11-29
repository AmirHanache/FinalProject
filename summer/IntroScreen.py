import sys
sys.path.insert(0, '..')
from graphics import *
from button import Button



class MainScreen:
    def __init__(self):
        win = GraphWin('Moving Scene', 600, 600, autoflush=False)
        im = Image(Point(300, 300), 'Summer_0.gif')
        i = 0
        while True:
            im.undraw()
            i = i % 1011
            im = Image(Point(300, 300), 'Summer_{}.gif'.format(i))
            im.draw(win)
            banner = Text(Point(300, 100), 'Welcome to our game!')
            banner.setSize(26)
            banner.draw(win)

            rules = Text(Point(275, 200), 'Rules: 1. Load an existing pet or create a new one.\n 2. The goal is to take care of your pet and level it up.\n 3. There are mini games at each corner to level up.\n 4. Make sure you feed your pet.\n 5. Make sure your pet gets enough sleep.')
            rules.setSize(15)
            rules.draw(win)
            #Add buttons
            create = Button(win, Point(150, 475), 130, 50, "Create New Pet!")
            play = Button(win, Point(150 , 535), 130, 50, "Practice Play!")
            load = Button(win, Point(450, 475), 130, 50, "Load your Pet!")
            exit = Button(win, Point(450 , 535), 130, 50, "Exit the Game :(")
            self.buttons = [play, exit]
            update(20)
            update(10)
            i += 1
            key = win.checkKey()
            if key:
                break

    def choose(self, choices):
        buttons = self.buttons

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel() # function exit here.

    def wantToPlay(self):
        ans = self.choose(["Practice Play!", "Exit the Game :("])
        return ans == "Practice Play!"


    def close(self):
        self.win.close()




def main():
    mainScreen = MainScreen()
    mainScreen.win.getMouse()  # Wait for a mouse click before closing
    mainScreen.close()         # Close the window after the click

main()

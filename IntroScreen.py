from graphics import *
from button import Button
from PIL import Image as PILImage



class MainScreen:
    def __init__(self):
        win = self.win = GraphWin("GigaPet", 600, 600)
        win.setCoords(0,0,2,3)


        # Load the image using Pillow
        pilImage = PILImage.open("summer2.gif")
        pilImage = pilImage.resize((600, 600))  # Specify the new dimensions

        # Save the resized image temporarily
        pilImage.save("resized_image.gif")

        # Now load the resized image in your graphics.py window
        myImage = Image(Point(1, 1.5), "resized_image.gif")
        myImage.draw(self.win)


        #Add a banner
        banner = Text(Point(1, 2.8), 'Welcome to our game!')
        banner.setSize(26)
        banner.draw(win)

        rules = Text(Point(1, 1.75), 'Rules: 1. Load an existing pet or create a new one.\n 2. The goal is to take care of your pet and level it up.\n 3. There are mini games at each corner to level up.\n 4. Make sure you feed your pet.\n 5. Make sure your pet gets enough sleep.')
        rules.setSize(15)
        rules.draw(win)
        #Add buttons
        create = Button(win, Point(0.5, 0.75), 0.6, 0.4, "Create New Pet!")
        play = Button(win, Point(0.5 , 0.3), 0.6, 0.4, "Practice Play!")
        load = Button(win, Point(1.5, 0.75), 0.6, 0.4, "Load your Pet!")
        exit = Button(win, Point(1.5 , 0.3), 0.6, 0.4, "Exit")
        self.buttons = [play, exit]

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
        ans = self.choose(["Lets Play!", "Exit"])
        return ans == "Lets Play!"


    def close(self):
        self.win.close()




def main():
    mainScreen = MainScreen()
    mainScreen.win.getMouse()  # Wait for a mouse click before closing
    mainScreen.close()         # Close the window after the click

main()

import sys
import os
sys.path.insert(0, '..')
from graphics import *
from button import Button
from tkinter import simpledialog
from tkinter import messagebox




class MainScreen:
    def __init__(self):
        win =self.win = GraphWin('Moving Scene', 600, 600, autoflush=False)
        self.user_choice = None
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

            rules = Text(Point(275, 200), 'Rules: 1. Load an existing pet or create a new one.\n 2. The goal is to take care of your pet and level it up.\n 3. There are mini games at each corner to level up.\n 4. Make sure you feed your pet.\n 5. Make sure your pet gets enough sleep. \n 6. Use WASD to move your character around!')
            rules.setSize(15)
            rules.draw(win)
            #Add buttons
            create = Button(win, Point(150, 475), 130, 50, "Create New Pet!")
            play = Button(win, Point(150 , 535), 130, 50, "Practice Play!")
            load = Button(win, Point(450, 475), 130, 50, "Load your Pet!")
            exit = Button(win, Point(450 , 535), 130, 50, "Exit the Game :(")
            self.buttons = [create, play, load, exit]
            # Check for button clicks or key presses
            update(20)
            update(10)
            i += 1
            self.user_choice = self.choose()
            if self.user_choice:
                break

    def choose(self):
        p = self.win.checkMouse()  # Check for mouse click
        if p:
            for b in self.buttons:
                if b.clicked(p):
                    self.user_choice = b.getLabel()
                    return b.getLabel()
        return None

    def create_pet(self):
        pet_name = simpledialog.askstring("Pet Name", "What do you want to name your pet?")
        if pet_name:
            with open('pet_names.txt', 'a') as file:
                file.write(pet_name + '\n')
            self.pet_name = pet_name  # Update the pet's name attribute

    def load_pet(self):
        pet_name = simpledialog.askstring("Load Pet", "Enter your pet's name:")
        if pet_name:
            with open('pet_names.txt', 'r') as file:
                if pet_name in file.read().splitlines():
                    # Code to handle the loading of the pet
                    self.pet_name = pet_name  # Update the pet's name attribute
                else:
                    messagebox.showinfo("No Pet Found", "No such pet found")


    def close(self):
        self.win.close()

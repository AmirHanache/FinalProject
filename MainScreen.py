from IntroScreen import MainScreen
from graphics import *
from button import Button
from PIL import Image as PILImage
import time
import foodgame


class PetMain:
    def __init__(self, pet_name = "Shmoney"):
        win = self.win = GraphWin("Let's Play!", 600, 600)
        self.last_update_time = time.time()  # Correct usage of time.time()

        # Set the background image
        # Load the image using Pillow
        #pilImage = PILImage.open("Dog_Park_Background.png")
        #pilImage = pilImage.resize((600, 600))  # Specify the new dimensions

        # Save the resized image temporarily
        #pilImage.save("DogResize.png")

        # Now load the resized image in your graphics.py window
        myImage = Image(Point(300, 300), "DogResize.png")
        myImage.draw(self.win)

        #dog_pil_image = PILImage.open("Dog.png")
        # Resize the dog image (adjust dimensions as needed)
        #dog_pil_image = dog_pil_image.resize((75, 75))  # Example dimensions
        #dog_pil_image.save("DogResized.png")

        # Now load the resized dog image
        self.doggy = Image(Point(300, 300), "DogResized.png")
        self.doggy.draw(self.win)

        # Initialize dog's name
        self.dog_name = pet_name  # Example name, you can set it differently
        self.dog_name_text = Text(Point(300, 250), self.dog_name)  # Position above the dog
        self.dog_name_text.setSize(12)  # Font size
        self.dog_name_text.setStyle('bold')
        self.dog_name_text.setTextColor('black')  # Text color
        self.dog_name_text.draw(self.win)


        ## adding buttons
        self.play = Button(win, Point(500, 475), 85, 30, "Play Fetch!")
        self.train = Button(win, Point(150, 50), 75, 30, "Training")
        self.sleep = Button(win, Point(525, 50), 85, 30, "Nap Time")
        self.feed = Button(win, Point(150, 475), 85, 30, "Feed Me!")

        #These are the dogs health and sleep bars
        self.health_boxes = []
        self.sleep_boxes = []
        self.init_status_bars()

        #Initializing the count for health and sleep
        self.health_score = 5
        self.sleep_score = 5

    def init_status_bars(self):
        # Create and position the 'Health' label
        health_label = Text(Point(30, 5), "Health")  # Adjust position as needed
        health_label.setSize(10)  # Set font size
        health_label.setStyle('bold')  # Set text style to bold
        health_label.draw(self.win)

        # Create and position the 'Sleep' label
        sleep_label = Text(Point(30, 35), "Sleep")  # Adjust position as needed
        sleep_label.setSize(10)  # Set font size
        sleep_label.setStyle('bold')  # Set text style to bold
        sleep_label.draw(self.win)
        for i in range(5):  # Assuming 5 boxes for each bar
            # Create health boxes
            health_box = Rectangle(Point(1 + i*20, 10), Point(3 + i*20, 30))  # Adjust positions as needed
            health_box.setFill('green')
            health_box.draw(self.win)
            self.health_boxes.append(health_box)

            # Create sleep boxes
            sleep_box = Rectangle(Point(10 + i*20, 40), Point(30 + i*20, 60))  # Adjust positions as needed
            sleep_box.setFill('blue')
            sleep_box.draw(self.win)
            self.sleep_boxes.append(sleep_box)

    def is_near_button(self, dog, button):
        dog_center = dog.getAnchor()

        # Calculate the center of the button
        button_center_x = (button.xmin + button.xmax) / 2
        button_center_y = (button.ymin + button.ymax) / 2
        button_center = Point(button_center_x, button_center_y)

        distance = ((dog_center.getX() - button_center.getX())  +
                    (dog_center.getY() - button_center.getY()) )
        return distance < 50  # Adjust the distance threshold as needed

    def reset_dog_position(self):
        # Directly move the dog to the center
        self.doggy.move(Point(300,300))
        self.dog_name_text.move(Point(300, 250))

    def run(self):
        while True:
            key = self.win.checkKey()
            if key in ["w", "a", "s", "d"]:
                self.move_doggy_based_on_key(key)  # Correct indentation

            current_time = time.time()
            if current_time - self.last_update_time >= 5:  # 20 seconds interval
                self.update_bars()
                self.last_update_time = current_time  # Reset the last update time

            if key == "q":
                break

            if self.is_near_button(self.doggy, self.feed):
                 foodgame.start_food_game() # Example for the play button
                 self.win.focus()
                 self.reset_dog_position()
            elif self.is_near_button(self.doggy, self.train):
                print("Starting Train Mini-Game")
            elif self.is_near_button(self.doggy, self.sleep):
                print("Starting Sleep Mini-Game")
            elif self.is_near_button(self.doggy, self.feed):
                print("Starting Feed Mini-Game")




    def move_doggy_based_on_key(self, key):
        if key == "w":
            self.move_doggy(0, -10)  # Move up
        elif key == "s":
            self.move_doggy(0, 10)   # Move down
        elif key == "a":
            self.move_doggy(-10, 0)  # Move left
        elif key == "d":
            self.move_doggy(10, 0)   # Move right


    def move_doggy(self, dx, dy):
        self.doggy.move(dx, dy)
        # Move the dog's name text
        self.dog_name_text.move(dx, dy)

    def update_bars(self):
        # Decrement the health and sleep scores
        self.health_score = max(0, self.health_score - 1)
        self.sleep_score = max(0, self.sleep_score - 1)

        self.update_health(int(self.health_score))
        self.update_sleep(int(self.sleep_score))

        if self.health_score <= 1:
            self.dog_name_text.setTextColor('red')

    def update_health(self, health_score):
        for i in range(5):
            if i < self.health_score:
                self.health_boxes[i].setFill('green')
            else:
                self.health_boxes[i].setFill('gray')
            self.health_boxes[i].undraw()  # Redraw the box for the update to take effect
            self.health_boxes[i].draw(self.win)

    def update_sleep(self, sleep_score):
        for i in range(5):
            if i < sleep_score:
                self.sleep_boxes[i].setFill('blue')
            else:
                self.sleep_boxes[i].setFill('gray')
            self.sleep_boxes[i].undraw()  # Redraw the box for the update to take effect
            self.sleep_boxes[i].draw(self.win)


    def OpenNewWindow(self):
        click = self.win.getMouse()
        if click == 

    def close(self):
        self.win.close()


#def main():
#    petMain = PetMain()
#    petMain.run()
#    petMain.win.getMouse()
#    petMain.close()

#main()

def main():
    intro = MainScreen()
    user_choice = intro.user_choice

    if user_choice == "Create New Pet!":
        intro.create_pet()
    elif user_choice == "Load your Pet!":
        intro.load_pet()

    pet_name = getattr(intro, 'pet_name', "Shmoney")  # Use the created/loaded name or default
    intro.close()  # Close the intro screen

    if user_choice in ["Practice Play!", "Create New Pet!", "Load your Pet!"]:
        petMain = PetMain(pet_name)  # Pass the pet name to PetMain
        petMain.run()
        petMain.win.getMouse()
        petMain.close()

main()

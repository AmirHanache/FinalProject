from IntroScreen import MainScreen
from graphics import *
from button import Button
import time
import foodgame
import sheepgame
import matching
import pettinggame


class PetMain:
    def __init__(self, pet_name = "Shmoney", level = 1):
        self.pet_name = pet_name
        self.dog_level = level
        #Initializing the count for health and sleep
        self.health_score = 5
        self.sleep_score = 5
        self.mini_games_completed = 0
        self.initialize_window()

    def initialize_window(self):
        win = self.win = GraphWin("Let's Play!", 600, 600)
        self.last_update_time = time.time()  # Correct usage of time.time()

        # Now load the resized image in your graphics.py window
        myImage = Image(Point(300, 300), "DogResize.png")
        myImage.draw(self.win)

        # Now load the resized dog image
        self.doggy = Image(Point(300, 300), "DogResized.png")
        self.doggy.draw(self.win)

        # Initialize dog's name
        #self.dog_name = pet_name  # Example name, you can set it differently
        self.dog_name_text = Text(Point(300, 250), self.pet_name)  # Position above the dog
        self.dog_name_text.setSize(12)  # Font size
        self.dog_name_text.setStyle('bold')
        self.dog_name_text.setTextColor('black')  # Text color
        self.dog_name_text.draw(self.win)

        # Initialize dogs level
        self.dog_level_text = Text(Point(300, 335), f"Level: {self.dog_level}")  # Position below the dog
        self.dog_level_text.setSize(12)
        self.dog_level_text.setStyle('bold')
        self.dog_level_text.setTextColor('black')
        self.dog_level_text.draw(self.win)

        ## adding buttons
        self.play = Button(win, Point(500, 475), 85, 30, "Play!")
        self.train = Button(win, Point(150, 50), 75, 30, "Training")
        self.sleep = Button(win, Point(525, 50), 85, 30, "Nap Time")
        self.feed = Button(win, Point(150, 475), 85, 30, "Feed Me!")

        #These are the dogs health and sleep bars
        self.health_boxes = []
        self.sleep_boxes = []
        self.init_status_bars()

    def reinitialize_window(self):
        self.win.close()  # Close the current window
        self.initialize_window()  # Reinitialize the window

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
            health_box = Rectangle(Point(10 + i*20, 10), Point(30 + i*20, 30))  # Adjust positions as needed
            health_box.setFill('green' if i < self.health_score else 'gray')
            health_box.draw(self.win)
            self.health_boxes.append(health_box)

            # Create sleep boxes
            sleep_box = Rectangle(Point(10 + i*20, 40), Point(30 + i*20, 60))  # Adjust positions as needed
            sleep_box.setFill('blue' if i < self.sleep_score else 'gray')
            sleep_box.draw(self.win)
            self.sleep_boxes.append(sleep_box)

    def is_near_button(self, dog, button):
        dog_center = dog.getAnchor()

        # Calculate the center of the button
        button_center_x = (button.xmin + button.xmax) / 2
        button_center_y = (button.ymin + button.ymax) / 2
        button_center = Point(button_center_x, button_center_y)

        distance = ((dog_center.getX() - button_center.getX()) ** 2  +
                    (dog_center.getY() - button_center.getY()) ** 2 )
        return distance < 50  # Adjust the distance threshold as needed

    def run(self):
        while True:
            key = self.win.checkKey()
            if key in ["w", "a", "s", "d"]:
                self.move_doggy_based_on_key(key)  # Correct indentation

            current_time = time.time()
            if current_time - self.last_update_time >= 20:  # 20 seconds interval
                self.update_bars()
                self.last_update_time = current_time  # Reset the last update time

            if key == "q":
                self.save_pet()
                break

            self.level_up()
            # Only trigger the mini-game if the cooldown has elapsed
            if self.is_near_button(self.doggy, self.feed):
                food_game_score = foodgame.start_food_game()  # Pass the main game window to the mini-game
                self.mini_games_completed += 1  # Increment the mini-game completion counter
                self.health_score = food_game_score
                self.update_health(self.health_score)
                self.reinitialize_window()
            elif self.is_near_button(self.doggy, self.train):
                matching.train_game()
                self.mini_games_completed += 1  # Increment the mini-game completion counter
                self.reinitialize_window()
            elif self.is_near_button(self.doggy, self.sleep):
                guessed_count, actual_count = sheepgame.sheep_game()
                # Map the score from 20-40 to 0-5
                difference = abs(guessed_count - actual_count)
                mapped_sleep_score = max(0, 5 - difference)

                self.sleep_score = mapped_sleep_score
                self.update_sleep(self.sleep_score)
                self.mini_games_completed += 1  # Increment the mini-game completion counter
                self.reinitialize_window()
            elif self.is_near_button(self.doggy, self.play):
                pettinggame.petting()
                self.mini_games_completed += 1  # Increment the mini-game completion counter
                self.reinitialize_window()
        self.close()

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
        self.dog_name_text.move(dx, dy)
        self.dog_level_text.move(dx, dy)

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

    def level_up(self):
        if self.mini_games_completed >= 2:
            self.dog_level += 1
            self.dog_level_text.setText(f"Level: {self.dog_level}")  # Update the level display
            self.mini_games_completed = 0  # Reset the counter
            self.save_pet()  # Save the pet's data after leveling up


    def save_pet(self):
        # Check if the current pet is using the default name and level
        if self.pet_name == "Shmoney":
            return  # Do not save if it's the default pet
        # Update this method to overwrite existing data
        pet_data = {}
        try:
            # Read existing data
            with open('pet_names.txt', 'r') as file:
                for line in file:
                    name, level = line.strip().split(',')
                    pet_data[name] = int(level)

            # Update the current pet's level
            pet_data[self.pet_name] = self.dog_level

            # Write all data back to the file
            with open('pet_names.txt', 'w') as file:
                for name, level in pet_data.items():
                    file.write(f"{name},{level}\n")
        except FileNotFoundError:
            # Create the file if it doesn't exist
            with open('pet_names.txt', 'w') as file:
                file.write(f"{self.pet_name},{self.dog_level}\n")

    def close(self):
        self.win.close()


def main():
    intro = MainScreen()
    user_choice = intro.user_choice

    if user_choice == "Create New Pet!":
        intro.create_pet()
        pet_name = getattr(intro, 'pet_name', "Shmoney")
        petMain = PetMain(pet_name)  # Create a new pet with default level
    elif user_choice == "Load your Pet!":
        pet_name, pet_level = intro.load_pet()
        if pet_name:
            petMain = PetMain(pet_name, pet_level)  # Create a pet with loaded name and level
        else:
            return  # Exit if no pet was loaded
    elif user_choice == "Practice Play!":
        petMain = PetMain("Shmoney", 1)

    intro.close()  # Close the intro screen

    if petMain:
        petMain.run()
        petMain.close()

main()

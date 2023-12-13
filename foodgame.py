from graphics import *
import time
import random

def initialize_game():
    # Initialize the game window
    win = GraphWin("Memory Game", 600, 573)

    # Set the background image
    background_image = Image(Point(300, 300), "bowl.png")
    background_image.draw(win)

    return win

def display_images(win, images, duration):
    # Display a set of images for a specified duration
    for image in images:
        image.draw(win)

    win.update()
    time.sleep(duration)

    # Undraw the displayed images
    for image in images:
        image.undraw()

def check_user_clicks(win, all_images, selected_images):
    correct_count = 0

    # Display all images before the user starts clicking
    for image in all_images:
        image.draw(win)

    win.update()
    time.sleep(0.5)  # Pause before user starts clicking

    # Check user clicks for 5 rounds
    for _ in range(5):
        click_point = win.getMouse()

        # Check if the click is within the bounds of any image
        for image in all_images:
            x_min, y_min, x_max, y_max = image.getAnchor().getX() - 25, image.getAnchor().getY() - 10, image.getAnchor().getX() + 25, image.getAnchor().getY() + 10
            if x_min <= click_point.getX() <= x_max and y_min <= click_point.getY() <= y_max:
                if image in selected_images:
                    correct_count += 1
                    image.undraw()  # Optionally remove correct guesses immediately
                    break
                else:
                    # Optionally display feedback for incorrect clicks
                    feedback_text = Text(Point(300, 300), "Incorrect!")
                    feedback_text.draw(win)
                    time.sleep(0.5)
                    feedback_text.undraw()

    return correct_count

def display_score(win, score):
    # Display the user's score
    score_text = Text(Point(300, 300), f"Score: {score}/5")
    score_text.draw(win)

def start_food_game():
    # Main function to orchestrate the game
    win = initialize_game()

    # List of all possible images
    all_images = [Image(Point(100, 150), "apple.png"), Image(Point(225, 150), "mango.png"),
                  Image(Point(350, 150), "strawberry.png"), Image(Point(475, 150), "watermelon.png"),
                  Image(Point(100, 250), "steak.png"), Image(Point(225, 250), "egg.png"),
                  Image(Point(350, 250), "salmon.png"), Image(Point(475, 250), "kibble.png")]

    # Randomly select 5 images for the user to memorize
    selected_images = random.sample(all_images, 5)

    # Display the selected images for a short duration
    display_images(win, selected_images, 0.125)
    time.sleep(0.5)

    # Check user clicks and determine the score
    score = check_user_clicks(win, all_images, selected_images)

    # Display the user's score
    display_score(win, score)

    # Wait for the user to click before closing the window
    win.getMouse()
    win.close()

    return score 

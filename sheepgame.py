from graphics import *
import random
import time

def create_window():
    win = GraphWin("Sheep Counting Game", 600, 574)
    background_image = Image(Point(300, 287), "sleepingbackground.png")
    background_image.draw(win)
    return win

def display_instructions(win):
    instructions = Text(Point(300, 20), "Count the Sheep in 30 seconds!")
    instructions.setTextColor("white")
    instructions.setSize(16)
    instructions.draw(win)

def create_entry_box(win):
    entry_box = Entry(Point(300, 450), 5)
    entry_box.setTextColor("white")
    entry_box.draw(win)
    return entry_box

def create_submit_button(win):
    submit_button = Rectangle(Point(260, 480), Point(340, 500))
    submit_button.setFill("lightblue")
    submit_button.draw(win)
    submit_label = Text(Point(300, 490), "Submit")
    submit_label.setTextColor("black")
    submit_label.setSize(16)
    submit_label.draw(win)

def generate_sheep(win, sheep_list):
    sheep_count = 0
    while sheep_count < 30:
        if random.random() < 0.05:
            x = random.randint(50, 550)
            y = random.randint(70, 500)
            sheep = Image(Point(x, y), "sheep.png")
            sheep.draw(win)
            sheep_list.append(sheep)
            sheep_count += 1
            time.sleep(random.uniform(0.125, 1))
            time.sleep(0.125)
            sheep.undraw()

def wait_for_input(win, entry_box):
    while True:
        click_point = win.getMouse()
        if 260 <= click_point.getX() <= 340 and 480 <= click_point.getY() <= 500:
            try:
                user_count = int(entry_box.getText())
                break
            except ValueError:
                pass

    return user_count

def display_results(win, user_count, sheep_list):
    correct_count = len(sheep_list)
    result_text = Text(Point(300, 300), "Your Score: {}".format(user_count))
    result_text.setTextColor("white")
    result_text.setSize(20)
    result_text.draw(win)

    correct_text = Text(Point(300, 330), "Correct Count: {}".format(correct_count))
    correct_text.setTextColor("white")
    correct_text.setSize(20)
    correct_text.draw(win)

    if user_count == correct_count:
        result = "Congratulations, you won the mini game"
    else:
        result = "You missed the count!"
    result_message = Text(Point(300, 360), result)
    result_message.setTextColor("white")
    result_message.setSize(20)
    result_message.draw(win)

    # Save the score to a file
    with open("sheepscore.txt", "a") as file:
        file.write(f"Score: {user_count}/{correct_count}\n")

    win.getMouse()
    win.close()

def sheep_game():
    win = create_window()
    display_instructions(win)

    entry_box = create_entry_box(win)
    create_submit_button(win)

    sheep_list = []
    generate_sheep(win, sheep_list)

    entry_box.setText("")  # Clear the text entry box
    user_count = wait_for_input(win, entry_box)

    display_results(win, user_count, sheep_list)

if __name__ == "__main__":
    sheep_game()

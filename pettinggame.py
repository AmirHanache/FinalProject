from graphics import GraphWin, Text, Point, Entry, Image
import time

# Global variables
count = 0
petgrade = 0  # Initialize petgrade

def petting():
    global count, petgrade
    count = 0
    petgrade = 0

    # Set up the window
    win = GraphWin("Click Speed Game", 400, 400)
    win.setBackground("white")

    # Set the background image
    background_image = Image(Point(200, 200), "pettingdog.png")
    background_image.draw(win)

    # Display introduction message
    intro_text = Text(Point(200, 50), "Click space to pet the dog, how many times can you pet the dog?")
    intro_text.draw(win)
    win.getKey()  # Wait for a key press before continuing
    intro_text.undraw()

    # Displays the ready set go
    ready_text = Text(Point(200, 50), "Ready...")
    ready_text.draw(win)
    time.sleep(1)

    ready_text.setText("Set...")
    time.sleep(1)

    ready_text.setText("Go!")
    time.sleep(1)
    ready_text.undraw()

    # Display the entry box for user input
    entry = Entry(Point(200, 350), 10)
    entry.draw(win)
    entry.setText("Click here and press space")

    # Record the start time
    start_time = time.time()

    # Allow 10 seconds for clicking
    while time.time() - start_time < 10:
        key = win.checkKey()
        if key == "space":
            update_count(entry)

    # Calculate and display the clicking speed
    entry.undraw()
    clicks_per_second = count / 10
    petgrade = calculate_grade(clicks_per_second)
    count_text = Text(Point(200, 350), f"Your clicking speed: {clicks_per_second} clicks per second\nGrade: {petgrade}")
    count_text.draw(win)

    win.getMouse()  # Wait for a key press before closing the window
    win.close()

def update_count(entry):
    global count
    count += 1
    entry.setText(f"Pets: {count}")

def calculate_grade(clicks_per_second):
    if 0 <= clicks_per_second <= 3:
        return 1
    elif 3.1 <= clicks_per_second <= 4:
        return 2
    elif 4.1 <= clicks_per_second <= 5.5:
        return 3
    elif 5.6 <= clicks_per_second <= 7.4:
        return 4
    else:
        return 5

if __name__ == "__main__":
    petting()

print("Pet Grade:", petgrade)

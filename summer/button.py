from graphics import *

class Button:

    def __init__(self, win, center, width, height, label):
        w, h = width/2, height/2
        x, y = center.getX(), center.getY()
        p1 = Point(x+w, y+h)
        p2 = Point(x-w, y-h)
        self.xmin, self.ymin = x-w, y-h
        self.xmax, self.ymax = x+w, y+h
        self.rect = Rectangle(p1, p2)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.color1, self.color2 = 'grey', 'lightgrey'
        self.activate()

    def clicked(self, p):
        return ((self.xmin <= p.getX() <= self.xmax) &
                (self.ymin <= p.getY() <= self.ymax) &
                self.active)


    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True
        self.rect.setFill(self.color1)

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
        self.rect.setFill(self.color2)

    def setColor(self, color1, color2):
        self.color1, self.color2 = color1, color2

def main():
    win = GraphWin()
    myButton = Button(win, Point(100,100), 50, 20, 'Fire!')

    color = 'red'
    win.setBackground(color)
    while True:
        p = win.getMouse()
        if myButton.clicked(p):
            if color == 'red':
                color = 'green'
                win.setBackground('green')
            else:
                color = 'red'
                win.setBackground('red')

if __name__ == '__main__':
    main()

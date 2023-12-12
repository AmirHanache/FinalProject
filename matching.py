from graphics import *
import random
import time

class Card:

    def __init__(self, value, position):
        self.value = value ## trick
        self.position = position
        self.isFlipped = False ## all cards start face down

class MemoryGame:

    def __init__(self, win):
        self.cards = []
        self.win = win
        self.board = []
        self.selectCards = []
        self.createCards()
        self.drawBoard()

    def createCards(self):

        tricks = ["SIT", "STAY", "PAW", "TOUCH", "DOWN", "ROLL", "SIT", "STAY", "PAW", "TOUCH", "DOWN", "ROLL"]
        random.shuffle(tricks)
        for i in range(3):
            row = []
            for j in range(4):
                card = Card(tricks[i*4 + j], (i,j))
                row.append(card)
            self.cards.append(row)

    def drawBoard(self):
        cardSize = 100
        margin = 10

        for i in range(3):
            row = []
            for j in range(4):
                rect = Rectangle(Point(j * (cardSize + margin), i * (cardSize + margin)),
                                 Point((j + 1) * cardSize + j * margin, (i + 1) * cardSize + i * margin))
                rect.draw(self.win)
                rect.setFill("lightgreen")
                label = Text(rect.getCenter(), "")
                label.setStyle("bold")
                label.draw(self.win)
                label.setSize(12)
                row.append((rect, label))
            self.board.append(row)

    def flipCard(self, card):
        row, col = card.position
        rect, label = self.board[row][col]

        if not card.isFlipped:
            label.setText(str(card.value))
            rect.setFill("lightpink")
        else:
            label.setText("")
            rect.setFill("lightgreen")
        card.isFlipped = not card.isFlipped


    def clicks(self, click):
        for i in range(3):
            for j in range(4):
                rect,label = self.board[i][j]
                if rect.getP1().getX() <= click.getX() <= rect.getP2().getX() and \
                        rect.getP1().getY() <= click.getY() <= rect.getP2().getY():
                    card = self.cards[i][j]
                    self.flipCard(card)
                    print(card.value)
                    return card

    def playGame(self):
        while True:
            click = self.win.getMouse()
            card1 = self.clicks(click)
            click = self.win.getMouse()
            card2 = self.clicks(click)

            if card1.value == card2.value:
                print("You got it!")
                self.selectCards.append(card1.position)
                self.selectCards.append(card2.position)
                if all(card.isFlipped for row in self.cards for card in row):
                    print("Great training!")
                    self.win.close()
                    return
            else:
                print("Try again!")
                time.sleep(1)
                self.flipCard(card1)
                self.flipCard(card2)

def train_game():
    win = GraphWin("Training Game", 430, 430)
    win.setBackground("lightblue")


    game = MemoryGame(win)
    game.playGame()


if __name__ == "__main__":
    main()

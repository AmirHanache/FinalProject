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
        tricks = list("SIT", "STAY", "PAW", "TOUCH", "DOWN", "ROLL")*2
        random.shuffle(tricks)
        for i in range(3):
            row = []
            for j in range(3):
                card = Card(values.pop(), (i,j))
                row.append(card)
            self.cards.append(row)

    def drawBoard(self):
        cardSize = 100
        margin = 10

        for i in range(3):
            row = []
            for j in range(3):
                rect = Rectangle(Point(j * (cardSize + margin), i * (cardSize + margin)),
                                 Point((j + 1) * cardSize + j * margin, (i + 1) * cardSize + i * margin))
                rect.draw(self.win)
                label = Text(rect.getCenter(), "")
                label.setSize(12)
                row.append((rect, label))
            self.board.append(row)

    def flipCard(self, card):
        row, col = card.position
        rect, label = self.board[row][col]

        if not card.isFlipped:
            label.setText(str(card.value))
        else:
            label.setText("")
        card.isFlipped = not card.isFlipped

    def clicks(self, click):
        for i in range(3):
            for j in range(3):
                rect, _ = self.board[i][j]
                if rect.getP1().getX() <= click.getrX() <= rect.getP2().getX() and \
                        rect.getP1().getY() <= click.getY() <= rect.getP2().getY():
                    card = self.cards[i][j]
                    if card.position not in self.selectCards:
                        self.flip_card(card)
                        self.selectCards.append(card.position)
                        return

    def playGame(self):
        while True:
            click = self.qin.getMouse()
            self.clicks(click)

            if len(self.selectCards) == 2:
                time.sleep(1)
                pos1, pos2 = self.selectCards
                card1, card2 = self.cards[pos1[0]][pos1[1]], self.cards[pos2[0]][pos2[1]]

                if card1.value == card2.value:
                    for pos in self.selectCards:
                        self.cards[pos[0]][pos[1]].isFlipped = True
                    if all(card.isFlipped for row in self.cards for card in row):
                        print("Great training!")
                        self.win.close()
                        return

                    else:
                        for pos in self.selectCards:
                            self.flipCard(self.cards[pos[0]][pos[1]])
                    self.selectCards = []

def main():
    win = GraphWin("Training Game", 400, 400)
    win.setBackground("lightblue")

    game = MemoryGame(win)
    game.play()


if __name__ == "__main__":
    main()

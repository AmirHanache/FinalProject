from graphics import *
import random
import time

class Card:

    def __init__(self, value, position):
        self.value = value ## trick
        self.position = position
        self.isFlipped = False ## all cards start face down

class MemoryGame:

    def __init__(self, ):
        self.cards = []
        self.

    def createCards

    def drawBoard

    def flipCard

    def clicks

    def playGame

def main():
    win = GraphWin("Training Game", )
    win.setBackground("lightblue")

    game = MemoryGame(win)
    game.play()


if __name__ == "__main__":
    main()

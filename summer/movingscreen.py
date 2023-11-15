import sys
sys.path.insert(0, '..')
from graphics import *

win = GraphWin('Moving Scene', 600, 600)

i = 0
while True:

    im = Image(Point(300, 300), 'Summer_{}.gif'.format(i))
    im.draw(win)
    update(20)
    i += 1
    key = win.checkKey()
    if key:
        break

import sys
sys.path.insert(0, '..')
from graphics import *

win = GraphWin('Moving Scene', 600, 600, autoflush=False)
im = Image(Point(300, 300), 'Summer_0.gif')
i = 0
while True:
    im.undraw()
    i = i % 1011
    im = Image(Point(300, 300), 'Summer_{}.gif'.format(i))
    im.draw(win)
    update(10)
    i += 1
    key = win.checkKey()
    if key:
        break

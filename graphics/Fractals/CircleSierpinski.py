from graphics import *

win = GraphWin("Fraactaaaal!!", 800, 800)

x=400
y=400
r=200

def drawCircle(x,y,r):
    print(x)
    print(y)
    print(r)
    cir = Circle(Point(x,y), r)
    cir.draw(win)
    if(r > 5):
        drawCircle(x - r,y,r/2)
        drawCircle(x + r,y,r/2)
        drawCircle(x, y + r, r/2)

win.getMouse()

drawCircle(x,y,r)

win.getMouse()

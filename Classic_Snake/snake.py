from graphics import *
import time
import random


 
block = 50

rows = int(input("How many rows?"))
columns = int(input("How many columns?"))
width = (block * columns) + (columns - 1)
height = (block * rows) + (rows - 1)

global snake
snake = []
global pivots
pivots = []
global appleList
appleList = []

direction = 'none'

win = GraphWin("Snake Game", width, height)

playAgain = True

def main():
        global snake
        global pivots
        global appleList
        global playAgain
                                                                                        #sets game speed
        frameTime = .2
        lastFrame = 0 

                                                                                        #draws grid lines
        for i in range(columns):
                v = Line(Point(i * (block + 1),0), Point(i * (block +1),height))
                v.draw(win)
                
        for i in range(rows):
                h = Line(Point(0, i * (block + 1)), Point(width, i * (block + 1)))
                h.draw(win)

                                                                                        #creates head of snake
        head = Rectangle(Point(0,0), Point((block + 1),(block + 1)))
        head.draw(win)
        head.setFill('green')
        head.setOutline('green')
        snake.append(head)
        
                                                                                        #waits for player to start game
        gameStart = False
        while gameStart == False:
                startKey = win.getKey()
                if startKey == 'Right':
                        snake[0].direction = 'right'
                        gameStart = True
                elif startKey == 'Down':
                        snake[0].direction = 'down'
                        gameStart = True
                else:
                        None



       
                                                                                        #game's main loop
        gameContinue = True
        while gameContinue:


                                                                                        #checks for existing apple       
                if len(appleList) < 1:
                        makeApple()
                print()
                key = win.checkKey()

                if key:
                        print(key)
                        

                if key == 'Right':
                        makePivot('Right')
                elif key == 'Left':
                        makePivot('Left')
                elif key == 'Up':
                        makePivot('Up')
                elif key == 'Down':
                        makePivot('Down')

                                                                                        #controls frame updates
                if (time.time() - lastFrame) >= frameTime:

                        
                        update()
                        lastFrame = time.time()                                         #checks for snake death

                if len(snake) > 1:        
                        for part in snake[1:]:
                                if (snake[0].getP1().getX() == part.getP1().getX() and
                                snake[0].getP1().getY() == part.getP1().getY()):
                                        print('You Lose! :(')
                                        time.sleep(2)
                                        print('Play Again? (y/n)')
                                        play = win.getKey()
                                        print(play)
                                        if play == 'y':
                                                for i in snake:
                                                        i.undraw()
                                                snake = []
                                                for i in pivots:
                                                        pivots.remove(i)
                                                pivots = []
                                                for i in appleList:
                                                        i.undraw()
                                                appleList = []
                                                return
                                        elif play == 'n':
                                                playAgain = False
                                                return
                                        else:
                                                playAgain = False
                                                return

                if win.checkKey() == "Escape":
                        gameContinue = False
                        win.close()


def update():

                                                                                        #if snake block hits a pivot point, its direction changes
        for part in snake:
                for i in pivots:
                        if part.getP1().getX() == i[0] and part.getP1().getY() == i[1]:
                                part.direction = i[2]

                                                                                       #stores data to make new snake block at end   
        new_x = snake[-1].getP1().getX()
        new_y = snake[-1].getP1().getY()
        direction = snake[-1].direction

        
                                                                                        #removes pivot when last snake block passes over it
        for i in pivots:
                if snake[-1].getP1().getX() == i[0] and snake[-1].getP1().getY() == i[1]:
                        pivots.remove(i)

                                                                                        #controls updating snake movement
        for part in snake:
                if part.direction == 'up':
                        part.move(0, -(block + 1))

                if part.direction == 'down':
                        part.move(0, (block + 1))

                if part.direction == 'left':
                        part.move(-(block + 1), 0)

                if part.direction == 'right':
                        part.move((block + 1), 0)

                                                                                        #wraps the snake if it goes off-screen
        for part in snake:
                if part.getP1().getX() > (rows * (block + 1) - 1):
                        part.move(-(columns * (block + 1)), 0)
                        
                if part.getP1().getX() < 0:
                        part.move(columns * (block + 1), 0)

                if part.getP1().getY() > (rows * (block + 1) - 1):      
                        part.move(0, -(rows * (block + 1)))

                if part.getP1().getY() < 0:
                        part.move(0, rows * (block + 1))
                

                                                                                        #dictates what happens when snake eats apple
        if (snake[0].getP1().getX() == appleList[0].getP1().getX() and
            snake[0].getP1().getY() == appleList[0].getP1().getY()):

                appleList[0].undraw()
                appleList.remove(appleList[0])
                makeApple()
                addTail(new_x,new_y,direction)

        
        
        
def makePivot(key):
        
        pivot = []
        x = snake[0].getP1().getX()
        pivot.append(x)
        y = snake[0].getP1().getY()
        pivot.append(y)
        direct = snake[0].direction
       
        pivotExists = False
        for i in pivots:
                if i[0] == x and i[1] == y:
                        pivotExists = True
                        break
        '''if pivotExists == False:
                if key == 'Right':
                        pivot.append('right')
                if key == 'Left':
                        pivot.append('left')
                if key == 'Up':
                        pivot.append('up')
                if key == 'Down':
                        pivot.append('down')
                pivots.append(pivot)'''

        
        if pivotExists == False:
                if direct == 'right' or direct == 'left':
                        if key == 'Up':
                                pivot.append('up')
                                pivots.append(pivot)
                        if key == 'Down':
                                pivot.append('down')
                                pivots.append(pivot)
                if direct == 'up' or direct == 'down':
                        if key == 'Right':
                                pivot.append('right')
                                pivots.append(pivot)
                        if key == 'Left':
                                pivot.append('left')
                                pivots.append(pivot)

        
def addTail(x,y,z):
  
  tail = Rectangle(Point(x,y), Point(x + (block + 1), y + (block + 1)))
  tail.draw(win)
  tail.setFill('blue')
  tail.setOutline('blue')
  tail.direction = z
  snake.append(tail)



def makeApple():
        appleOkay = False
        while appleOkay == False:
                
                x = random.randint(0,rows - 1)
                y = random.randint(0,columns - 1)
                appleOkay = True
                        


                for part in snake:
                        if part.getP1().getX() == x and part.getP1().getY() == y:
                                appleOkay = False

        if len(appleList) == 0:
                apple = Rectangle( Point(y*(block+1),x*(block+1)) , Point( (y*(block+1))+(block+1) , (x*(block+1))+(block+1)) )
                apple.draw(win)
                apple.setFill('red')
                apple.setOutline('red')
                appleOkay = True
                appleList.append(apple)

 
while playAgain == True:                 
        main()

input('Thanks for Playing!')


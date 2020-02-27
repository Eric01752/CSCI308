#Eric Schmidt
#Homework 3: Problem 1

import turtle

#Makes a square
def square(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

#Determines square pattern
def blackThenWhite(current, X, Y, WIDTH):
    if current % 2 == 0:
        square(X, Y, WIDTH, "black")
    else:
        square(X, Y, WIDTH, "white")

#Determines square pattern
def whiteThenBlack(current, X, Y, WIDTH):
    if current % 2 != 0:
        square(X, Y, WIDTH, "black")
    else:
        square(X, Y, WIDTH, "white")

#Makes the board
def makeBoard():
    X = 0
    Y = 0
    WIDTH = 50
    
    for x in range(5):
        for y in range(5):
            if x % 2 == 0:
                blackThenWhite(y, X, Y, WIDTH)
            else:
                whiteThenBlack(y, X, Y, WIDTH)
            X += WIDTH
        X = 0
        Y -= WIDTH

makeBoard()

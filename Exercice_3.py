import turtle
import random

escargot = turtle.Turtle()
escargot.speed(10)
escargot.pencolor("red")
turtle.delay(1)

escargott = turtle.Turtle()
escargott.speed(10)
escargott.pencolor("pink")
turtle.delay(1)

escargottt = turtle.Turtle()
escargottt.speed(10)
escargottt.pencolor("green")
turtle.delay(1)

escargotttt = turtle.Turtle()
escargotttt.speed(10)
escargotttt.pencolor("purple")
turtle.delay(1)


for i in range(360):

        escargot.left(random.randint(-100,100))
        escargot.forward(random.randint(0,50))
        escargott.right(random.randint(-100,100))
        escargott.forward(random.randint(0,50))
        escargottt.right(random.randint(-100,100))
        escargottt.forward(random.randint(0,50))
        escargotttt.right(random.randint(-100,100))
        escargotttt.forward(random.randint(0,50))

input()




import turtle
import random

escargot = turtle.Turtle()
escargot.speed(100)
escargot.shape('turtle')
escargot.color("red")
escargot.penup()
escargot.shapesize(random.randint(1,10))
escargot.sety(random.randint(-50,100))
escargot.setx(random.randint(-50,100))


escargott = turtle.Turtle()
escargott.speed(10)
escargott.color("pink")
escargott.penup()
escargott.shape('turtle')
escargott.sety(random.randint(-50,200))
escargott.setx(random.randint(-50,200))
escargott.shapesize(random.randint(1,10))



escargottt = turtle.Turtle()
escargottt.speed(10)
escargottt.penup()

escargottt.color("green")
escargottt.shape('turtle')
escargottt.sety(random.randint(-50,200))
escargottt.setx(random.randint(-50,200))
escargottt.shapesize(random.randint(1,10))


escargotttt = turtle.Turtle()
escargotttt.speed(10)


escargotttt.pencolor("purple")
escargotttt.shape('turtle')
escargotttt.penup()
escargotttt.sety(random.randint(-50,200))
escargotttt.setx(random.randint(-50,200))
escargotttt.shapesize(random.randint(1,10))

turtle.delay(2)

for i in range(360):

        escargot.left(random.randint(-100,100))
        escargot.forward(random.randint(0,5))
        escargott.right(random.randint(-100,100))
        escargott.forward(random.randint(0,5))
        escargottt.right(random.randint(-100,100))
        escargottt.forward(random.randint(0,5))
        escargotttt.right(random.randint(-100,100))
        escargotttt.forward(random.randint(0,5))

        
    
        
    

input()

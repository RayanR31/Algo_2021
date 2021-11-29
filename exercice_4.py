import turtle
import random
 

escargot = turtle.Turtle()
escargot.speed(10)
escargot.shape('turtle')
escargot.color('red')
escargot.penup()
escargot.shapesize(10)
escargot.sety(random.randint(-50,100))
escargot.setx(random.randint(-50,100))


def changeUpPosition():
    escargot.setheading(90)
def changeRightPosition():
    escargot.setheading(0)
def changeLeftPosition():
    escargot.setheading(180)
def changeDownPosition():
    escargot.setheading(270)

turtle.onkeypress(changeUpPosition,"z")
turtle.onkeypress(changeLeftPosition,"q")
turtle.onkeypress(changeRightPosition,"d")
turtle.onkeypress(changeDownPosition,"s")
turtle.listen()

n= 3
tortue = []

def creationEnnemie():
        for enn in range (3):
                enn = turtle.Turtle()
                enn.color(random.random(),random.random(),random.random())
                enn.shape("circle")
                enn.speed(0)
                enn.penup()
                enn.sety(random.randint(-50,200))
                enn.setx(random.randint(-50,200))
        
                enn.shapesize(random.randint(1,10))
                
                tortue.append(enn)

""""             def collison():
                for i in tortue:
                for j in tortue:
                        if i != j and i.distance(j) < i.shapesize()[0] + j.shapesize()[0]:
                                if i.shapesize()[0]< j.shapesize()[0]:
                                        j.shapesize(i.shapesize()[0] + j.shapesize()[0],i.shapesize()[0] + j.shapesize()[0])
                                        remove
                                        hideturtle
                                else:
"""



turtle.delay(0)
creationEnnemie()

while True : 
        for enn in tortue:
                escargot.forward(1)
                enn.left(random.randint(-100,100))
                enn.forward(random.randint(0,5))



input()

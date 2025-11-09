from turtle import *
from random import *

#定义屏幕
t = Turtle()
t.hideturtle()

t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("white")

#主程序

x = randrange(-100,100,10)
y = randrange(-100,100,10)

t.begin_fill()
t.up()
t.goto(x,y)
t.down()
t.color("yellow")
t.speed(0)

for i in range(4):

    t.fd(10)
    t.right(90)    

t.end_fill()

#
t.screen.mainloop()
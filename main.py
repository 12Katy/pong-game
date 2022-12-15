from turtle import Turtle,Screen
from panel import Panel
from ball import Ball
from scoreb import Score
import time
sc=Screen()
sc.setup(width=800,height=600)
sc.title("Pong")
sc.bgcolor("black")
sc.tracer(0)
pos=300
for i in range(20):                                 #screen sepration by dashed line
    sep=Turtle("square")
    sep.shapesize(stretch_wid=0.7,stretch_len=0.2)
    sep.color("white")
    sep.penup()
    pos-=30
    sep.goto(0,pos)

pa_r=Panel(380)
pa_l=Panel(-380)

ball=Ball()

scr_l=Score(-200)
scr_r=Score(200)

sc.listen()
sc.onkeypress(pa_l.up,"w")
sc.onkeypress(pa_l.dw,"s")
sc.onkeypress(pa_r.up,"Up")
sc.onkeypress(pa_r.dw,"Down")



on=True
while on:
    time.sleep(ball.sp)
    sc.update()
    ball.move()
    #detect collisionn with wall with bouncing effect:
    if ball.ycor()>280 or ball.ycor()<-280 :
        ball.bounce_y()
    #detect collision with paddle:
    if (ball.xcor()<-330 and ball.distance(pa_l)<50) or(ball.xcor()>330 and ball.distance(pa_r)<50) :
        ball.bounce_x()        # change x axis
    #misses ball on right side paddle(left will get points)
    if ball.xcor()>380:
        scr_l.sr()
        ball.ref()
    if ball.xcor()<-380:
        scr_r.sr()
        ball.ref()



sc.exitonclick()
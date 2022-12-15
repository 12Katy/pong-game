from turtle import Turtle,Screen
import random
from pract_panel import Panel
sc=Screen()
sc.setup(width=550,height=600)
sc.bgcolor("black")

pn_l=Panel(-220)
pn_r=Panel(220)


sc.listen()
sc.onkey(pn_l.move_up(),"Up")
sc.onkey(pn_l.move_down(),"Down")
sc.onkey(pn_r.move_up(),"Up")
sc.onkey(pn_r.move_down(),"Down")

on=True
while on:
    pn_l.move()
    pn_r.move()


























sc.exitonclick()
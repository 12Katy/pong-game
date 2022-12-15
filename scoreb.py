from turtle import Turtle
class Score(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(pos,250)
        self.score=0
        self.write(f" {self.score}",align="center",font=("bold",35,"normal"))
    def sr(self):
        self.score+=1
        self.clear()
        self.write(f" {self.score}", align="center", font=("bold", 35, "normal"))

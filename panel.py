from turtle import Turtle
class Panel(Turtle):
    def __init__(self,pos):
        self.pos=pos
        super().__init__()
        self.create(pos)
    def create(self,pos):
        self.shape("square")
        self.speed("fastest")
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(pos,0)
    def up(self):
        if self.ycor()>250 :
            pass
        else :
            new_y=self.ycor()+20
            self.goto(self.xcor(),new_y)
    def dw(self):
        if self.ycor()<-250 :
            pass
        else :
            new_y=self.ycor()-20
            self.goto(self.xcor(),new_y)
        #new_y=self.ycor()-20
        # self.goto(self.xcor(),new_y)

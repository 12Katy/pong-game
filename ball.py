from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_mov=10
        self.y_mov=10
        self.sp=0.1
        self.create()
    def create(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.8)
        self.goto(0,0)
    def move(self):
        x=self.xcor()+self.x_mov
        y=self.ycor()+self.y_mov
        self.goto(x,y)
    def bounce_y(self):                     # xcor remains same whle y need to be in reverse direction for that we are reversing y cor from current cor for bouncing effect
        self.y_mov*=-1
    def bounce_x(self):
        self.x_mov*=-1
        self.sp*=0.9
    def ref(self):
        self.goto(0,0)
        self.x_mov*=-1
        self.sp=0.1


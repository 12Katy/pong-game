from turtle import Turtle
class Panel(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.pos=pos
        self.panel=[]
        self.create(pos)
        self.tail=self.panel[-1]
    def create(self,pos):
        for i in range(3):
            pan=Turtle("square")
            pan.penup()
            pan.color("white")
            pan.goto(pos,10*i)
            self.panel.append(pan)
    def move(self):
        for i in range(2,0,-1):
            x=self.panel[i-1].xcor()
            y=self.panel[i-1].ycor()
            self.tail.setheading(90)
            self.panel[i].goto(x,y)
            self.tail.forward(10)
    def move_up(self):
        self.setheading(90)
    def move_down(self):
        self.setheading(270)



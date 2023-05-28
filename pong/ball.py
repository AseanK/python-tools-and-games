from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        
        self.pu()
        self.shape("square")
        self.color("red")
        self.speed(20)


    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.setpos(new_x, new_y)
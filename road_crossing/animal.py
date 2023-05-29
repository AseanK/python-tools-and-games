from turtle import Turtle

MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Animal(Turtle):
    def __init__(self):
        super().__init__()

        self.pu()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.sety(-280)
    
    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.sety(new_y)
    
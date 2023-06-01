from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        
        self.shape("square")
        self.color("white")
        self.pu()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(position, 0)

    # Move paddle up
    def up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    # Move paddle down
    def down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)
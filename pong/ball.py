from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        
        self.pu()
        self.shape("square")
        self.color("white")
        self.speed(20)
        self.x_position = 10
        self.y_position = 10

    def move(self):
        new_x = self.xcor() + self.x_position
        new_y = self.ycor() + self.y_position
        self.setpos(new_x, new_y)

    
    def bounce_wall(self):
        self.y_position *= -1

    
    def bounce_paddle(self):
        self.x_position *= -1

    def reset(self):
        self.setpos(0, 0)

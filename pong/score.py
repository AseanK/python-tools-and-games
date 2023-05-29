from turtle import Turtle

class score(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.pu()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.clear()
        self.setpos(-150, 200)
        self.write(f"Score: {self.left_score}", align="center", font=('Arial', 18, 'normal'))

        self.setpos(150, 200)
        self.write(f"Score: {self.right_score}", align="center", font=('Arial', 18, 'normal'))


    def left_point(self):
        self.left_score += 1
        self.update()

    def right_point(self):
        self.right_score += 1
        self.update()
from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.create_level()


    # Create current level text
    def create_level(self):
        self.pu()
        self.hideturtle()
        self.setpos(-250, 260)
        self.write(f"Current level: {self.lvl}", font=("Courier", 18, "normal"))


    # Updates current level
    def level_up(self):
        self.reset()
        self.lvl += 1
        self.create_level()

    
    # Game over text
    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER",align="center", font=("Courier", 18, "normal"))
    
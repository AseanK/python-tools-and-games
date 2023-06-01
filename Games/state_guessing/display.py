from turtle import Turtle
import pandas

# Read .csv data using pandas
data = pandas.read_csv("./50_states.csv", index_col=False)


class Display(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.guessed = []


    # Displays states im the map
    def show(self, state):
        cor = data[data["state"] == state]

        self.setpos(int(cor.x), int(cor.y))
        self.write(f"{state}", font=("Arial", 8, "normal"))
        self.guessed.append(state)



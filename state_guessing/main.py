import turtle
import pandas
from display import Display

# Turtle window
screen = turtle.Screen()
screen.bgpic("./state_guessing/blank_states_img.gif")
screen.setup(725, 491)
screen.title("Guess The States")

# Read .csv data using pandas and put all states in a set
data = pandas.read_csv("./states_guessing/50_states.csv")
states = set(data["state"])
# Displays states in the map
display = Display()

# Users guessed states
# TODO: Using guessed list, work on the HINT 
guessed = []
while len(guessed) < 50:
    user_ans = screen.textinput(title=f"{len(guessed)}/50 States", prompt="Enter the state").title()

    if user_ans in states:
        guessed.append(user_ans)
        display.show(user_ans)
    
turtle.mainloop()
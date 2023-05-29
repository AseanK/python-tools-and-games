from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_SPEED = 5
INCREASE_SPEED = 10

class Cars:
    def __init__(self):
        self.all_cars = []
        for _ in range(15):
            y_pos = randint(-250, 250)
            x_pos = randint(0, 250)
            color = choice(COLORS)

            new_car = Turtle("square")
            new_car.pu()
            new_car.color(color)
            new_car.turtlesize(stretch_len=2, stretch_wid=1)
            new_car.setpos(x_pos, y_pos)

            self.all_cars.append(new_car)


    def create_car(self):
        chance = randint(1,5)
        if chance == 1:
            y_pos = randint(-250, 250)
            color = choice(COLORS)

            new_car = Turtle("square")
            new_car.pu()
            new_car.color(color)
            new_car.turtlesize(stretch_len=2, stretch_wid=1)
            new_car.setpos(300, y_pos)

            self.all_cars.append(new_car)
        

    def move_cars(self):
        for car in self.all_cars:
            car.bk(STARTING_SPEED)

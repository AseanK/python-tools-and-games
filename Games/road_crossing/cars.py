from turtle import Turtle
from random import randint, choice

# Global val
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
INCREASE_SPEED = 10
STARTING_SPEED = 5

class Cars:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_SPEED
        self.create_car()

    # Create cars / decreased # of cars with randint
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
        

    # Move cars
    def move_cars(self):
        for car in self.all_cars:
            car.bk(self.speed)


    # Increase the speed of cars
    def level_up(self):
        for car in self.all_cars:
            car.setpos(1000 ,1000)
        self.all_cars = []
        self.speed += INCREASE_SPEED
        self.create_car()
        self.move_cars()
from turtle import Screen
from animal import Animal
from cars import Cars
from random import randint
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Road Crossing")
screen.tracer(0)
screen.listen()

animal = Animal()
car = Cars()

screen.onkeypress(animal.move_up, "Up")
screen.onkeypress(animal.move_down, "Down")

game_on = True
while game_on:
    sleep(.05)
    screen.update()
    car.create_car()
    car.move_cars()

screen.exitonclick()
from turtle import Screen
from animal import Animal
from cars import Cars
from level import Level
from time import sleep

# turtle screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Road Crossing")
screen.tracer(0)
screen.listen()

animal = Animal()
car = Cars()
display = Level()

screen.onkeypress(animal.move_up, "Up")
screen.onkeypress(animal.move_down, "Down")


# Main loop
game_on = True
while game_on:
    sleep(.05)
    screen.update()
    car.create_car()
    car.move_cars()

    # Game over when hit by the car
    for each_car in car.all_cars:
        if each_car.distance(animal) < 25:
            display.game_over()
            game_on = False

    # Level up when the player reaches certain y_cor
    if animal.ycor() > 280:
        animal.reset_animal()
        display.level_up()
        car.level_up()


screen.exitonclick()
from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()


l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_on = True
while game_on:
    sleep(.1)
    ball.move()
    screen.update()




screen.exitonclick()
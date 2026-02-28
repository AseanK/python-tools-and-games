from turtle import Screen
from time import sleep
from score import score
from random import choice

from utils import package_installer
package_installer.install_dependencies()

from paddle import Paddle
from ball import Ball

# Global val
SPEEDS = [.08, .07, .06, .05, .04, .03, .02, .01]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

# Paddle X-axis position
l_paddle = Paddle(-350)
r_paddle = Paddle(350)

ball = Ball()

scoreboard = score()

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


# Main game loop
game_on = True
speed = 0.07
while game_on:
    # time.sleep() = speed of the ball / lower = faster
    sleep(speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_wall()

    # When ball hits the either paddle/ flip the X-axis
    # Random speed
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
        speed = choice(SPEEDS)

    # Left paddle scores
    if ball.xcor() > 360:
        scoreboard.left_point()
        ball.reset()
        ball.bounce_paddle()
        speed = 0.07
    
    # Right paddle scores
    if ball.xcor() < -360:
        scoreboard.right_point()
        ball.reset()
        ball.bounce_paddle()
        speed = 0.07



screen.exitonclick()
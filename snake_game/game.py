import turtle
import time
import random
import winsound
import pygame
from constants import *

# Global variables
game_delay = INITIAL_DELAY
current_score = 0
high_score = 0
snake_body_segments = []
paused = False 
previous_direction = "stop"
current_difficulty = "easy"



pygame.mixer.init()  # Initialize the mixer module

eat_sound = pygame.mixer.Sound('eat.wav')
die_sound = pygame.mixer.Sound('die.wav')

# Screen setup
game_screen = turtle.Screen()
game_screen.title("Snake Game")
game_screen.bgcolor(SCREEN_COLOR)
game_screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
game_screen.tracer(0)

# Draw border
border = turtle.Turtle()
border.penup()
border.hideturtle()
border.pensize(3)
border.color("white")
border.goto(-BOUNDARY_LIMIT, -BOUNDARY_LIMIT)
border.pendown()
for _ in range(4):
    border.forward(BOUNDARY_LIMIT * 2)
    border.left(90)

def create_turtle(shape, color, position):
    """Helper function to create a turtle."""
    turtle_object = turtle.Turtle()
    turtle_object.speed(0)
    turtle_object.shape(shape)
    turtle_object.color(color)
    turtle_object.penup()
    turtle_object.goto(position)
    return turtle_object

# Snake head
snake_head = create_turtle("square", SNAKE_HEAD_COLOR, SNAKE_HEAD_INITIAL_POSITION)
snake_head.direction = "stop"

# Snake food
snake_food = create_turtle("circle", FOOD_COLOR, FOOD_INITIAL_POSITION)

# Pen (for writing score)
score_pen = create_turtle("square", "white", (0, SCREEN_HEIGHT/2 - 30))
score_pen.hideturtle()
score_pen.write("Score: 0  High Score: 0", align="center", font=SCORE_FONT)

# Difficulty label
difficulty_label = create_turtle("square", "white", (0, SCREEN_HEIGHT/2 - 60))
difficulty_label.hideturtle()  # make it invisible for now
difficulty_label.write("", align="center", font=SCORE_FONT)

# Difficulty buttons
easy_button = create_turtle("square", "white", (-100, 0))  # in the middle and slightly to the left
easy_button.write("Easy", align="center", font=SCORE_FONT)

hard_button = create_turtle("square", "white", (100, 0))  # in the middle and slightly to the right
hard_button.write("Hard", align="center", font=SCORE_FONT)


def toggle_difficulty(difficulty):
    """Sets the game delay based on the specified difficulty."""
    global game_delay, current_difficulty
    game_delay = INITIAL_DELAY if difficulty == "easy" else HARD_DELAY
    current_difficulty = difficulty  # Update the current difficulty
    difficulty_label.clear()
    difficulty_label.write(f"Difficulty: {difficulty.title()}", align="center", font=SCORE_FONT)


def set_difficulty(difficulty):
    """Sets the difficulty to the specified level."""
    toggle_difficulty(difficulty)
    easy_button.clear()  # clears the 'Easy' text
    hard_button.clear()  # clears the 'Hard' text
    easy_button.hideturtle()
    hard_button.hideturtle()


easy_button.onclick(lambda x, y: set_difficulty("easy"))
hard_button.onclick(lambda x, y: set_difficulty("hard"))



def update_score_display():
    """Updates the score on the screen."""
    score_pen.clear()
    score_pen.write(f"Score: {current_score}  High Score: {high_score}", align="center", font=SCORE_FONT)

def change_direction(new_direction):
    """Changes direction of the snake unless it's going in the opposite direction."""
    global previous_direction
    if snake_head.direction == "stop" or new_direction != OPPOSITE_DIRECTIONS[snake_head.direction]:
        previous_direction = snake_head.direction
        snake_head.direction = new_direction


# Movement functions
game_screen.listen()
for key, direction in DIRECTION_KEYS.items():
    game_screen.onkeypress(lambda direction=direction: change_direction(direction), key)

def move_snake():
    """Moves the snake in the current direction."""
    x, y = snake_head.xcor(), snake_head.ycor()

    if snake_head.direction == "up":
        snake_head.sety(y + 20)
    elif snake_head.direction == "down":
        snake_head.sety(y - 20)
    elif snake_head.direction == "left":
        snake_head.setx(x - 20)
    elif snake_head.direction == "right":
        snake_head.setx(x + 20)

def has_collided_with_boundary():
    """Checks if the snake head has collided with the boundary."""
    x, y = snake_head.xcor(), snake_head.ycor()
    if abs(x) > BOUNDARY_LIMIT - TURTLE_SIZE or abs(y) > BOUNDARY_LIMIT - TURTLE_SIZE:
        die_sound.play()
        reset_game()
        return True
    return False

def has_eaten_food():
    """Checks if the snake head has collided with the food."""
    return snake_head.distance(snake_food) < 20

def has_collided_with_body():
    """Checks if the snake head has collided with the body."""
    return any(segment.distance(snake_head) < 20 for segment in snake_body_segments)

def update_segments():
    """Moves each segment to the position of the previous segment."""
    for index in range(len(snake_body_segments) - 1, 0, -1):
        x = snake_body_segments[index-1].xcor()
        y = snake_body_segments[index-1].ycor()
        snake_body_segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if snake_body_segments:
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_body_segments[0].goto(x, y)

def reset_game():
    """Resets the game when the snake hits the boundary or itself."""
    global current_score, game_delay, snake_body_segments

    # Pause the game for a second
    time.sleep(1)
    snake_head.goto(0, 0)
    snake_head.direction = "stop"

    # Hide the segments
    for segment in snake_body_segments:
        segment.goto(1000, 1000)

    # Clear the segments list
    snake_body_segments.clear()

    # Reset the score
    current_score = 0

    # Reset the delay based on the current difficulty
    toggle_difficulty(current_difficulty)  # Call the function here

    # Update the score display
    update_score_display()


def add_segment():
    """Adds a new segment to the snake."""
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    snake_body_segments.append(new_segment)

# Pause function
def toggle_pause():
    """Pause or unpause the game."""
    global paused, previous_direction
    paused = not paused
    if paused:
        # Store the previous direction and stop the snake
        previous_direction = snake_head.direction
        snake_head.direction = "stop"
    else:
        # Restore the previous direction
        snake_head.direction = previous_direction

game_screen.onkeypress(toggle_pause, "p")  

# Main game loop
while True:
    game_screen.update()

    if not paused:  # only run game logic when not paused
        if has_collided_with_boundary() or has_collided_with_body():
            reset_game()

        if has_eaten_food():
            x = random.randint(-BOUNDARY_LIMIT + TURTLE_SIZE, BOUNDARY_LIMIT - TURTLE_SIZE)
            y = random.randint(-BOUNDARY_LIMIT + TURTLE_SIZE, BOUNDARY_LIMIT - TURTLE_SIZE)
            snake_food.goto(x, y)
            add_segment()
            eat_sound.play()
            game_delay -= DELAY_DECREMENT
            current_score += SCORE_INCREMENT
            if current_score > high_score:
                high_score = current_score
            update_score_display()

        update_segments()
        move_snake()

    time.sleep(game_delay)

turtle.mainloop()
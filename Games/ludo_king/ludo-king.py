import sys
import random

from utils import package_installer
package_installer.install_dependencies()

import pygame

# Initialization Pygame
pygame.init()

# Set Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Create the window
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ludo King")

# Set positions for the pawns
positions = {
    'red': [(100, 500), (200, 500), (100, 400), (200, 400)],
    'green': [(400, 500), (500, 500), (400, 400), (500, 400)],
    'blue': [(400, 100), (500, 100), (400, 200), (500, 200)],
    'yellow': [(100, 100), (200, 100), (100, 200), (200, 200)]
}

# Define the dice
dice = {
    'value': 1,
    'rect': pygame.Rect(250, 250, 100, 100)
}

# Function for dice roll
def roll_dice():
    return random.randint(1, 6)

# Function for pawns movements
def move_pawns(color, steps):
    for i in range(len(positions[color])):
        positions[color][i] = (
            positions[color][i][0] + steps * 50,
            positions[color][i][1]
        )

# Basic loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and dice['rect'].collidepoint(event.pos):
            dice['value'] = roll_dice()
            move_pawns('red', dice['value'])  # Move the pawns based on the value of dice

    # Clear the window
    screen.fill(WHITE)

    # Drawing the positions of the pawns
    for color, pos_list in positions.items():
        for pos in pos_list:
            pygame.draw.circle(screen, eval(color.upper()), pos, 20)

    # Daw the dice
    pygame.draw.rect(screen, WHITE, dice['rect'])
    pygame.draw.rect(screen, RED, dice['rect'], 2)
    font = pygame.font.SysFont(None, 36)
    text = font.render(str(dice['value']), True, RED)
    screen.blit(text, (dice['rect'].x + 40, dice['rect'].y + 40))

    # Refresh the window
    pygame.display.flip()


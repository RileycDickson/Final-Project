import pygame
from pygame.locals import *

# initialize pygame
pygame.init()

# Set window size
screen_width = 1000
screen_height = 1000

# Start Pygame
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')


# Keeps running 
run = True
while run:
    # Closes game when winndow is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


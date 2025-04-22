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

tile_size = 50

# load images
sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')

def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

# Keeps running 
run = True
while run:

    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (100, 100))

    draw_grid()

    # Closes game when winndow is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()
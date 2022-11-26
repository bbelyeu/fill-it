import math
import random
import sys

import pygame
from pygame.locals import QUIT

pygame.init()

# limit to x frames per second
frames_per_second = pygame.time.Clock()
frames_per_second.tick(45)

# Set up display object to be x pixels wide and y pixels tall
screen = pygame.display.set_mode((1000, 1000))

# Give it a cool caption
pygame.display.set_caption("Fill It Up!")

# setup color objects
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(128, 128, 128)
red = pygame.Color(255, 0, 0)
purple = pygame.Color(161, 66, 245)
light_blue = pygame.Color(66, 218, 245)
green = pygame.Color(66, 245, 84)
yellow = pygame.Color(227, 245, 66)
pink = pygame.Color(245, 66, 224)

# Make the background white
screen.fill(white)

# Make text header
font = pygame.font.SysFont(None, 48)
num_of_moves = 0
text_header = font.render(f"Steps Used: {num_of_moves}", True, black)
screen.blit(text_header, (340, 10))

# Make game tiles
tile_colors = [red, purple, light_blue, green, yellow, pink]
tile_width = tile_height = 70
for i in range(12):
    top = 75 + (i * tile_height)
    for j in range(12):
        # (left, top), (width, height)
        left = 25 + (j * tile_width)
        tile = pygame.Rect((left, top), (tile_width, tile_height))
        pygame.draw.rect(
            screen, color=random.choice(tile_colors), rect=tile, border_radius=10
        )

# Color choices
bubble_y = 150
circle_centers = []
circle_radius = 50
for color in tile_colors:
    circle_centers.append((930, bubble_y))
    pygame.draw.circle(
        surface=screen, color=color, center=(930, bubble_y), radius=circle_radius
    )
    bubble_y += 125

# Game loop begins
while True:
    # Check if the game was exited
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            sq_x = (mouse_x - circle_centers[0][0]) ** 2
            sq_y = (mouse_y - circle_centers[0][1]) ** 2

            if math.sqrt(sq_x + sq_y) < circle_radius:
                num_of_moves += 1

                if num_of_moves >= 25:
                    screen.fill(color=black)
                    fail_font = pygame.font.SysFont(None, 256)
                    text = fail_font.render("FAIL", True, red)
                    screen.blit(text, (300, 300))

                else:
                    # erase previous text
                    screen.fill(color=white, rect=(0, 0, 1000, 75))
                    text_header = font.render(
                        f"Steps Used: {num_of_moves}", True, black
                    )
                    screen.blit(text_header, (340, 10))

    pygame.display.update()

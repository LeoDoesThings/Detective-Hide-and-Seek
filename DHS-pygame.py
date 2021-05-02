import pygame
from pygame.locals import *


pygame.init()

display_width = 853
display_height = 480

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Detective Hide and Seek')


def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT: # Click the X window button to close program
            pygame.quit()
            quit()

while True:
    event_handler()

    pygame.display.update()

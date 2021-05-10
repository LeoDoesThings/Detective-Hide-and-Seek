import pygame
import pygame.freetype
from pygame.locals import *

import os
import random

class Locations:
    locations = ['forest', 'park', 'cafe', 'house', 'school', 'garden']
    searched = []

    def location_searched(self, location):
        self.searched.append(location)


class Clues:
    seen = []

    forest = [
        "You notice a muddy footprint on the ground...",
        "some dirt on the pavement",
        "a stick on the ground",
        "a leaf blowing past you",
        "a shoelace on the ground"
    ]

    park = [
        "a branch on the ground",
        "some gardening gloves on the ground",
        forest[1],
        forest[2],
        forest[4]
    ]

    cafe = [
        "a coffee cup on the ground",
        "a lid on the ground",
        "some liquid on the ground",
        "some drops on the floor",
        forest[4]
    ]

    house = [
        "a bag on the ground",
        "a wallet on the ground",
        "a book on the ground",
        cafe[3],
        "an HP laptop charger in the basement"
    ]

    school = [
        house[2],
        house[0],
        cafe[2],
        house[1],
        house[4]
    ]

    garden = [
        park[3],
        forest[2],
        forest[1],
        cafe[2],
        forest[3]
    ]

    def getRandom(location):
        # Random clue related to location
        random.choice(location)

class Game:
    level = 1
    time = 60
    # Randomly pick a hiding palce
    hidingplace = random.choice(Locations.locations)
    
    def checkHidingPlace(location, level, time):
        if location == hidingplace:
            print("You found the computer!")
            # Increase difficulty
            level += 1
            time -= 1
        else:
            print("You stare into a void of empty nothingness.")
            chance = random.randint(0, level)
            if chance == level:
                Clues.getRandom(location)



# Start game
pygame.init()
pygame.font.init()

# Set window size to 480p
display_width = 853
display_height = 480
screen = pygame.display.set_mode((display_width, display_height))
# Limit fps to save computer resources used
clock = pygame.time.Clock()
FPS = 60

center_x = display_width / 2
center_y = display_height / 2

# Set colours
background_grey = (32, 33, 36)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
red1 = (200, 0, 0)
green = (0, 255, 0)
green1 = (0, 200, 0)

# Import fonts
dir_path = os.path.dirname(os.path.realpath(__file__))
class Poppins:
    bold = pygame.font.Font(os.path.join(dir_path, 'resources/fonts/Poppins-Black.ttf'), 38)
    regular = pygame.font.Font(os.path.join(dir_path, 'resources/fonts/Poppins-Regular.ttf'), 24)
    thin = pygame.font.Font(os.path.join(dir_path, 'resources/fonts/Poppins-Thin.ttf'), 18)

class img:
    title = Poppins.bold.render('Detective Hide and Seek', True, white, background_grey)

# Set window name
pygame.display.set_caption('Detective Hide and Seek')

def quitgame():
    pygame.quit()
    quit()

def text_objects(text, font, color):
    rendered = font.render(text, True, color)
    return rendered

def button(msg, textcolour, font, x,y, w,h, colour,hovercolour, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, hovercolour,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, colour,(x,y,w,h))

    textSurf = text_objects(msg, font, textcolour)
    screen.blit(textSurf, (x,y))

def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT:  # Click the X window button to close program
            quitgame()
        if event.key == pygame.K_SPACE:
                timer_started = not timer_started
                if timer_started:
                    start_time = pygame.time.get_ticks()

class Page:
    def clear():
        screen.fill(background_grey)

    def start():
        screen.blit(img.title, img.title.get_rect(center=(display_width/2, 30)))
        button("Start", "black", Poppins.regular, center_x-40,center_y+100, 80,30, green,green1)
        button("Quit", "black", Poppins.regular, center_x-40,center_y+140, 80,30, red,red1, quitgame)

timer_started = False

while True:
    event_handler()
    mouse = pygame.mouse.get_pos()

    Page.start()

    pygame.display.update()
    if timer_started:
        passed_time = pygame.time.get_ticks() - start_time
    clock.tick(FPS)

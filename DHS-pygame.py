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
    
    def isHidingPlace(location):
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
# This will be useful for centering and other stuff later on
screen_rect = screen.get_rect()

# Set colours
background_grey = (32, 33, 36)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
red1 = (200, 0, 0)
green = (0, 255, 0)
screen.fill(background_grey)

# Import fonts
dir_path = os.path.dirname(os.path.realpath(__file__))
class Poppins:
    bold = pygame.font.Font(os.path.join(dir_path, 'resources/fonts/Poppins-Black.ttf'), 38)
    regular = pygame.font.Font(os.path.join(dir_path, 'resources/fonts/Poppins-Regular.ttf'), 24)
    thin = pygame.font.Font(os.path.join(dir_path, 'resources/fonts/Poppins-Thin.ttf'), 18)

class img:
    title = Poppins.bold.render('Detective Hide and Seek', True, white, background_grey)
    start_button = Poppins.regular.render('Start', True, black, green)
    quit_button = Poppins.regular.render('Quit', True, black, red)

# Set window name
pygame.display.set_caption('Detective Hide and Seek')

def quitgame():
    pygame.quit()
    quit()

def center(rendered):
    return rendered.get_rect(center=screen_rect.center)

def text_objects(text, font, color, text_center):
    rendered = font.render(text, True, color)
    if text_center == True:
        return rendered, center(rendered)
    else:
        return rendered

def button(msg, x,y, w,h, colour,hovercolour, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, hovercolour,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, colour,(x,y,w,h))

    textSurf, textRect = text_objects(msg, Poppins.regular, colour, True)
    screen.blit(textSurf, textRect)

def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT:  # Click the X window button to close program
            quitgame()

class Page:
    def start():
        screen.blit(img.title, img.title.get_rect(center=(display_width/2, 30)))
        screen.blit(img.start_button, img.start_button.get_rect(center=(display_width/2, 340)))
        button("Quit", 426,380, 20,10, red,red1, quitgame)


while True:
    event_handler()
    mouse = pygame.mouse.get_pos()

    Page.start()

    pygame.display.update()

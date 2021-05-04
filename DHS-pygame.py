import pygame
from pygame.locals import *

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

# Set window size to 480p
display_width = 853
display_height = 480
game_display = pygame.display.set_mode((display_width, display_height))

# Set window name
pygame.display.set_caption('Detective Hide and Seek')


def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT:  # Click the X window button to close program
            pygame.quit()
            quit()


while True:
    event_handler()

    pygame.display.update()

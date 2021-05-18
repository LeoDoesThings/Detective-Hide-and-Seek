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
    timer_started = False
    # Randomly pick a hiding palce
    hidingplace = random.choice(Locations.locations)
    
    def checkHidingPlace(self, location):
        if location == self.hidingplace:
            # Increase difficulty
            self.level += 1
            self.time -= 1
            return True
        else:
            chance = random.randint(0, self.level)
            if chance == self.level:
                return False, Clues.getRandom(location)
            else:
                return False

    def startTimer(self):
        if self.timer_started == False:
            return pygame.time.get_ticks()
        else:
            return 0

    
    def gameOver():
        print("Game over!")




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
    thin = pygame.font.Font(os.path.join(dir_path, 'resources/fonts/Poppins-Thin.ttf'), 20)

class img:
    title = Poppins.bold.render('Detective Hide and Seek', True, white, background_grey)

# Set window name
pygame.display.set_caption('Detective Hide and Seek')

def quitgame():
    pygame.quit()
    quit()

class Graphics:
    def text_object(text, font, color, background=None):
        rendered = font.render(text, True, color, background)
        return rendered

    def button(self, msg, textcolour, font, x,y, w,h, colour,hovercolour, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(screen, hovercolour,(x,y,w,h))

            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(screen, colour,(x,y,w,h))

        textSurf = self.text_object(msg, font, textcolour)
        screen.blit(textSurf, (x,y))

class showPage:
    def __init__(self):
        self.show_startmenu = True
        self.show_game = False
        self.show_clue = False
        self.show_gameover = False

    def startmenu(self):
        self.show_startmenu = True
        self.show_game = False

    def game(self):
        self.show_startmenu = False
        self.show_game = True

Game = Game()
showPage = showPage()


while True:
    screen.fill(background_grey)
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:  # Click the X window button to close program
            quitgame()

    if showPage.show_startmenu:
        screen.blit(img.title, img.title.get_rect(center=(display_width/2, 30)))
        Graphics.button(Graphics, "Start", "black", Poppins.regular, center_x-40,center_y+100, 80,30, green,green1, showPage.game)
        Graphics.button(Graphics, "Quit", "black", Poppins.regular, center_x-40,center_y+140, 80,30, red,red1, quitgame)

        pygame.display.update()
        clock.tick(FPS)

    elif showPage.show_game:
        
        timer = Game.time
        seconds = (pygame.time.get_ticks()-Game.startTimer())/1000
        timer -= round(seconds)
        timer_text = Graphics.text_object(str(timer), Poppins.thin, white, background_grey)
        screen.blit(timer_text, (display_width-50, 10))

    pygame.display.update()
    clock.tick(FPS)

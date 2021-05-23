import tkinter as tk
from tkmacosx import Button
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
        "some drops on the ground",
        forest[4]
    ]

    house = [
        "a bag on the ground",
        "a wallet on the ground",
        "a book on the ground",
        cafe[3],
        "an HP laptop charger on the ground"
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
Game = Game()


background_grey = "#333"

# Start tkinter
root = tk.Tk()
root['bg'] = background_grey
root.title('Detective Hide and Seek')

# Set window size to 480p
root.geometry('853x480')
# Gets the requested values of the height and width
windowWidth = 853
windowHeight = 480
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/3 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/3 - windowHeight/2)
# Positions the window in the center of the page
root.geometry("+{}+{}".format(positionRight, positionDown))

class Page():
    def __init__(self, window):
        self.components = []
        self.frame = tk.Frame(window, width=windowWidth[0], height=windowHeight[1], bg="#F9EBD1")

    # Add components to page
    def add_component(self, object, xpos, ypos, anchor, width, height):
        self.components.append([object,xpos,ypos, anchor, width, height])
        return

# Game Page Manager
class PageHandler():
    def __init__(self, home):
        self.current = home
    
    # Get the games current page frame
    def getPage(self):
        return self.current.frame

    # Change the games page
    def setPage(self, page):
        # Place all components in desired page
        for component in page.components:
            self.current = page
            object = component[0]
            object.place(x=component[1], y=component[2], anchor=component[3], width=component[4], height=component[5])
            self.current.frame.place(x=0,y=0)

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        main_title = tk.Label(
            text='Detective Hide and Seek',
            foreground="white",
            background=background_grey
        )
        main_title.config(font=("Courier", 44))
        main_title.place()
        main_title.pack(side="top")

        start_button = Button(root, text='Start', bg='#ADEFD1',
            fg='#00203F', borderless=1,
            activebackground='#6eb897',
            activeforeground='#FFFFFF'
            )
        start_button.place(anchor='center', x=windowWidth/2, y=windowHeight-100)

app = App(master=root)
app.mainloop()

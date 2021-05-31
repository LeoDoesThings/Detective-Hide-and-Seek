import tkinter as tk
from tkmacosx import Button
import random
import time


class Locations:
    locations = ['forest', 'park', 'cafe', 'house', 'school', 'garden']
    searched = []

    def location_searched(self, location):
        self.searched.append(location)
locations = Locations()

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
        # New random clue related to location
        clue = random.choice(location)
        return clue

class Game:
    def __init__(self):
        self.level = 1
        self.time = 60
        # Randomly pick a hiding palce
        self.hidingplace = random.choice(locations.locations)

    def checkHidingPlace(self, location):
        location = str(location)
        if location in locations.searched:
            print("You've already searched here!")
        elif location == self.hidingplace:
            # Increase difficulty
            self.level += 1
            self.time -= 1
            return True
        else:
            chance = random.randint(0, self.level)
            if chance == self.level:
                return Clues.getRandom(location)
            else:
                return False

        locations.searched.append(location)

Game = Game()


windowWidth = 853
windowHeight = 480
background_grey = "#333"

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Set tkinter window settings
        self['bg'] = background_grey
        self.title('Detective Hide and Seek')

        # Set window size to 480p
        self.geometry('853x480')
        # Gets both half the screen width/height and window width/height
        positionRight = int(self.winfo_screenwidth()/3 - windowWidth/2)
        positionDown = int(self.winfo_screenheight()/3 - windowHeight/2)
        # Positions the window in the center of the screen
        self.geometry("+{}+{}".format(positionRight, positionDown))

        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.pack_forget()
        self._frame = new_frame
        self._frame.pack()
    
    def superimpose_frame(self, frame_class):
        new_frame = frame_class(self)
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        main_title = tk.Label(
            self,
            text="Detective Hide and Seek",
            font=('Courier', 54, "bold")
        )
        main_title.pack(side="top", pady=5)
        start_button = Button(
            self,
            text='Start',
            bg='#ADEFD1',
            fg='#00203F', borderless=1,
            activebackground='#6eb897',
            activeforeground='#FFFFFF',
            command=lambda: master.switch_frame(MapPage)
        )
        start_button.pack(side="bottom", pady=30)

class MapPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Map", font=('Courier', 54, "bold")).pack(side="top", fill="x", pady=5)
        forest = Button(self, 
            text="Forest",
            bg="#efcead",
            command=lambda: whatthehelldoido(self, forest)
        ).pack()
        park = Button(self, 
            text="Park",
            bg="#efcead",
            command=lambda: whatthehelldoido(self, park)
        ).pack()
        cafe = Button(self, 
            text="Cafe",
            bg="#efcead",
            command=lambda: whatthehelldoido(self, cafe)
        ).pack()
        house = Button(self,
            text="House",
            bg="#efcead",
            command=lambda: whatthehelldoido(self, house)
        ).pack()
        school = Button(self, 
            text="School",
            bg="#efcead",
            command=lambda: whatthehelldoido(self, school)
        ).pack()
        garden = Button(self, 
            text="Garden",
            bg="#efcead",
            command=lambda: whatthehelldoido(self, garden)
        ).pack()

        def whatthehelldoido(self, location):
            whattodo = Game.checkHidingPlace(location)
            if whattodo == True:
                print("You win!")
            elif whattodo == False:
                print("You come up empty.")
            else:
                master.superimpose_frame(CluePage)

class CluePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg='red', width=420, height=69)
        tk.Label(
            self,
            text="Clue", 
            font=('Courier', 18)
        ).pack(
            side="top", 
            pady=5
        )

class GameOverPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        gameover_title = tk.Label(
            self,
            text='Game Over',
            font=("Courier", 44),
            foreground="white",
            background=background_grey
        )
        gameover_title.pack()
        playagain_button = Button(self, text='Play Again?', bg='#ADEFD1',
            fg='#00203F', borderless=1,
            activebackground='#6eb897',
            activeforeground='#FFFFFF',
            command=lambda: master.switch_frame(MapPage)
            )
        playagain_button.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()

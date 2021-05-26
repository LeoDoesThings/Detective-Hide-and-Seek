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
windowWidth = 853
windowHeight = 480


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
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        main_title = tk.Label(
            self,
            text='Detective Hide and Seek',
            font=("Courier", 44),
            foreground="white",
            background=background_grey
        )
        main_title.pack()
        start_button = Button(
            self,
            text='Start',
            background='#ADEFD1',
            foreground='#00203F', borderless=1,
            activebackground='#6eb897',
            activeforeground='#FFFFFF',
            command=lambda: master.switch_frame(MapPage)
            )
        start_button.pack(side="bottom", pady=30)

class MapPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

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

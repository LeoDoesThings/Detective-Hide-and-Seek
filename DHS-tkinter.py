import tkinter as tk
from tkmacosx import Button
import random
import time

class Locations():
    dict = {}
    # These all need to be addded outside of the initial dictionary set
    # because we're copying dictionary values to other keys
    # This could be done in a more efficient way but this is more readable.
    dict["forest"] = [
        "a muddy footprint on the ground...", 
        "some dirt on the pavement",
        "a stick on the ground",
        "a leaf blowing past you",
        "a shoelace on the ground"
    ]

    dict["park"] = [
        "a branch on the ground",
        "some gardening gloves on the ground",
        dict["forest"][1],
        dict["forest"][2],
        dict["forest"][4]
    ]

    dict["cafe"] = [
        "a coffee cup on the ground",
        "a lid on the ground",
        "some liquid on the ground",
        "some drops on the ground",
        dict["forest"][4]
    ]

    dict["house"] = [
        "a bag on the ground",
        "a wallet on the ground",
        "a book on the ground",
        dict["cafe"][3],
        "an HP laptop charger on the ground"
    ]

    dict["school"] = [
        dict["house"][2],
        dict["house"][0],
        dict["cafe"][2],
        dict["house"][1],
        dict["house"][4]
    ]

    dict["garden"] = [
        dict["park"][3],
        dict["forest"][2],
        dict["forest"][1],
        dict["cafe"][2],
        dict["forest"][3]
    ]

    searched = []
    seenclues = []

    def location_searched(self, location):
        self.searched.append(location)

    def getRandomClue(self, location):
        location = str(location)
        # New random clue related to location
        num = random.randrange(0, 5)
        print(location)
        clue = self.dict[location][num]
        while clue in self.seenclues:
            clue = random.choice(location)
        self.seenclues.append(clue)
        return clue
locations = Locations()

class Game():
    def __init__(self):
        self.level = 1
        self.time = 60
        # Randomly pick a hiding palce
        self.hidingplace = random.choice(list(locations.dict))

    def checkHidingPlace(self, location):
        location = str(location)
        if location in locations.searched:
            return "searched"
        elif location == self.hidingplace:
            # Increase difficulty
            self.level += 1
            self.time -= 1
            return True
        else:
            locations.searched.append(location)
            chance = random.randint(0, self.level)
            if chance == self.level:
                return locations.getRandomClue(location)
            else:
                return False

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
            command=lambda: whatthehelldoido(forest)
        ).pack()
        park = Button(self, 
            text="Park",
            bg="#efcead",
            command=lambda: whatthehelldoido(park)
        ).pack()
        cafe = Button(self, 
            text="Cafe",
            bg="#efcead",
            command=lambda: whatthehelldoido(cafe)
        ).pack()
        house = Button(self,
            text="House",
            bg="#efcead",
            command=lambda: whatthehelldoido(house)
        ).pack()
        school = Button(self, 
            text="School",
            bg="#efcead",
            command=lambda: whatthehelldoido(school)
        ).pack()
        garden = Button(self, 
            text="Garden",
            bg="#efcead",
            command=lambda: whatthehelldoido(garden)
        ).pack()

        def whatthehelldoido(location):
            whattodo = Game.checkHidingPlace(location)
            if whattodo == "searched":
                print("You've searched this place!")
                return
            elif whattodo == True:
                print("You win!")
            elif whattodo == False:
                print("You come up empty.")
            else:
                print(whattodo)
                cluemessage = "You notice " + str(whattodo)
                tk.Label(
                    self,
                    text=cluemessage, 
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

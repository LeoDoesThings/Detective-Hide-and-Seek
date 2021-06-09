import tkinter as tk
import random
import sys

try:
    from tkmacosx import Button
except ImportError:
    sys.exit("""You need tkmacosx!
                install it from https://pypi.org/project/tkmacosx/
                or run pip install tkmacosx.""")

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

    def getRandomClue(self, location):
        # New random clue related to location
        num = random.randrange(0, 5)
        clue = self.dict[location][num]
        while True:
            if clue in self.seenclues:
                clue = random.choice(location)
            else:
                break
        self.seenclues.append(clue)
        return clue
locations = Locations()

class Game(tk.Tk):
    def __init__(self):
        self.level = 1
        self.time = 60
        self.mapcountdown = 0
        self.searchcountdown = 0
        # Randomly pick a hiding place
        self.hidingplace = random.choice(list(locations.dict))
    
    def playagain(self):
        self.hidingplace = random.choice(list(locations.dict))
        App.switch_frame(App, MapPage)

    def checkHidingPlace(self, location):
        location_str = str(location)
        if location_str in locations.searched:
            return "searched"
        elif location_str == self.hidingplace:
            # Increase difficulty
            self.level += 1
            self.time -= 1
            return True
        else:
            locations.searched.append(location_str)
            chance = random.randint(0, self.level)
            if chance == self.level:
                return locations.getRandomClue(location_str)
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

        self.remaining = 0
        self.timerlabel = tk.Label(self, text="", width=10)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.pack_forget()
        self._frame = new_frame
        self._frame.pack()
    
    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.timerlabel.pack_forget()
        else:
            self.timerlabel.pack()
            self.timerlabel.configure(text="%d" % self.remaining, font=('Courier', 24, "bold"))
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

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
            command=lambda: whatthehelldoido("forest")
        ).pack()
        park = Button(self, 
            text="Park",
            bg="#efcead",
            command=lambda: whatthehelldoido("park")
        ).pack()
        cafe = Button(self, 
            text="Cafe",
            bg="#efcead",
            command=lambda: whatthehelldoido("cafe")
        ).pack()
        house = Button(self,
            text="House",
            bg="#efcead",
            command=lambda: whatthehelldoido("house")
        ).pack()
        school = Button(self, 
            text="School",
            bg="#efcead",
            command=lambda: whatthehelldoido("school")
        ).pack()
        garden = Button(self, 
            text="Garden",
            bg="#efcead",
            command=lambda: whatthehelldoido("garden")
        ).pack()

        def whatthehelldoido(location):
            whattodo = Game.checkHidingPlace(location)
            if whattodo == "searched":
                print("You've searched this place!")
                return
            elif whattodo == True:
                master.switch_frame(YouWinPage)
            elif whattodo == False:
                print("You come up empty.")
            else:
                master.switch_frame(SearchingPage)
                cluemessage = "You notice " + str(whattodo)
                tk.Label(
                    self,
                    text=cluemessage,
                    font=('Courier', 18)
                ).pack(side="top", pady=5)

class SearchingPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        searching_title = tk.Label(
            self,
            text='Searching...',
            font=("Courier", 36),
            foreground="white",
            background=background_grey
        ).pack(fill="none", expand=True) # This centers the title in the middle of the screen

        searchingtime = random.randrange(5, 13)
        master.countdown(searchingtime)
        self.after(searchingtime*1000, master.switch_frame, MapPage)

class YouWinPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        roundnum = Game.level-1
        youwin_title = tk.Label(
            self,
            text='You Win!',
            font=("Courier", 44),
            foreground="white",
            background=background_grey
        ).pack()

        roundcomplete = tk.Label(
            self,
            text='Round ' + str(roundnum) + ": Complete",
            font=("Courier", 18),
            foreground="white",
            background=background_grey
        ).pack()

        playagain_button = Button(self, 
            text='Play Round ' + str(roundnum+1), 
            bg='#ADEFD1',
            fg='#00203F', 
            borderless=1,
            activebackground='#6eb897',
            activeforeground='#FFFFFF',
            command=lambda: Game.playagain()
        ).pack()

        exit_button = Button(self, 
            text='Exit', 
            bg='#ADEFD1',
            fg='#00203F', 
            borderless=1,
            activebackground='#6eb897',
            activeforeground='#FFFFFF',
            command=lambda: app.destroy()
        ).pack()

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

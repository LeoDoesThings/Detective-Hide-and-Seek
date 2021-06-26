import tkinter as tk
from tkinter import PhotoImage
import random

try:
    from tkmacosx import Button
except ImportError:
    import sys
    sys.exit("""You need tkmacosx!
                install it from https://pypi.org/project/tkmacosx/
                or run pip install tkmacosx.""")

class Locations():
    dict = {}
    # These all need to be addded outside of the initial dictionary set
    # because we're copying dictionary values to other keys
    dict["forest"] = [
        "a muddy footprint on the ground",
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
        "an HP laptop charger on the ground",
        dict["cafe"][3]
    ]

    dict["school"] = [
        dict["house"][0],
        dict["house"][1],
        dict["house"][2],
        dict["house"][4],
        dict["cafe"][2]
    ]

    dict["garden"] = [
        dict["forest"][1],
        dict["forest"][2],
        dict["forest"][3],
        dict["park"][1],
        dict["cafe"][2]
    ]

    searched = []
    seenclues = []

    def randomClue(self, location):
        num = random.randrange(0, 5)
        return self.dict[location][num]

locations = Locations()

class Game():
    def __init__(self):
        self.level = 1
        self.time = 60
        self.cluechance = 10
        # Randomly pick a hiding place
        self.hidingplace = random.choice(list(locations.dict))

        self.searching = False

    def getClue(self, location):
        location_str = str(location)
        # Remember that this location was searched
        locations.searched.append(Game.searching)
        # Chance for a clue is lower as you level up
        chance = random.randint(self.cluechance, 10)
        if chance == 10:
            # Always show a clue the player hasn't seen before
            while True:
                clue = locations.randomClue(location_str)
                if clue not in locations.seenclues:
                    break
            locations.seenclues.append(clue)
            return clue
        # Tell game that there is no clue
        return False


Game = Game()


windowWidth = 853
windowHeight = 480
background_grey = "#333"

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Set tkinter window settings
        self["bg"] = background_grey
        self.title("Detective Hide and Seek")

        # Set window size to 480p
        self.geometry("853x480")
        # Gets both half the screen width/height and window width/height
        positionRight = int(self.winfo_screenwidth()/3 - windowWidth/2)
        positionDown = int(self.winfo_screenheight()/3 - windowHeight/2)
        # Positions the window in the center of the screen
        self.geometry("+{}+{}".format(positionRight, positionDown))

        # Start the game on the starting page
        self._frame = None
        self.switch_frame(StartPage)

        # Timer settings
        self.remaining = 0
        self.timerlabel = tk.Label(self, text="", width=10)

        # Must set this variable in __init__ before using
        self.playerwon = None

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.pack_forget()
            self._frame.place_forget()
        self._frame = new_frame
        self._frame.pack()

    def playAgain(self, levelup=True, reset=False):
        if levelup is True:
            Game.level += 1
            Game.time -= 5
            if Game.cluechance > 1:
                Game.cluechance -= 1
        if reset is True:
            Game.level = 1
            Game.time = 60
        Game.searching = False
        Game.hidingplace = random.choice(list(locations.dict))
        locations.searched.clear()
        locations.seenclues.clear()
        self.playerwon = False
        self.countdown(Game.time)
        self.switch_frame(MapPage)

    def playerFinished(self, playerwon):
        # Player can only win if timer is still running
        if self.remaining > 0 and playerwon is True:
            self.playerwon = True
            self.remaining = 0
        else:
            self.remaining = 0

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.timerlabel.pack_forget()
            if self.playerwon is False:
                self.switch_frame(GameOverPage)
            else:
                self.switch_frame(YouWinPage)
        else:
            self.timerlabel.pack(side="top", anchor="ne")
            self.timerlabel.configure(
                text="Time: %d" % self.remaining,
                font=("Courier", 24, "bold")
            )
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        main_title = tk.Label(
            self,
            text="Detective Hide and Seek",
            font=("Courier", 54, "bold")
        )
        main_title.pack(side="top", pady=5)

        # Start button
        Button(
            self,
            text="Start",
            bg="#ADEFD1",
            fg="#00203F", borderless=1,
            activebackground="#6eb897",
            activeforeground="#FFFFFF",
            command=lambda: master.playAgain(False)
        ).pack()

        # How to Play button
        Button(
            self,
            text="How to Play",
            bg="#ADEFD1",
            fg="#00203F", borderless=1,
            activebackground="#6eb897",
            activeforeground="#FFFFFF",
            command=lambda: how_to_play.pack()
        ).pack()

        # Exit button
        Button(self,
            text="Exit",
            bg="#ADEFD1",
            fg="#00203F",
            borderless=1,
            activebackground="#6eb897",
            activeforeground="#FFFFFF",
            command=lambda: app.destroy()
        ).pack()

        how_to_play = tk.Label(
            self,
            text="""
You are the Detective. You need to catch the criminal before he escapes!


You'll have 60 seconds, otherwise the criminal is home free.


The criminal might leave clues behind in certain locations that you'll have to
find if you want to catch him in time.

But don't get too confident!
The criminal will learn from his mistakes and won't leave as many clues the
next time you try to catch him.
            """,
            font=("Courier", 16)
        )

class MapPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        def searchLocation(location):
            Game.searching = location
            master.switch_frame(SearchingPage)

        print(Game.hidingplace)
        # Map title
        tk.Label(self,
            text="Map",
            font=("Courier", 54, "bold")
        ).grid(row=1, column=2)

        self.forest_image = PhotoImage(file="resources/img0.png")
        forest = tk.Button(self,
            image=self.forest_image,
            borderwidth=0,
            command=lambda: searchLocation("forest")
        )
        if "forest" not in locations.searched:
            forest.grid(row=4, column=1)

        self.park_image = PhotoImage(file="resources/img1.png")
        park = tk.Button(self,
            image=self.park_image,
            borderwidth=0,
            command=lambda: searchLocation("park")
        )
        if "park" not in locations.searched:
            park.grid(row=4, column=2)

        self.cafe_image = PhotoImage(file="resources/img2.png")
        cafe = tk.Button(self,
            image=self.cafe_image,
            borderwidth=0,
            command=lambda: searchLocation("cafe")
        )
        if "cafe" not in locations.searched:
            cafe.grid(row=4, column=3)

        self.house_image = PhotoImage(file="resources/img3.png")
        house = tk.Button(self,
            image=self.house_image,
            borderwidth=0,
            command=lambda: searchLocation("house")
        )
        if "house" not in locations.searched:
            house.grid(row=5, column=1)

        self.school_image = PhotoImage(file="resources/img4.png")
        school = tk.Button(self,
            image=self.school_image,
            borderwidth=0,
            command=lambda: searchLocation("school")
        )
        if "school" not in locations.searched:
            school.grid(row=5, column=2)

        self.garden_image = PhotoImage(file="resources/img5.png")
        garden = tk.Button(self,
            image=self.garden_image,
            borderwidth=0,
            command=lambda: searchLocation("garden")
        )
        if "garden" not in locations.searched:
            garden.grid(row=5, column=3)

class SearchingPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Searching title message
        tk.Label(
            self,
            text="Searching...",
            font=("Courier", 36),
            foreground="white",
            background=background_grey
        ).pack()

        self.remaining = 0
        self.timerlabel = tk.Label(self, text="", width=10)

        searchingtime = random.randrange(8, 14)
        self.countdown(searchingtime)

        # Check timer is still running before finishing the search
        # otherwise it override the switch to GameOverPage
        def finishSearch():
            if master.remaining > 0:
                master.switch_frame(MapPage)

        if Game.searching == Game.hidingplace:
            # Must have a clue otherwise script returns an error sometimes
            self.clue = False
            waittime = random.randrange(4, searchingtime-1)
            self.after(waittime*1000, master.playerFinished, True)
        else:
            self.clue = Game.getClue(Game.hidingplace)
            self.after(searchingtime*1000, finishSearch)

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining == 3 and Game.searching != Game.hidingplace:
            if self.clue is False:
                tk.Label(
                    self,
                    text="You come up empty.",
                    font=("Courier", 18)
                ).pack(side="top", pady=5)
            else:
                tk.Label(
                    self,
                    text=f"You notice {self.clue}",
                    font=("Courier", 18)
                ).pack(side="top", pady=5)

        if self.remaining <= 0:
            self.timerlabel.pack_forget()
        else:
            self.timerlabel.pack()
            self.timerlabel.configure(text="%d" % self.remaining, font=("Courier", 24, "bold"))
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

class YouWinPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        roundnum = Game.level
        # You Win title message
        tk.Label(
            self,
            text="You Win!",
            font=("Courier", 44),
            foreground="white",
            background=background_grey
        ).pack()

        # Round compelete message
        tk.Label(
            self,
            text=f"Round {roundnum}: Complete",
            font=("Courier", 18),
            foreground="white",
            background=background_grey
        ).pack()

        # Play again button
        Button(self,
            text=f"Play Round {roundnum+1}",
            bg="#ADEFD1",
            fg="#00203F",
            borderless=1,
            activebackground="#6eb897",
            activeforeground="#FFFFFF",
            command=lambda: master.playAgain()
        ).pack()

        # Exit button
        Button(self,
            text="Exit",
            bg="#ADEFD1",
            fg="#00203F",
            borderless=1,
            activebackground="#6eb897",
            activeforeground="#FFFFFF",
            command=lambda: app.destroy()
        ).pack()

class GameOverPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Game over title
        tk.Label(
            self,
            text="Game Over",
            font=("Courier", 44),
            foreground="white",
            background=background_grey
        ).pack()

        # User stats label
        tk.Label(
            self,
            text=f"""
You survived until Round {Game.level}
Your best time was {Game.time}
            """,
            font=("Courier", 18),
            foreground="white",
            background=background_grey
        ).pack()

        # Hiding place message
        tk.Label(
            self,
            text=f"The hiding place was {Game.hidingplace}",
            font=("Courier", 16, "bold"),
            foreground="white",
            background=background_grey
        ).pack()

        # Play again button
        Button(self, text="Play Again?", bg="#ADEFD1",
            fg="#00203F", borderless=1,
            activebackground="#6eb897",
            activeforeground="#FFFFFF",
            command=lambda: master.playAgain(False, True)
            ).pack()

        # Exit button
        Button(self,
            text="Exit",
            bg="#ADEFD1",
            fg="#00203F",
            borderless=1,
            activebackground="#6eb897",
            activeforeground="#FFFFFF",
            command=lambda: app.destroy()
        ).pack()

app = App()
app.mainloop()

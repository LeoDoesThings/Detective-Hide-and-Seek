import tkinter as tk
from tkinter import PhotoImage
import platform
import random


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

# Windows font size is bigger by around 25% so make text smaller
# if running on Windows
if platform.system() == "Windows":
    h1 = 38
    h2 = 26
    h3 = 18
    h4 = 14
    h5 = 12
    h6 = 8
else:
    h1 = 54
    h2 = 36
    h3 = 24
    h4 = 18
    h5 = 16
    h6 = 10


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Set tkinter window settings
        self.title("Detective Hide and Seek")
        self.configure(bg=background_grey)

        # Set window size to 480p
        self.geometry("853x480")

        # Start the game on the starting page
        self._frame = None
        self.switch_frame(StartPage)

        # Timer settings
        self.remaining = 0
        self.timerlabel = tk.Label(self, text="", width=10)

        # Must set this variable in __init__ before using
        self.playerwon = None

    def switch_frame(self, frame_class):
        # Forget the old frame and pack the new frame
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.pack_forget()
            self._frame.place_forget()
        self._frame = new_frame
        self._frame.pack()

    def playAgain(self, levelup=True, reset=False):
        if levelup is True:
            # Player level up
            Game.level += 1
            Game.time -= 5
            if Game.cluechance > 1:
                # Lower chances of clue
                Game.cluechance -= 1
        if reset is True:
            # Do this for full game reset
            Game.level = 1
            Game.time = 60
        # Reset game ready for next round
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

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        # The player can still win if they get it just in time before 0
        if self.remaining <= 0:
            self.timerlabel.pack_forget()
            if self.playerwon is False:
                self.switch_frame(GameOverPage)
            else:
                self.switch_frame(YouWinPage)
        else:
            # Update timer every second with the new second value
            self.timerlabel.pack(side="top", anchor="ne")
            self.timerlabel.configure(
                text="Time: %d" % self.remaining,
                font=("Courier", h3, "bold"),
                fg="#FFF",
                bg=background_grey
            )
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=background_grey)

        main_title = tk.Label(
            self,
            text="Detective Hide and Seek",
            font=("Courier", h1, "bold"),
            fg="#FFF",
            bg=background_grey
        )
        main_title.grid(column=1, columnspan=2, pady=10)

        # Start button
        self.start_image = PhotoImage(file="resources/start.png")
        tk.Button(self,
                  image=self.start_image,
                  highlightthickness=0,
                  bd=0,
                  command=lambda: master.playAgain(False)
                  ).grid(row=2, column=1, rowspan=2, pady=120)

        # Exit button
        self.exit_image = PhotoImage(file="resources/exit.png")
        tk.Button(self,
                  image=self.exit_image,
                  highlightthickness=0,
                  bd=0,
                  command=lambda: app.destroy()
                  ).grid(row=3, column=1)

        # Brief description of how to play
        tk.Label(
            self,
            text="""
You are the Detective. You need to catch the criminal before he escapes!


You'll have 60 seconds, otherwise the criminal is home free.


The criminal might leave clues behind in certain locations that you'll have to find if you want to catch him in time.

But don't get too confident!
The criminal will learn from his mistakes and won't leave as many clues the next time you try to catch him.
            """,
            font=("Courier", h5),
            fg="#FFF",
            bg=background_grey,
            wraplength=windowWidth-300
        ).grid(row=2, column=2, rowspan=3, pady=40)

        tk.Label(
            self,
            text="Apple Color Emoji are Copyright (c) Apple Inc.",
            font=("Courier", h6),
            fg="#FFF",
            bg=background_grey,
        ).grid(row=4, column=2, sticky="se")


class MapPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=background_grey)

        # Save the location being searched before switching to the
        # searching page
        def searchLocation(location):
            Game.searching = location
            master.switch_frame(SearchingPage)

        print(Game.hidingplace)
        # Map title
        tk.Label(self,
                 text="Map",
                 font=("Courier", h1, "bold"),
                 borderwidth=0,
                 highlightthickness=0,
                 fg="#FFF",
                 bg=background_grey
                 ).grid(row=1, column=2)

        # Forest button
        self.forest_image = PhotoImage(file="resources/img0.png")
        forest = tk.Button(self,
                           image=self.forest_image,
                           highlightthickness=0,
                           bd=0,
                           command=lambda: searchLocation("forest")
                           )
        if "forest" not in locations.searched:
            forest.grid(row=4, column=1)

        # Park button
        self.park_image = PhotoImage(file="resources/img1.png")
        park = tk.Button(self,
                         image=self.park_image,
                         highlightthickness=0,
                         bd=0,
                         command=lambda: searchLocation("park")
                         )
        if "park" not in locations.searched:
            park.grid(row=4, column=2)

        # Cafe button
        self.cafe_image = PhotoImage(file="resources/img2.png")
        cafe = tk.Button(self,
                         image=self.cafe_image,
                         highlightthickness=0,
                         bd=0,
                         command=lambda: searchLocation("cafe")
                         )
        if "cafe" not in locations.searched:
            cafe.grid(row=4, column=3)

        # House button
        self.house_image = PhotoImage(file="resources/img3.png")
        house = tk.Button(self,
                          image=self.house_image,
                          highlightthickness=0,
                          bd=0,
                          command=lambda: searchLocation("house")
                          )
        if "house" not in locations.searched:
            house.grid(row=5, column=1)

        # School button
        self.school_image = PhotoImage(file="resources/img4.png")
        school = tk.Button(self,
                           image=self.school_image,
                           highlightthickness=0,
                           bd=0,
                           command=lambda: searchLocation("school")
                           )
        if "school" not in locations.searched:
            school.grid(row=5, column=2)

        # Garden button
        self.garden_image = PhotoImage(file="resources/img5.png")
        garden = tk.Button(self,
                           image=self.garden_image,
                           highlightthickness=0,
                           bd=0,
                           command=lambda: searchLocation("garden")
                           )
        if "garden" not in locations.searched:
            garden.grid(row=5, column=3)


class SearchingPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=background_grey)

        # Searching title message
        tk.Label(
            self,
            text="Searching...",
            font=("Courier", h2),
            borderwidth=0,
            highlightthickness=0,
            fg="#FFF",
            bg=background_grey
        ).pack()

        self.remaining = 0
        self.timerlabel = tk.Label(self, text="", width=10)

        # Start the countdown with random searching time
        searchingtime = random.randrange(8, 14)
        self.countdown(searchingtime)

        # Check timer is still running before finishing the search
        # otherwise it override the switch to GameOverPage
        def finishSearch():
            if master.remaining > 0:
                master.switch_frame(MapPage)

        if Game.searching == Game.hidingplace:
            # Clue variable must have something otherwise script returns an error sometimes
            self.clue = False
            waittime = random.randrange(4, searchingtime-1)
            self.after(waittime*1000, master.playerFinished, True)
        else:
            # Show a clue if the location is not the hiding place
            self.clue = Game.getClue(Game.hidingplace)
            self.after(searchingtime*1000, finishSearch)

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining == 3 and Game.searching != Game.hidingplace:
            # Either show a clue or tell user there is no clue
            if self.clue is False:
                tk.Label(
                    self,
                    text="You come up empty.",
                    font=("Courier", h4),
                    borderwidth=0,
                    highlightthickness=0,
                    fg="#FFF",
                    bg=background_grey
                ).pack(side="top", pady=5)
            else:
                tk.Label(
                    self,
                    text=f"You notice {self.clue}",
                    font=("Courier", h4),
                    borderwidth=0,
                    highlightthickness=0,
                    fg="#FFF",
                    bg=background_grey
                ).pack(side="top", pady=5)

        if self.remaining <= 0:
            self.timerlabel.pack_forget()
        else:
            # Update the timer every second
            self.timerlabel.pack()
            self.timerlabel.configure(
                text="%d" % self.remaining,
                font=("Courier", h3, "bold"),
                fg="#FFF",
                borderwidth=0,
                highlightthickness=0,
                bg=background_grey
            )
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)


class YouWinPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=background_grey)

        roundnum = Game.level
        # You Win title message
        tk.Label(
            self,
            text="You Win!",
            font=("Courier", h1, "bold"),
            foreground="white",
            background=background_grey
        ).pack(pady=(40, 0))

        # Round complete message
        tk.Label(
            self,
            text=f"Round {roundnum}: Complete",
            font=("Courier", h4),
            foreground="white",
            background=background_grey
        ).pack()

        # Exit button
        self.exit_image = PhotoImage(file="resources/exit2.png")
        tk.Button(self,
                  image=self.exit_image,
                  highlightthickness=0,
                  bd=0,
                  command=lambda: app.destroy()
                  ).pack(side="left", pady=80)

        # Play next round button
        self.nextround_image = PhotoImage(file=f"resources/playround{roundnum+1}.png")
        tk.Button(self,
                  image=self.nextround_image,
                  highlightthickness=0,
                  bd=0,
                  command=lambda: master.playAgain()
                  ).pack(side="left")

class GameOverPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=background_grey)

        # Game over title
        tk.Label(
            self,
            text="Game Over",
            font=("Courier", h1, "bold"),
            foreground="white",
            background=background_grey
        ).pack()

        # User stats label
        tk.Label(
            self,
            text=f"""
You survived until Round {Game.level}
Your best time was {Game.time} seconds
            """,
            font=("Courier", h4),
            foreground="white",
            background=background_grey
        ).pack()

        # Hiding place message
        tk.Label(
            self,
            text=f"The hiding place was {Game.hidingplace}",
            font=("Courier", h5, "bold"),
            foreground="white",
            background=background_grey
        ).pack()

        # Exit button
        self.exit_image = PhotoImage(file="resources/exit2.png")
        tk.Button(self,
                  image=self.exit_image,
                  highlightthickness=0,
                  bd=0,
                  command=lambda: app.destroy()
                  ).pack(side="left", pady=80)

        # Play next round button
        self.playagain_image = PhotoImage(file="resources/playagain.png")
        tk.Button(self,
                  image=self.playagain_image,
                  highlightthickness=0,
                  bd=0,
                  command=lambda: master.playAgain(False, True)
                  ).pack(side="left")


app = App()
app.eval('tk::PlaceWindow . center')
app.mainloop()

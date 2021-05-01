import tkinter as tk
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

    school [
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


class Game:
    difficulty = 1

    def getHidingPlace():
        hidingplace = random.choice(Locations.locations)
        print(hidingplace)


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        main_title_label = tk.Label(
            text='Detective Hide and Seek',
            foreground="white",
            background="#3b3b3b"
        )
        main_title_label.place()
        main_title_label.pack(side="top")

        start_button = tk.Button(
            text="Start", command=Game.getHidingPlace).pack(side="bottom")
        test_button = tk.Button(
            text="testing button", command=print(Clues.park[3])).pack(side="bottom")


root = tk.Tk()
root.title('Detective Hide and Seek')

# Set window size to 480p
root.geometry('853x480')
# Gets the requested values of the height and width
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
print("Width", windowWidth, "Height", windowHeight)
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/3 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/3 - windowHeight/2)
# Positions the window in the center of the page
root.geometry("+{}+{}".format(positionRight, positionDown))

app = App(master=root)
app.mainloop()

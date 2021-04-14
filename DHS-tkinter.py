import tkinter as tk


class Locations:
    locations = ['forest', 'park', 'cafe', 'house', 'school', 'garden', 'chapel']
    searched = []

    def location_searched(self, location):
        self.searched.append(location)

class Clues:
    seen = []

    forest1 = 'You notice a muddy footprint on the ground...'
    forest2 = 'You notice some dirt on the pavement...'
    forest3 = 'You notice a stick on the ground...'
    forest4 = 'You notice a leaf blowing past you...'

    park1 = 'You notice a branch on the ground...'
    park2 = 'You notice a stick on the ground...'
    park3 = ''
    park4 = ''

    cafe1 = 'You notice a coffee cup on the ground...'
    cafe2 = 'You notice a lid on the ground...'
    cafe3 = 'You notice some liquid on the ground...'
    cafe4 = 'You notice some drops on the ground...'

    house1 = ''
    house2 = ''
    house3 = ''
    house4 = ''

    school1 = ''
    school2 = ''
    school3 = ''
    school4 = ''

    garden1 = ''
    garden2 = ''
    garden3 = ''
    garden4 = ''

    chapel1 = ''
    chapel2 = ''
    chapel3 = ''
    chapel4 = ''

class Application(tk.Frame):
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


root = tk.Tk()
root.title('Detective Hide and Seek')

# Set window size to 480p
root.geometry('853x480')
# Gets the requested values of the height and width
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/3 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/3 - windowHeight/2)
# Positions the window in the center of the page
root.geometry("+{}+{}".format(positionRight, positionDown))

app = Application(master=root)
app.mainloop()

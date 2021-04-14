import tkinter as tk


class Locations:
    locations = ['forest', 'park', 'cafe', 'house', 'school', 'garden', 'chapel']
    searched = []

    def location_searched(self, location):
        self.searched.append(location)

class Clues:
    seen = []

    forest1 = 'You notice a muddy footprint on the ground...'
    forest2 = 'some dirt on the pavement'
    forest3 = 'a stick on the ground'
    forest4 = 'a leaf blowing past you'

    park1 = 'a branch on the ground'
    park2 = forest3
    park3 = forest2
    park4 = 'some gardening gloves on the ground'

    cafe1 = 'a coffee cup on the ground'
    cafe2 = 'a lid on the ground'
    cafe3 = 'some liquid on the ground'
    cafe4 = 'some drops on the ground'

    house1 = 'a bag on the ground
    house2 = 'a wallet on the ground'
    house3 = 'a book on the ground'
    house4 = cafe4
    house5 = 'an HP laptop charger on the ground'

    school1 = house3
    school2 = house1
    school3 = cafe3
    school4 = house2
    school5 = house5

    garden1 = 'some gardening gloves on the ground'
    garden2 = 'a stick on the ground'
    garden3 = forest2
    garden4 = ''

    chapel1 = 'a rosary on the ground'
    chapel2 = school1
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

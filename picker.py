import random
from tkinter import *



episodes = ["S1E1 - Rose",
            "S1E2 - The End of the World",
            "S1E3 - The Unquiet Dead",
            "S1E4 - Aliens of London",
            "S1E5 - World War Three",
            "S1E6 - Dalek",
            "S1E7 - The Long Game",
            "S1E8 - Father's Day",
            "S1E9 - The Empty Child",
            "S1E10 - The Doctor Dances",
            "S1E11 - Boom Town",
            "S1E12 - Bad Wolf",
            "S1E13 - The Parting of the Ways",
            ]


root = Tk()
root.title("Doctor Who Episode Generator")
root.geometry("800x400")

episode_label = Label(root, text=random.choice(episodes))

episode_label.pack()

root.mainloop()
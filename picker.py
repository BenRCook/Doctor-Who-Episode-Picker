import random
from tkinter import *


def pick_episode():
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
    return random.choice(episodes)

def pick_episode_button():
    episode_label["text"] = pick_episode()

root = Tk()
root.title("Doctor Who Episode Generator")
root.geometry("800x400")
root.configure(bg="#17163e")
episode_label = Label(root, text=pick_episode())
episode_label.pack()

new_episode_button = Button(text="Pick New Episode", command=pick_episode_button, padx = 10, pady = 20)
new_episode_button.pack(pady=10)


root.mainloop()
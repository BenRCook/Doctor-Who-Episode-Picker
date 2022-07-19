import random
import json
from tkinter import *

episodes_json = """[
    {
        "series": 1,
        "episode": 1,
        "title": "Rose",
        "doctor": 9
    },
    {
        "series": 1,
        "episode": 2,
        "title": "The End of the World",
        "doctor": 9
    },
    {
        "series": 1,
        "episode": 3,
        "title": "The Unquiet Dead",
        "doctor": 9
    },
    {
        "series": 1,
        "episode": 4,
        "title": "Aliens of London",
        "doctor": 9
    },
    {
        "series": 1,
        "episode": 5,
        "title": "World War Three",
        "doctor": 9
    },
    {
        "series": 1,
        "episode": 6,
        "title": "Dalek",
        "doctor": 9
    },
    {
        "series": 1,
        "episode": 7,
        "title": "The Long Game",
        "doctor": 9
    },
    {
        "series": 1,
        "episode": 8,
        "title": "Father's Day",
        "doctor": 9
    },
    {
        "series": 1,
        "episode": 9,
        "title": "The Empty Child",
        "doctor": 9
    },
    {
        "series": 1,
        "episode": 10,
        "title": "The Doctor Dances",
        "doctor": 9
    },
    {
        "series": 1,
        "episode": 11,
        "title": "Boom Town",
        "doctor": 9
    },
    {
        "series": 1,
        "episode": 12,
        "title": "Bad Wolf",
        "doctor": 9
    },
    {
        "series": 1,
        "episode": 13,
        "title": "The Parting of the Ways",
        "doctor": 9
    },
    {
        "series": 2,
        "episode": 1,
        "title": "The Christmas Invasion",
        "doctor": 10
    },
    {
        "series": 2,
        "episode": 2,
        "title": "New Earth",
        "doctor": 10
    },
    {
        "series": 2,
        "episode": 3,
        "title": "Tooth and Claw",
        "doctor": 10
    },
    {
        "series": 2,
        "episode": 4,
        "title": "School Reunion",
        "doctor": 10
    },
    {
        "series": 2,
        "episode": 5,
        "title": "The Girl in the Fireplace",
        "doctor": 10
    },
    {
        "series": 2,
        "episode": 6,
        "title": "Rise of the Cybermen",
        "doctor": 10
    },
    {
        "series": 2,
        "episode": 7,
        "title": "The Age of Steel",
        "doctor": 10
    },
    {
        "series": 2,
        "episode": 8,
        "title": "The Idiot's Lantern",
        "doctor": 10
    },
    {
        "series": 2,
        "episode": 9,
        "title": "The Impossible Planet",
        "doctor": 10
    },
    {
        "series": 2,
        "episode": 10,
        "title": "The Satan Pit",
        "doctor": 10
    },
    {
        "series": 2,
        "episode": 11,
        "title": "Love & Monsters",
        "doctor": 10
    },
    {
        "series": 2,
        "episode": 12,
        "title": "Fear Her",
        "doctor": 10
    },
    {
        "series": 2,
        "episode": 13,
        "title": "Army of Ghosts",
        "doctor": 10
    },
    {
        "series": 2,
        "episode": 14,
        "title": "Doomsday",
        "doctor": 10
    },
    {
        "series": 3,
        "episode": 1,
        "title": "The Runaway Bride",
        "doctor": 10
    },
    {
        "series": 3,
        "episode": 2,
        "title": "Smith and Jones",
        "doctor": 10
    },
    {
        "series": 3,
        "episode": 3,
        "title": "The Shakespeare Code",
        "doctor": 10
    },
    {
        "series": 3,
        "episode": 4,
        "title": "Gridlock",
        "doctor": 10
    },
    {
        "series": 3,
        "episode": 5,
        "title": "Daleks in Manhattan",
        "doctor": 10
    },
    {
        "series": 3,
        "episode": 6,
        "title": "Evolution of the Daleks",
        "doctor": 10
    },
    {
        "series": 3,
        "episode": 7,
        "title": "The Lazarus Experiment",
        "doctor": 10
    },
    {
        "series": 3,
        "episode": 8,
        "title": "42",
        "doctor": 10
    },
    {
        "series": 3,
        "episode": 9,
        "title": "Human Nature",
        "doctor": 10
    },
    {
        "series": 3,
        "episode": 10,
        "title": "The Family of Blood",
        "doctor": 10
    },
    {
        "series": 3,
        "episode": 11,
        "title": "Blink",
        "doctor": 10
    },
    {
        "series": 3,
        "episode": 12,
        "title": "Utopia",
        "doctor": 10
    },
    {
        "series": 3,
        "episode": 13,
        "title": "The Sound of Drums",
        "doctor": 10
    },
    {
        "series": 3,
        "episode": 14,
        "title": "Last of the Time Lords",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 1,
        "title": "Voyage of the Damned",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 2,
        "title": "Partners in Crime",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 3,
        "title": "The Fires of Pompeii",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 4,
        "title": "Planet of the Ood",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 5,
        "title": "The Sontaran Stratagem",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 6,
        "title": "The Poison Sky",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 7,
        "title": "The Doctor's Daughter",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 8,
        "title": "The Unicorn and the Wasp",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 9,
        "title": "Silence in the Library",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 10,
        "title": "Forest of the Dead",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 11,
        "title": "Midnight",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 12,
        "title": "Turn Left",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 13,
        "title": "The Stolen Earth",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 14,
        "title": "Journey's End",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 15,
        "title": "The Next Doctor",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 16,
        "title": "Planet of the Dead",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 17,
        "title": "The Waters of Mars",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 18,
        "title": "The End of Time Part One",
        "doctor": 10
    },
    {
        "series": 4,
        "episode": 19,
        "title": "The End of Time Part Two",
        "doctor": 10
    },
    {
        "series": 5,
        "episode": 1,
        "title": "The Eleventh Hour",
        "doctor": 11
    },
    {
        "series": 5,
        "episode": 2,
        "title": "The Beast Below",
        "doctor": 11
    },
    {
        "series": 5,
        "episode": 3,
        "title": "Victory of the Daleks",
        "doctor": 11
    },
    {
        "series": 5,
        "episode": 4,
        "title": "The Time of Angels",
        "doctor": 11
    },
    {
        "series": 5,
        "episode": 5,
        "title": "Flesh and Stone",
        "doctor": 11
    },
    {
        "series": 5,
        "episode": 6,
        "title": "The Vampires of Venice",
        "doctor": 11
    },
    {
        "series": 5,
        "episode": 7,
        "title": "Amy's Choice",
        "doctor": 11
    },
    {
        "series": 5,
        "episode": 8,
        "title": "The Hungry Earth",
        "doctor": 11
    },
    {
        "series": 5,
        "episode": 9,
        "title": "Cold Blood",
        "doctor": 11
    },
    {
        "series": 5,
        "episode": 10,
        "title": "Vincent and the Doctor",
        "doctor": 11
    },
    {
        "series": 5,
        "episode": 11,
        "title": "The Lodger",
        "doctor": 11
    },
    {
        "series": 5,
        "episode": 12,
        "title": "The Pandorica Opens",
        "doctor": 11
    },
    {
        "series": 5,
        "episode": 13,
        "title": "The Big Bang",
        "doctor": 11
    },
    {
        "series": 6,
        "episode": 1,
        "title": "A Christmas Carol",
        "doctor": 11
    },
    {
        "series": 6,
        "episode": 2,
        "title": "The Impossible Astronaut",
        "doctor": 11
    },
    {
        "series": 6,
        "episode": 3,
        "title": "Day of the Moon",
        "doctor": 11
    },
    {
        "series": 6,
        "episode": 4,
        "title": "The Curse of the Black Spot",
        "doctor": 11
    },
    {
        "series": 6,
        "episode": 5,
        "title": "The Doctor's Wife",
        "doctor": 11
    },
    {
        "series": 6,
        "episode": 6,
        "title": "The Rebel Flesh",
        "doctor": 11
    },
    {
        "series": 6,
        "episode": 7,
        "title": "The Almost People",
        "doctor": 11
    },
    {
        "series": 6,
        "episode": 8,
        "title": "A Good Man Goes to War",
        "doctor": 11
    },
    {
        "series": 6,
        "episode": 9,
        "title": "Let's Kill Hitler",
        "doctor": 11
    },
    {
        "series": 6,
        "episode": 10,
        "title": "Night Terrors",
        "doctor": 11
    },
    {
        "series": 6,
        "episode": 11,
        "title": "The Girl Who Waited",
        "doctor": 11
    },
    {
        "series": 6,
        "episode": 12,
        "title": "The God Complex",
        "doctor": 11
    },
    {
        "series": 6,
        "episode": 13,
        "title": "Closing Time",
        "doctor": 11
    },
    {
        "series": 6,
        "episode": 14,
        "title": "The Wedding of River Song",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 1,
        "title": "The Doctor, the Widow and the Wardrobe",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 2,
        "title": "Asylum of the Daleks",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 3,
        "title": "Dinosaurs on a Spaceship",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 4,
        "title": "A Town Called Mercy",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 5,
        "title": "The Power of Three",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 6,
        "title": "The Angels Take Manhattan",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 7,
        "title": "The Snowmen",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 8,
        "title": "The Bells of Saint John",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 9,
        "title": "The Rings of Akhaten",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 10,
        "title": "Cold War",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 11,
        "title": "Hide",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 12,
        "title": "Journey to the Centre of the TARDIS",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 13,
        "title": "Journey to the Centre of the TARDIS",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 14,
        "title": "The Crimson Horror",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 15,
        "title": "Nightmare in Silver",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 16,
        "title": "The Name of the Doctor",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 17,
        "title": "The Day of the Doctor",
        "doctor": 11
    },
    {
        "series": 7,
        "episode": 18,
        "title": "The Time of the Doctor",
        "doctor": 11
    }
]
"""
episodes = json.loads(episodes_json)
print(episodes)

def pick_episode():
    episode = random.choice(episodes)
    return episode

def pick_episode_button():
    episode = pick_episode()
    title_label["text"] = "S%s E%s - %s" %(episode["series"], episode["episode"], episode["title"])
    doctor_label["text"] = "%sth Doctor" % episode["doctor"]
    

root = Tk()
root.title("Doctor Who Episode Generator")
root.geometry("600x250")
root.configure(bg="#17163e")
title_label = Label(root, text="", font=("Helvetica", 20))
title_label.pack(pady=10, padx=10)
doctor_label = Label(root, text="", font=("Helvetica", 15))
doctor_label.pack(pady=30, padx=30)
pick_episode_button() # picks an episode  

new_episode_button = Button(text="Pick New Episode", command=pick_episode_button, font=("Helvetica", 15), padx = 10, pady = 20)
new_episode_button.pack(pady=10)


root.mainloop()
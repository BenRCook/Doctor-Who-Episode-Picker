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
    },
    {
        "series": 8,
        "episode": 1,
        "title": "Deep Breath",
        "doctor": 12
    },
    {
        "series": 8,
        "episode": 2,
        "title": "Into the Dalek",
        "doctor": 12
    },
    {
        "series": 8,
        "episode": 3,
        "title": "Robot of Sherwood",
        "doctor": 12
    },
    {
        "series": 8,
        "episode": 4,
        "title": "Listen",
        "doctor": 12
    },
    {
        "series": 8,
        "episode": 5,
        "title": "Time Heist",
        "doctor": 12
    },
    {
        "series": 8,
        "episode": 6,
        "title": "The Caretaker",
        "doctor": 12
    },
    {
        "series": 8,
        "episode": 7,
        "title": "Kill the Moon",
        "doctor": 12
    },
    {
        "series": 8,
        "episode": 8,
        "title": "Mummy on the Orient Express",
        "doctor": 12
    },
    {
        "series": 8,
        "episode": 9,
        "title": "Flatline",
        "doctor": 12
    },
    {
        "series": 8,
        "episode": 10,
        "title": "In the Forest of the Night",
        "doctor": 12
    },
    {
        "series": 8,
        "episode": 11,
        "title": "Dark Water",
        "doctor": 12
    },
    {
        "series": 8,
        "episode": 12,
        "title": "Death in Heaven",
        "doctor": 12
    },
    {
        "series": 9,
        "episode": 1,
        "title": "Last Christmas",
        "doctor": 12
    },
    {
        "series": 9,
        "episode": 2,
        "title": "The Magician's Apprentice",
        "doctor": 12
    },
    {
        "series": 9,
        "episode": 3,
        "title": "The Witch's Familiar",
        "doctor": 12
    },
    {
        "series": 9,
        "episode": 4,
        "title": "Under the Lake",
        "doctor": 12
    },
    {
        "series": 9,
        "episode": 5,
        "title": "Before the Flood",
        "doctor": 12
    },
    {
        "series": 9,
        "episode": 6,
        "title": "The Girl Who Died",
        "doctor": 12
    },
    {
        "series": 9,
        "episode": 7,
        "title": "The Woman Who Lived",
        "doctor": 12
    },
    {
        "series": 9,
        "episode": 8,
        "title": "The Zygon Invasion",
        "doctor": 12
    },
    {
        "series": 9,
        "episode": 9,
        "title": "The Zygon Inversion",
        "doctor": 12
    },
    {
        "series": 9,
        "episode": 10,
        "title": "Sleep No More",
        "doctor": 12
    },
    {
        "series": 9,
        "episode": 11,
        "title": "Face the Raven",
        "doctor": 12
    },
    {
        "series": 9,
        "episode": 12,
        "title": "Heaven Sent",
        "doctor": 12
    },
    {
        "series": 9,
        "episode": 13,
        "title": "Hell Bent",
        "doctor": 12
    },
    {
        "series": 9,
        "episode": 14,
        "title": "The Husbands of River Song",
        "doctor": 12
    },
    {
        "series": 10,
        "episode": 1,
        "title": "The Return of Doctor Mysterio",
        "doctor": 12
    },
    {
        "series": 10,
        "episode": 2,
        "title": "The Pilot",
        "doctor": 12
    },
    {
        "series": 10,
        "episode": 3,
        "title": "Smile",
        "doctor": 12
    },
    {
        "series": 10,
        "episode": 4,
        "title": "Thin Ice",
        "doctor": 12
    },
    {
        "series": 10,
        "episode": 5,
        "title": "Knock Knock",
        "doctor": 12
    },
    {
        "series": 10,
        "episode": 6,
        "title": "Oxygen",
        "doctor": 12
    },
    {
        "series": 10,
        "episode": 7,
        "title": "Extremis",
        "doctor": 12
    },
    {
        "series": 10,
        "episode": 8,
        "title": "The Pyramid at the End of the World",
        "doctor": 12
    },
    {
        "series": 10,
        "episode": 9,
        "title": "The Lie of the Land",
        "doctor": 12
    },
    {
        "series": 10,
        "episode": 10,
        "title": "Empress of Mars",
        "doctor": 12
    },
    {
        "series": 10,
        "episode": 11,
        "title": "The Eaters of Light",
        "doctor": 12
    },
    {
        "series": 10,
        "episode": 12,
        "title": "World Enough and Time",
        "doctor": 12
    },
    {
        "series": 10,
        "episode": 13,
        "title": "The Doctor Falls",
        "doctor": 12
    },
    {
        "series": 10,
        "episode": 14,
        "title": "Twice Upon a Time",
        "doctor": 12
    },
    {
        "series": 11,
        "episode": 1,
        "title": "The Woman Who Fell to Earth",
        "doctor": 13
    },
    {
        "series": 11,
        "episode": 2,
        "title": "The Ghost Monument",
        "doctor": 13
    },
    {
        "series": 11,
        "episode": 3,
        "title": "Rosa",
        "doctor": 13
    },
    {
        "series": 11,
        "episode": 4,
        "title": "Arachnids in the UK",
        "doctor": 13
    },
    {
        "series": 11,
        "episode": 5,
        "title": "The Tsuranga Conundrum",
        "doctor": 13
    },
    {
        "series": 11,
        "episode": 6,
        "title": "Demons of the Punjab",
        "doctor": 13
    },
    {
        "series": 11,
        "episode": 7,
        "title": "Kerblam!",
        "doctor": 13
    },
    {
        "series": 11,
        "episode": 8,
        "title": "The Witchfinders",
        "doctor": 13
    },
    {
        "series": 11,
        "episode": 9,
        "title": "It Takes You Away",
        "doctor": 13
    },
    {
        "series": 11,
        "episode": 10,
        "title":"The Battle of Ranskoor Av Kolos",
        "doctor": 13
    },
    {
        "series": 11,
        "episode": 11,
        "title": "Resolution",
        "doctor": 13
    },
    {
        "series": 12,
        "episode": 1,
        "title": "Spyfall Part 1",
        "doctor": 13
    },
    {
        "series": 12,
        "episode": 2,
        "title": "Spyfall Part 2",
        "doctor": 13
    },
    {
        "series": 12,
        "episode": 3,
        "title": "Orphan 55",
        "doctor": 13
    },
    {
        "series": 12,
        "episode": 4,
        "title": "Nikola Tesla's Night of Terror",
        "doctor": 13
    },
    {
        "series": 12,
        "episode": 5,
        "title": "Fugitive of the Judoon",
        "doctor": 13
    },
    {
        "series": 12,
        "episode": 6,
        "title": "Praxeus",
        "doctor": 13
    },
    {
        "series": 12,
        "episode": 7,
        "title": "Can You Hear Me?",
        "doctor": 13
    },
    {
        "series": 12,
        "episode": 8,
        "title": "The Haunting of Villa Diodati",
        "doctor": 13
    },
    {
        "series": 12,
        "episode": 9,
        "title": "Ascension of the Cybermen",
        "doctor": 13
    },
    {
        "series": 12,
        "episode": 10,
        "title": "The Timeless Children",
        "doctor": 13
    },
    {
        "series": 12,
        "episode": 11,
        "title": "Revolution of the Daleks",
        "doctor": 13
    },
    {
        "series": 13,
        "episode": 1,
        "title": "The Halloween Apocalypse",
        "doctor": 13
    },
    {
        "series": 13,
        "episode": 2,
        "title": "War of the Sontarans",
        "doctor": 13
    },
    {
        "series": 13,
        "episode": 3,
        "title": "Once, Upon Time",
        "doctor": 13
    },
    {
        "series": 13,
        "episode": 4,
        "title": "Village of the Angels",
        "doctor": 13
    },
    {
        "series": 13,
        "episode": 5,
        "title": "Survivors of the Flux",
        "doctor": 13
    },
    {
        "series": 13,
        "episode": 6,
        "title": "The Vanquishers",
        "doctor": 13
    },
    {
        "series": 13,
        "episode": 7,
        "title": "Eve of the Daleks",
        "doctor": 13
    },
    {
        "series": 13,
        "episode": 8,
        "title": "Legend of the Sea Devils",
        "doctor": 13
    }
    
]
"""
episodes = json.loads(episodes_json)

def pick_episode():
    episode = random.choice(episodes)
    return episode

def pick_episode_button():
    episode = pick_episode()
    title_label["text"] = "S%s E%s - %s" %(episode["series"], episode["episode"], episode["title"])
    doctor_label["text"] = "%sth Doctor" % episode["doctor"]

    bg_colours = {
        9 : "#423120", # colour taken from 9's tardis
        10 : "#000b79", # colour taken from 10's screwdriver
        11: "#0f3318", # colour taken from 11's screwdriver
        12: "#575654", # colour taken from 12's hair
        13: "#4d3438" # colour taken from 13's screwdriver
    }
    root["bg"] = bg_colours[episode["doctor"]]
    
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
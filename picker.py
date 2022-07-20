from faulthandler import disable
import random
import json
from tkinter import *

episodes_json = """[
    {
        "series": 1,
        "episode": 1,
        "title": "Rose",
        "doctor": 9,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074dlv"
    },
    {
        "series": 1,
        "episode": 2,
        "title": "The End of the World",
        "doctor": 9,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074dmp"
    },
    {
        "series": 1,
        "episode": 3,
        "title": "The Unquiet Dead",
        "doctor": 9,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074dng"
    },
    {
        "series": 1,
        "episode": 4,
        "title": "Aliens of London",
        "doctor": 9,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074dp9"
    },
    {
        "series": 1,
        "episode": 5,
        "title": "World War Three",
        "doctor": 9,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074dpv"
    },
    {
        "series": 1,
        "episode": 6,
        "title": "Dalek",
        "doctor": 9,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074dq8"
    },
    {
        "series": 1,
        "episode": 7,
        "title": "The Long Game",
        "doctor": 9,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074dr5"
    },
    {
        "series": 1,
        "episode": 8,
        "title": "Father's Day",
        "doctor": 9,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074drw"
    },
    {
        "series": 1,
        "episode": 9,
        "title": "The Empty Child",
        "doctor": 9,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074ds9"
    },
    {
        "series": 1,
        "episode": 10,
        "title": "The Doctor Dances",
        "doctor": 9,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074dsp"
    },
    {
        "series": 1,
        "episode": 11,
        "title": "Boom Town",
        "doctor": 9,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074dt5"
    },
    {
        "series": 1,
        "episode": 12,
        "title": "Bad Wolf",
        "doctor": 9,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074dth"
    },
    {
        "series": 1,
        "episode": 13,
        "title": "The Parting of the Ways",
        "doctor": 9,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074dv1"
    },
    {
        "series": 2,
        "episode": 1,
        "title": "The Christmas Invasion",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074f9p"
    },
    {
        "series": 2,
        "episode": 2,
        "title": "New Earth",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074fll"
    },
    {
        "series": 2,
        "episode": 3,
        "title": "Tooth and Claw",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074fly"
    },
    {
        "series": 2,
        "episode": 4,
        "title": "School Reunion",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074fm7"
    },
    {
        "series": 2,
        "episode": 5,
        "title": "The Girl in the Fireplace",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074fmn"
    },
    {
        "series": 2,
        "episode": 6,
        "title": "Rise of the Cybermen",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074fn1"
    },
    {
        "series": 2,
        "episode": 7,
        "title": "The Age of Steel",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074fnh"
    },
    {
        "series": 2,
        "episode": 8,
        "title": "The Idiot's Lantern",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074fnv"
    },
    {
        "series": 2,
        "episode": 9,
        "title": "The Impossible Planet",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074gfz"
    },
    {
        "series": 2,
        "episode": 10,
        "title": "The Satan Pit",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074fpm"
    },
    {
        "series": 2,
        "episode": 11,
        "title": "Love & Monsters",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074fpz"
    },
    {
        "series": 2,
        "episode": 12,
        "title": "Fear Her",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074fqf"
    },
    {
        "series": 2,
        "episode": 13,
        "title": "Army of Ghosts",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074fqz"
    },
    {
        "series": 2,
        "episode": 14,
        "title": "Doomsday",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074frg"
    },
    {
        "series": 3,
        "episode": 1,
        "title": "The Runaway Bride",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074g6q"
    },
    {
        "series": 3,
        "episode": 2,
        "title": "Smith and Jones",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074gly"
    },
    {
        "series": 3,
        "episode": 3,
        "title": "The Shakespeare Code",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074gmy"
    },
    {
        "series": 3,
        "episode": 4,
        "title": "Gridlock",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074gnr"
    },
    {
        "series": 3,
        "episode": 5,
        "title": "Daleks in Manhattan",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0079mgg"
    },
    {
        "series": 3,
        "episode": 6,
        "title": "Evolution of the Daleks",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0079t3d"
    },
    {
        "series": 3,
        "episode": 7,
        "title": "The Lazarus Experiment",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b007ghhb"
    },
    {
        "series": 3,
        "episode": 8,
        "title": "42",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b007hb9s"
    },
    {
        "series": 3,
        "episode": 9,
        "title": "Human Nature",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b007m0r9"
    },
    {
        "series": 3,
        "episode": 10,
        "title": "The Family of Blood",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b007n0d6"
    },
    {
        "series": 3,
        "episode": 11,
        "title": "Blink",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0074gpl"
    },
    {
        "series": 3,
        "episode": 12,
        "title": "Utopia",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b007qltt"
    },
    {
        "series": 3,
        "episode": 13,
        "title": "The Sound of Drums",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b007r65s"
    },
    {
        "series": 3,
        "episode": 14,
        "title": "Last of the Time Lords",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b007rsj5"
    },
    {
        "series": 4,
        "episode": 1,
        "title": "Voyage of the Damned",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b008lyb2"
    },
    {
        "series": 4,
        "episode": 2,
        "title": "Partners in Crime",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b009w049"
    },
    {
        "series": 4,
        "episode": 3,
        "title": "The Fires of Pompeii",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b009wzbf"
    },
    {
        "series": 4,
        "episode": 4,
        "title": "Planet of the Ood",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00b07kw"
    },
    {
        "series": 4,
        "episode": 5,
        "title": "The Sontaran Stratagem",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00b3z7h"
    },
    {
        "series": 4,
        "episode": 6,
        "title": "The Poison Sky",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00b563l"
    },
    {
        "series": 4,
        "episode": 7,
        "title": "The Doctor's Daughter",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00bbpsb"
    },
    {
        "series": 4,
        "episode": 8,
        "title": "The Unicorn and the Wasp",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00bdjtc"
    },
    {
        "series": 4,
        "episode": 9,
        "title": "Silence in the Library",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00byd29"
    },
    {
        "series": 4,
        "episode": 10,
        "title": "Forest of the Dead",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00c191w"
    },
    {
        "series": 4,
        "episode": 11,
        "title": "Midnight",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00c4xjk"
    },
    {
        "series": 4,
        "episode": 12,
        "title": "Turn Left",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00c7ytx"
    },
    {
        "series": 4,
        "episode": 13,
        "title": "The Stolen Earth",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00cccvg"
    },
    {
        "series": 4,
        "episode": 14,
        "title": "Journey's End",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00cgnjr"
    },
    {
        "series": 4,
        "episode": 15,
        "title": "The Next Doctor",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00gd1mr"
    },
    {
        "series": 4,
        "episode": 16,
        "title": "Planet of the Dead",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00jz2t4"
    },
    {
        "series": 4,
        "episode": 17,
        "title": "The Waters of Mars",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00p05x8"
    },
    {
        "series": 4,
        "episode": 18,
        "title": "The End of Time Part One",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00pk651"
    },
    {
        "series": 4,
        "episode": 19,
        "title": "The End of Time Part Two",
        "doctor": 10,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00pk7ls"
    },
    {
        "series": 5,
        "episode": 1,
        "title": "The Eleventh Hour",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00rs6t7"
    },
    {
        "series": 5,
        "episode": 2,
        "title": "The Beast Below",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00s1wcm"
    },
    {
        "series": 5,
        "episode": 3,
        "title": "Victory of the Daleks",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00s56d2"
    },
    {
        "series": 5,
        "episode": 4,
        "title": "The Time of Angels",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00s8dwd"
    },
    {
        "series": 5,
        "episode": 5,
        "title": "Flesh and Stone",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00s971z"
    },
    {
        "series": 5,
        "episode": 6,
        "title": "The Vampires of Venice",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00sch0s"
    },
    {
        "series": 5,
        "episode": 7,
        "title": "Amy's Choice",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00sfgtp"
    },
    {
        "series": 5,
        "episode": 8,
        "title": "The Hungry Earth",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00sj9sq"
    },
    {
        "series": 5,
        "episode": 9,
        "title": "Cold Blood",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00sm031"
    },
    {
        "series": 5,
        "episode": 10,
        "title": "Vincent and the Doctor",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00spgsf"
    },
    {
        "series": 5,
        "episode": 11,
        "title": "The Lodger",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00sr4bm"
    },
    {
        "series": 5,
        "episode": 12,
        "title": "The Pandorica Opens",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00stv7m"
    },
    {
        "series": 5,
        "episode": 13,
        "title": "The Big Bang",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00sxfc7"
    },
    {
        "series": 6,
        "episode": 1,
        "title": "A Christmas Carol",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b00wyj5p"
    },
    {
        "series": 6,
        "episode": 2,
        "title": "The Impossible Astronaut",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b010tb7q"
    },
    {
        "series": 6,
        "episode": 3,
        "title": "Day of the Moon",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b010y5l3"
    },
    {
        "series": 6,
        "episode": 4,
        "title": "The Curse of the Black Spot",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0110g4b"
    },
    {
        "series": 6,
        "episode": 5,
        "title": "The Doctor's Wife",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b011884d"
    },
    {
        "series": 6,
        "episode": 6,
        "title": "The Rebel Flesh",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b011fnd4"
    },
    {
        "series": 6,
        "episode": 7,
        "title": "The Almost People",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b011lqwt"
    },
    {
        "series": 6,
        "episode": 8,
        "title": "A Good Man Goes to War",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b011rf7y"
    },
    {
        "series": 6,
        "episode": 9,
        "title": "Let's Kill Hitler",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0146h0q"
    },
    {
        "series": 6,
        "episode": 10,
        "title": "Night Terrors",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b014983t"
    },
    {
        "series": 6,
        "episode": 11,
        "title": "The Girl Who Waited",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b014j7x7"
    },
    {
        "series": 6,
        "episode": 12,
        "title": "The God Complex",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b014vy02"
    },
    {
        "series": 6,
        "episode": 13,
        "title": "Closing Time",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b0156hh8"
    },
    {
        "series": 6,
        "episode": 14,
        "title": "The Wedding of River Song",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b015p5kc"
    },
    {
        "series": 7,
        "episode": 1,
        "title": "The Doctor, the Widow and the Wardrobe",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b018nrhp"
    },
    {
        "series": 7,
        "episode": 2,
        "title": "Asylum of the Daleks",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/p00wqr14"
    },
    {
        "series": 7,
        "episode": 3,
        "title": "Dinosaurs on a Spaceship",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b01mm5c9"
    },
    {
        "series": 7,
        "episode": 4,
        "title": "A Town Called Mercy",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b01mxx3h"
    },
    {
        "series": 7,
        "episode": 5,
        "title": "The Power of Three",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b01n2tmc"
    },
    {
        "series": 7,
        "episode": 6,
        "title": "The Angels Take Manhattan",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b01n70f3"
    },
    {
        "series": 7,
        "episode": 7,
        "title": "The Snowmen",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/p011gpsb"
    },
    {
        "series": 7,
        "episode": 8,
        "title": "The Bells of Saint John",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b01rryzz"
    },
    {
        "series": 7,
        "episode": 9,
        "title": "The Rings of Akhaten",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b01rx0lj"
    },
    {
        "series": 7,
        "episode": 10,
        "title": "Cold War",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b01s1cz7"
    },
    {
        "series": 7,
        "episode": 11,
        "title": "Hide",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b01s35ck"
    },
    {
        "series": 7,
        "episode": 12,
        "title": "Journey to the Centre of the TARDIS",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b01s8pn6"
    },
    {
        "series": 7,
        "episode": 13,
        "title": "The Crimson Horror",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b01sfhyp"
    },
    {
        "series": 7,
        "episode": 14,
        "title": "Nightmare in Silver",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b01skfzk"
    },
    {
        "series": 7,
        "episode": 15,
        "title": "The Name of the Doctor",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/b01skh8t"
    },
    {
        "series": 7,
        "episode": 16,
        "title": "The Night of The Doctor",
        "doctor": 8,
        "link": "https://www.bbc.co.uk/iplayer/episode/p01lhhv4"
    },
    {
        "series": 7,
        "episode": 17,
        "title": "The Day of the Doctor",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/p01l1z04"
    },
    {
        "series": 7,
        "episode": 18,
        "title": "The Time of the Doctor",
        "doctor": 11,
        "link": "https://www.bbc.co.uk/iplayer/episode/p01mj6k8"
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
    link_label.delete(0, "end")
    link_label.insert(0, episode["link"])
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
title_label.pack(pady=10)
doctor_label = Label(root, text="", font=("Helvetica", 15))
doctor_label.pack(pady=10)
link_label = Entry(root, width = 40, font=("Helvetica", 12))
link_label.pack(pady=10)

pick_episode_button() # picks an episode  

new_episode_button = Button(text="Pick New Episode", command=pick_episode_button, font=("Helvetica", 15), padx = 10, pady = 20)
new_episode_button.pack(pady=10)


root.mainloop()
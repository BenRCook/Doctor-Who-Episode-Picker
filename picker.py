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
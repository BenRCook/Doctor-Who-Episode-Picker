from faulthandler import disable
import random
import json
from tkinter import *

episodes = json.load(open('episodes.json', 'r'))

def pick_episode():

    episode = random.choice(episodes)
    episode_is_okay = False

    if series_1_var.get() + series_2_var.get() + series_3_var.get() + series_4_var.get() + series_5_var.get() + series_6_var.get() + series_7_var.get() + series_8_var.get() + series_9_var.get() + series_10_var.get() + series_11_var.get() + series_12_var.get() + series_13_var.get() == 0:
        episode_is_okay = True
        episode = {
            "series": 0,
            "episode": 0,
            "title": "Please Select a Series",
            "doctor": 0,
            "link": "https://www.bbc.co.uk/iplayer/episodes/b006q2x0" # link to the general dr who iplayer page

        }

    match episode["series"]:
            case 1 :
                if series_1_var.get() == 1:
                    episode_is_okay = True
            case 2 :
                if series_2_var.get() == 1:
                    episode_is_okay = True
            case 3 :
                if series_3_var.get() == 1:
                    episode_is_okay = True
            case 4 :
                if series_4_var.get() == 1:
                    episode_is_okay = True
            case 5 :
                if series_5_var.get() == 1:
                    episode_is_okay = True
            case 6 :
                if series_6_var.get() == 1:
                    episode_is_okay = True
            case 7 :
                if series_7_var.get() == 1:
                    episode_is_okay = True
            case 8 :
                if series_8_var.get() == 1:
                    episode_is_okay = True
            case 9 :
                if series_9_var.get() == 1:
                    episode_is_okay = True
            case 10 :
                if series_10_var.get() == 1:
                    episode_is_okay = True
            case 11 :
                if series_11_var.get() == 1:
                    episode_is_okay = True
            case 12 :
                if series_12_var.get() == 1:
                    episode_is_okay = True
            case 13 :
                if series_13_var.get() == 1:
                    episode_is_okay = True
    if not episode_is_okay:
        episode = pick_episode()
    return episode

def pick_episode_button_function():
    episode = pick_episode()
    title_label["text"] = "S%s E%s - %s" %(episode["series"], episode["episode"], episode["title"])
    doctor_label["text"] = "%sth Doctor" % episode["doctor"]
    link_label.delete(0, "end")
    link_label.insert(0, episode["link"])
    bg_colours = {
        0: "black",    # this colour is only used if no series is selected
        8: "#0f090a",  # colour taken from 8's coat
        9: "#423120",  # colour taken from 9's tardis
        10: "#000b79", # colour taken from 10's screwdriver
        11: "#0f3318", # colour taken from 11's screwdriver
        12: "#575654", # colour taken from 12's hair
        13: "#4d3438"  # colour taken from 13's screwdriver
    }
    root["bg"] = bg_colours[episode["doctor"]]

def select_all_button_function():
    series_1_var.set(1)
    series_2_var.set(1)
    series_3_var.set(1)
    series_4_var.set(1)
    series_5_var.set(1)
    series_6_var.set(1)
    series_7_var.set(1)
    series_8_var.set(1)
    series_9_var.set(1)
    series_10_var.set(1)
    series_11_var.set(1)
    series_12_var.set(1)
    series_13_var.set(1)

def deselect_all_button_function():
    series_1_var.set(0)
    series_2_var.set(0)
    series_3_var.set(0)
    series_4_var.set(0)
    series_5_var.set(0)
    series_6_var.set(0)
    series_7_var.set(0)
    series_8_var.set(0)
    series_9_var.set(0)
    series_10_var.set(0)
    series_11_var.set(0)
    series_12_var.set(0)
    series_13_var.set(0)

root = Tk()
root.title("Doctor Who Episode Generator")
root.geometry("620x390")
root.configure(bg="#17163e")
title_label = Label(root, text="", font=("Helvetica", 20))
title_label.pack(pady=10)
doctor_label = Label(root, text="", font=("Helvetica", 15))
doctor_label.pack(pady=10)
link_label = Entry(root, width = 40, font=("Helvetica", 12))
link_label.pack(pady=10)

series_frame = LabelFrame(root, text = "Select Series", padx=5, pady=5)
series_frame.pack()
series_1_var = IntVar()
series_1_var.set(1)
series_1_checkbutton = Checkbutton(series_frame, text="series 1", bg="#423120", fg="white", selectcolor="#423120", padx=4, variable = series_1_var).grid(row=0, column=0)
series_2_var = IntVar()
series_2_var.set(1)
series_2_checkbutton = Checkbutton(series_frame, text="series 2", bg="#000b79", fg="white", selectcolor="#000b79", padx=4, variable = series_2_var).grid(row=0, column=1)
series_3_var = IntVar()
series_3_var.set(1)
series_3_checkbutton = Checkbutton(series_frame, text="series 3", bg="#000b79", fg="white", selectcolor="#000b79", padx=4, variable = series_3_var).grid(row=0, column=2)
series_4_var = IntVar()
series_4_var.set(1)
series_4_checkbutton = Checkbutton(series_frame, text="series 4", bg="#000b79", fg="white", selectcolor="#000b79", padx=4, variable = series_4_var).grid(row=0, column=3)
series_5_var = IntVar()
series_5_var.set(1)
series_5_checkbutton = Checkbutton(series_frame, text="series 5", bg="#0f3318", fg="white", selectcolor="#0f3318", padx=4, variable = series_5_var).grid(row=0, column=4)
series_6_var = IntVar()
series_6_var.set(1)
series_6_checkbutton = Checkbutton(series_frame, text="series 6", bg="#0f3318", fg="white", selectcolor="#0f3318", padx=4, variable = series_6_var).grid(row=1, column=0)
series_7_var = IntVar()
series_7_var.set(1)
series_7_checkbutton = Checkbutton(series_frame, text="series 7", bg="#0f3318", fg="white", selectcolor="#0f3318", padx=4, variable = series_7_var).grid(row=1, column=1)
series_8_var = IntVar()
series_8_var.set(1)
series_8_checkbutton = Checkbutton(series_frame, text="series 8", bg="#575654", fg="white", selectcolor="#575654", padx=4, variable = series_8_var).grid(row=1, column=2)
series_9_var = IntVar()
series_9_var.set(1)
series_9_checkbutton = Checkbutton(series_frame, text="series 9", bg="#575654", fg="white", selectcolor="#575654", padx=4, variable = series_9_var).grid(row=1, column=3)
series_10_var = IntVar()
series_10_var.set(1)
series_10_checkbutton = Checkbutton(series_frame, text="series 10", bg="#575654", fg="white", selectcolor="#575654", padx=1, variable = series_10_var).grid(row=1, column=4)
series_11_var = IntVar()
series_11_var.set(1)
series_11_checkbutton = Checkbutton(series_frame, text="series 11", bg="#4d3438", fg="white", selectcolor="#4d3438", padx=1, variable = series_11_var).grid(row=2, column=1)
series_12_var = IntVar()
series_12_var.set(1)
series_12_checkbutton = Checkbutton(series_frame, text="series 12", bg="#4d3438", fg="white", selectcolor="#4d3438", padx=1, variable = series_12_var).grid(row=2, column=2)
series_13_var = IntVar()
series_13_var.set(1)
series_13_checkbutton = Checkbutton(series_frame, text="series 13", bg="#4d3438", fg="white", selectcolor="#4d3438", padx=1, variable = series_13_var).grid(row=2, column=3)

select_all_frame = LabelFrame(root, padx=5, pady=5)
select_all_frame.pack()
select_all_button = Button(select_all_frame, text="Select All", command=select_all_button_function, font=("Helvetica, 10")).grid(row=0, column=0)
deselect_all_button = Button(select_all_frame, text="Deselect All", command=deselect_all_button_function, font=("Helvetica, 10")).grid(row=0, column=1)
pick_episode_button_function() # picks an episode

pick_episode_button = Button(text="Pick New Episode", command=pick_episode_button_function, font=("Helvetica", 15), padx = 10, pady = 20)
pick_episode_button.pack(pady=10)


root.mainloop()
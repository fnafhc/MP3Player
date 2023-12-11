#this code is made by FnafyyBoyy
#https://linktr.ee/fnafyyboyy

import os
import pygame
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import random
import time

def play_music():
    global selected_song, is_paused, total_time
    selected_song = listbox.get(tk.ACTIVE)
    pygame.mixer.music.load(selected_song)
    pygame.mixer.music.play()
    total_time = pygame.mixer.Sound(selected_song).get_length() // 1
    is_paused = False
    update_time()

def stop_music():
    pygame.mixer.music.stop()
    status_var.set("No song selected")
    song_var.set("No song selected")
    auto_play_var.set(False)

def pause_resume_music():
    global is_paused
    if not is_paused:
        pygame.mixer.music.pause()
        status_var.set("Music paused")
    else:
        pygame.mixer.music.unpause()
        status_var.set("Music resumed")
    is_paused = not is_paused
    update_time()
def load_music():
    global total_time
    folder = filedialog.askdirectory()
    os.chdir(folder)
    songs = [file for file in os.listdir(folder) if file.endswith((".mp3", ".ogg"))]
    listbox.delete(0, tk.END)
    for song in songs:
        listbox.insert(tk.END, song)

def play_random_song():
    if listbox.size() > 0:
        random_index = random.randint(0, listbox.size() - 1)
        listbox.selection_clear(0, tk.END)
        listbox.selection_set(random_index)
        listbox.activate(random_index)
        play_music()

def update_time():
    global total_time
    if pygame.mixer.music.get_busy() and not is_paused:
        current_time = pygame.mixer.music.get_pos() // 1000
        status_var.set(f"Time: {current_time} / {total_time} s")
        song_var.set(f"{os.path.basename(selected_song)}")
        root.after(1000, update_time)
    else:
        if auto_play_var.get():
            play_next_song()

def play_next_song():
    next_index = (listbox.curselection()[0] + 1) % listbox.size()
    listbox.selection_clear(0, tk.END)
    listbox.selection_set(next_index)
    listbox.activate(next_index)
    play_music()

root = tk.Tk()
root.title("MP3 Player by FnafyyBoyy")

#you can use this if you installed the mp3player.ico file
#icon_path = "mp3player.ico"
#root.iconbitmap(icon_path)

pygame.init()
pygame.mixer.init()

status_var = tk.StringVar()

y_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

x_scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL)
x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

listbox = tk.Listbox(root, width=50, height=15, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
listbox.pack(pady=10)

song_var = tk.StringVar()
status_var = tk.StringVar()
auto_play_var = tk.BooleanVar()

song_label = tk.Label(root, textvariable=song_var)
song_label.pack(pady=1)

status_label = tk.Label(root, textvariable=status_var)
status_label.pack(pady=10)

play_buttons_frame = ttk.Frame(root)
play_buttons_frame.pack(pady=5)

play_button = ttk.Button(play_buttons_frame, text='Play', command=play_music)
play_button.grid(row=0, column=0, padx=5)

pause_resume_button = ttk.Button(play_buttons_frame, text='Pause/Resume', command=pause_resume_music)
pause_resume_button.grid(row=0, column=1, padx=5)

stop_button = ttk.Button(play_buttons_frame, text='Stop', command=stop_music)
stop_button.grid(row=0, column=2, padx=5)

action_buttons_frame = ttk.Frame(root)
action_buttons_frame.pack(pady=5)

random_button = ttk.Button(action_buttons_frame, text='Play Random Song', command=play_random_song)
random_button.grid(row=0, column=0, padx=5)

load_button = ttk.Button(action_buttons_frame, text='Load Music Folder', command=load_music)
load_button.grid(row=0, column=1, padx=5)

ac2_buttons_frame = ttk.Frame(root)
ac2_buttons_frame.pack(pady=5)

auto_play_checkbox = ttk.Checkbutton(root, text="Auto Play Next Song", variable=auto_play_var)
auto_play_checkbox.pack(pady=5)

y_scrollbar.config(command=listbox.yview)
x_scrollbar.config(command=listbox.xview)

status_var.set("No song selected")
song_var.set("No song selected")

pygame.mixer.music.set_endevent(pygame.USEREVENT)

root.bind(pygame.USEREVENT, lambda event: play_next_song())

root.mainloop()

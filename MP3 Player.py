#this code is made by FnafyyBoyy
#https://linktr.ee/fnafyyboyy

import os
import pygame
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import random

def play_music():
    global selected_song
    selected_song = listbox.get(tk.ACTIVE)
    pygame.mixer.music.load(selected_song)
    pygame.mixer.music.play()
    current_time = pygame.mixer.music.get_pos() // 1000
    total_time = pygame.mixer.Sound(selected_song).get_length()
    status_var.set(f"Time: {current_time} / {total_time} s")

def stop_music():
    pygame.mixer.music.stop()
    status_var.set("No song selected")

def set_volume(val):
    pygame.mixer.music.set_volume(val / 100.0)

def load_music():
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
    if pygame.mixer.music.get_busy():
        selected_song = listbox.get(tk.ACTIVE)
        current_time = pygame.mixer.music.get_pos().real
        total_time = pygame.mixer.Sound(selected_song).get_length().real
        status_var.set(f"Time: {current_time} / {total_time} s")
        print("Time updated")

root = tk.Tk()
root.title("MP3 Player by FnafyyBoyy")

#you can use this if you installd the mp3player.ico file
#icon_path = r"C:\your\path\mp3player.ico"
#root.iconbitmap(icon_path)

pygame.init()
pygame.mixer.init()

status_var = tk.StringVar()

y_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

x_scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL)
x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

listbox = tk.Listbox(root, width=50, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
listbox.pack(pady=10)

status_var = tk.StringVar()
status_label = tk.Label(root, textvariable=status_var)
status_label.pack(pady=10)

play_button = ttk.Button(root, text='Play', command=play_music)
play_button.pack(pady=5)

stop_button = ttk.Button(root, text='Stop', command=stop_music)
stop_button.pack(pady=5)

load_button = ttk.Button(root, text='Load Music Folder', command=load_music)
load_button.pack(pady=10)

random_button = ttk.Button(root, text='Play Random Song', command=play_random_song)
random_button.pack(pady=5)

y_scrollbar.config(command=listbox.yview)
x_scrollbar.config(command=listbox.xview)

status_var.set("No song selected")

root.mainloop()

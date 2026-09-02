# Task 1 - Math Module

import math
print("Square root:", math.sqrt(225))


# Task 2 - OS Module

import os

folder_name = "MyDownloads"

os.makedirs(folder_name, exist_ok=True)

folder_path = os.path.abspath(folder_name)

print("Folder created at:", folder_path)


# Task 3 - Datetime Module

from datetime import datetime

current_time = datetime.now()

formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")

print("Current date and time:", formatted_time)


# Task 4 - Custom Module

import playlist_utils

playlist = []

playlist_utils.add_song(playlist, "Believer")
playlist_utils.add_song(playlist, "Perfect")
playlist_utils.add_song(playlist, "Senorita")

print("Final Playlist:", playlist)



# Task 5 - Requests Module

import requests

print("Requests version:", requests.__version__)
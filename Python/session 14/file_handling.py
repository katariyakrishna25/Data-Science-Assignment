# Task 1: Create playlist.txt

songs = ["Believer", "Perfect", "Senorita", "Shape Of You", "Levitating"]

with open("E:/tops assingment/session 14/playlist.txt", "w") as file:
    for song in songs:
        file.write(song + "\n")


# Task 2: Read playlist.txt

with open("E:/tops assingment/session 14/playlist.txt", "r") as file:
    for song in file:
        print(song.strip().upper())


# Task 3: Read IPL CSV file

import csv

with open("E:/tops assingment/session 14/ipl_matches.csv", "r") as file:
    data = csv.DictReader(file)

    for row in data:
        print("Winner:", row["winner"])


# Task 4: Read movies.json

import json

with open("E:/tops assingment/session 14/movies.json", "r") as file:
    movies = json.load(file)

for movie in movies:
    print(movie["title"], "-", movie["rating"])


# Task 5: Check and create my_fav_apps.json

from pathlib import Path

file_path = Path("E:/tops assingment/session 14/my_fav_apps.json")

apps = [
    {"name": "Instagram", "category": "Social Media"},
    {"name": "Zomato", "category": "Food Delivery"},
    {"name": "Paytm", "category": "Finance"}
]

if not file_path.exists():
    with open(file_path, "w") as file:
        json.dump(apps, file, indent=4)

    print("my_fav_apps.json created")
else:
    print("my_fav_apps.json already exists")
# Task 1: Dictionary
# Create a dictionary with 5 Instagram influencers
# Dictionary = {key : value}
# Keys are unique

insta_followers = {
    "virat": 270,
    "rohit": 40,
    "dhoni": 50,
    "rahul": 20,
    "hardik": 35
}

print(insta_followers)


# Task 2: Add, update and delete dictionary values
# Dictionary is mutable

insta_followers["bumrah"] = 15       # Add
insta_followers["virat"] = 280       # Update
del insta_followers["rahul"]          # Delete

print(insta_followers)


# Task 3: Dictionary - display items above ₹200
# We can access values using their keys

food_prices = {
    "Pizza": 250,
    "Burger": 180,
    "Biryani": 300,
    "Pasta": 220,
    "Sandwich": 150
}

for item in food_prices:
    if food_prices[item] > 200:
        print(item, food_prices[item])


# Task 4: Sets
# Sets are defined inside {}
# Sets do not allow duplicates
# Sets are mutable and iterable

flipkart_users = {"rahul", "krishna", "amit", "neha", "rohit"}
myntra_users = {"krishna", "neha", "pooja", "rohit", "raj"}

common_users = flipkart_users.intersection(myntra_users)

print(common_users)


# Task 5: Set Union
# Union gives all unique elements from both sets

def get_unique_artists(spotify_playlist1, spotify_playlist2):
    return spotify_playlist1.union(spotify_playlist2)

playlist1 = {"Arijit", "Atif", "AP Dhillon"}
playlist2 = {"Arijit", "Diljit", "Shreya"}

print(get_unique_artists(playlist1, playlist2))
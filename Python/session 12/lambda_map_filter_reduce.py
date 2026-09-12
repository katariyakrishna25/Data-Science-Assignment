# Task 1: Lambda + map()

songs = ['Shape Of You', 'Blinding Lights', 'Levitating', 'Senorita']

lowercase = lambda songs: songs.lower()

cleaned_songs = list(map(lowercase, songs))

print(cleaned_songs)


# Task 2: Lambda + filter()

ratings = [4.2, 3.8, 4.5, 2.9, 3.5]

above_4 = list(filter(lambda rating: rating > 4.0, ratings))

print(above_4)


# Task 3: reduce()

from functools import reduce

prices = [499, 1299, 299, 799]

total = reduce(lambda a, b: a + b, prices)

print("Total:", total)


# Task 4: map() + function

def format_followers(number):
    if number >= 1000000:
        return str(number / 1000000) + "M"
    elif number >= 1000:
        return str(number / 1000) + "K"
    else:
        return str(number)

followers = [950, 1500, 25000, 1200000]

formatted = list(map(format_followers, followers))

print(formatted)


# Task 5: Lambda + filter()

scores = [101, 98, 120, 77, 88]

even_scores = list(filter(lambda x: x % 2 == 0, scores))

print("Even scores:", even_scores)
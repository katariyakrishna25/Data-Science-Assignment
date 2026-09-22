# SESSION 2 - NumPy Intermediate

import numpy as np


# TASK 1 - Zomato Ratings

ratings = np.array([
    [5, 4, 3, 5, 4],
    [4, 5, 4, 3, 5],
    [3, 4, 5, 4, 4],
    [5, 3, 4, 5, 3]
])

# Second and third users
selected_ratings = ratings[1:3]

print("Second and Third Users Ratings:")
print(selected_ratings)


# TASK 2 - Boolean Indexing

steps = np.array([
    7500, 8200, 9000, 6500, 10000,
    7800, 8500, 7200, 9500, 6000
])

high_steps = steps[steps > 8000]

print("\nSteps Greater Than 8000:")
print(high_steps)


# TASK 3 - Fancy Indexing

scores = np.array([210, 185, 240, 195, 260, 220, 275, 230])

# Matches 2, 5 and 7
selected_scores = scores[[1, 4, 6]]

print("\nIPL Scores from Matches 2, 5 and 7:")
print(selected_scores)


# TASK 4 - Broadcasting

prices = np.array([500, 1000, 1500, 2000, 2500])

# 10% discount
discounted_prices = prices * 0.90

print("\nPrices After 10% Discount:")
print(discounted_prices)


# TASK 5 - Boolean Masking

song_ratings = np.array([-2, 5, -1, 4, 3, -3, 0, 5])

# Set all negative ratings to zero
song_ratings[song_ratings < 0] = 0

print("\nSong Ratings After Removing Negative Values:")
print(song_ratings)
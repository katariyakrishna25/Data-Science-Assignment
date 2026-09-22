# SESSION 1 - NumPy Foundations

# Task 1 - Import NumPy

import numpy as np


# Task 2 - Instagram Followers

followers = np.array([1200, 15000, 67000, 340000, 1250000])

print("Followers:", followers)
print("Shape:", followers.shape)
print("Dimensions:", followers.ndim)
print("Data Type:", followers.dtype)


# Task 3 - Zomato Order IDs

order_ids = np.arange(101, 111)

print("\nZomato Order IDs:", order_ids)
print("Size:", order_ids.size)


# Task 4 - Spotify Like Identity Matrix

like_matrix = np.eye(3)

# Diagonal values are 1, representing the main identity positions.
# Other values are 0.

print("\nSpotify Like Identity Matrix:")
print(like_matrix)


# Task 5 - Cricket Scores

scores = [45, 67, 120, 89, 54]

scores_array = np.array(scores)

print("\nCricket Scores:", scores_array)
print("Bytes per score:", scores_array.itemsize)
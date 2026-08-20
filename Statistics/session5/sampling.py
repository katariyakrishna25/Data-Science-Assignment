# Task 1: Population and Sample

# Example 1:
# Population = All Instagram followers
# Sample = 100 randomly selected Instagram followers

# Example 2:
# Population = All Zomato restaurants
# Sample = 50 randomly selected Zomato restaurants

# Example 3:
# Population = All Flipkart products
# Sample = 100 randomly selected Flipkart products


# Task 2: Random Sampling

import random

users = []

for i in range(1, 1001):
    users.append("user" + str(i))

sample = random.sample(users, 50)

print("Selected Users:")
print(sample)


# Task 3: Why Sampling?

# Sampling saves time and resources because collecting data from every
# Swiggy order would be very large and difficult.
# A properly selected sample can give useful information about all orders.


# Task 4: Sampling Bias

# This introduces selection bias because the survey only includes
# users who recently streamed Bollywood songs.
# Users who listen to other types of music are not properly represented.


# Task 5: Sampling Methods

# 1. Random Sampling:
# Randomly select BookMyShow users from the complete user list
# so every user has an equal chance of being selected.

# 2. Stratified Sampling:
# Divide users into groups based on factors like age or city,
# then randomly select users from each group.
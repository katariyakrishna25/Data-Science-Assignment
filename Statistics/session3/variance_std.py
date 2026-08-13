# Task 1: Variance by hand

steps = [4500, 7000, 5000, 8000, 4000, 9000, 6000]

# Mean
mean = sum(steps) / len(steps)
print("Mean:", mean)

# Variance formula:
# Variance = Sum of (x - mean)^2 / n

squared_differences = []

for x in steps:
    difference = x - mean
    square = difference ** 2
    squared_differences.append(square)
    print(x, "-", mean, "=", difference, " Square =", square)

variance = sum(squared_differences) / len(steps)

print("Variance:", variance)


# Task 2: Standard Deviation

import math

def calculate_standard_deviation(scores):
    mean = sum(scores) / len(scores)

    squared_differences = []
    for x in scores:
        squared_differences.append((x - mean) ** 2)

    variance = sum(squared_differences) / len(scores)
    return round(math.sqrt(variance), 2)

scores = [80, 75, 90, 85, 70]

print("Standard Deviation:", calculate_standard_deviation(scores))


# Task 3: Compare spending

friend_a = [200, 200, 200, 200, 200]
friend_b = [100, 300, 150, 400, 50]

print("Friend A SD:", calculate_standard_deviation(friend_a))
print("Friend B SD:", calculate_standard_deviation(friend_b))

# Friend A has more consistent spending because the standard deviation is 0.
# Friend B has higher variation because the spending amounts are very different.


# Task 4: Salary variance and standard deviation

salaries = [28000, 29000, 27000, 60000, 26500, 27500]

mean = sum(salaries) / len(salaries)

squared_differences = []

for salary in salaries:
    squared_differences.append((salary - mean) ** 2)

variance = sum(squared_differences) / len(salaries)
standard_deviation = math.sqrt(variance)

print("Salary Variance:", variance)
print("Salary Standard Deviation:", round(standard_deviation, 2))

# The spread is high because one salary (60000) is much higher than the others.
# This shows that employee salaries are not very consistent.
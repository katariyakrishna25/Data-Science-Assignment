# SESSION 3 - NumPy Advanced
# Matrix Operations & Array Manipulation

import numpy as np


# TASK 1 - Daily Steps of Two Friends

friend1 = np.array([5000, 6000, 7000, 8000, 9000, 7500, 8500])
friend2 = np.array([4500, 6500, 6800, 7200, 9500, 7000, 8000])

print("Addition:")
print(friend1 + friend2)

print("\nSubtraction:")
print(friend1 - friend2)

print("\nMultiplication:")
print(friend1 * friend2)

print("\nDivision:")
print(friend1 / friend2)


# TASK 2 - Spotify Recommendation

user_preferences = np.array([
    [5, 4, 3],
    [3, 5, 4],
    [4, 3, 5]
])

song_popularity = np.array([
    [5, 3, 4],
    [4, 5, 3],
    [3, 4, 5]
])

dot_result = np.dot(user_preferences, song_popularity)
matmul_result = np.matmul(user_preferences, song_popularity)

print("\nDot Result:")
print(dot_result)

print("\nMatmul Result:")
print(matmul_result)

# For 2D arrays, dot() and matmul() give the same matrix multiplication result.


# TASK 3 - Instagram Image

pixels = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

rotated_image = pixels.T

print("\nOriginal Image:")
print(pixels)

print("\nTransposed Image:")
print(rotated_image)

print("\nMean:", np.mean(pixels))
print("Median:", np.median(pixels))
print("Standard Deviation:", np.std(pixels))
print("Variance:", np.var(pixels))


# TASK 4 - Zomato Rating Correlation Grid

matrix = np.array([
    [4, 1, 2],
    [1, 5, 1],
    [2, 1, 6]
])

inverse = np.linalg.inv(matrix)
determinant = np.linalg.det(matrix)
eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("\nMatrix:")
print(matrix)

print("\nInverse:")
print(inverse)

print("\nDeterminant:")
print(determinant)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)


# TASK 5 - Swiggy Orders

orders = np.array([
    [10, 20, 30, 40, 50, 60],
    [15, 25, 35, 45, 55, 65]
])

reshaped = orders.reshape(3, 4)

flattened = orders.flatten()

parts = np.split(flattened, 2)

stacked = np.vstack(parts)

print("\nOriginal Orders:")
print(orders)

print("\nReshaped to 3x4:")
print(reshaped)

print("\nFlattened:")
print(flattened)

print("\nTwo Equal Parts:")
print(parts)

print("\nStacked Vertically:")
print(stacked)
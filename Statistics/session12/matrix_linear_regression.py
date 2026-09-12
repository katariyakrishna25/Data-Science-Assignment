# Task 1: 2x2 Matrix Multiplication (Instagram Engagement)
# Matrix A: Post engagement rates / Day 1 & Day 2
# Matrix B: Weights / Engagement scaling factors
matrix_a = [
    [120, 15],  # [Likes, Comments] Post 1
    [200, 30]   # [Likes, Comments] Post 2
]

matrix_b = [
    [2, 1],
    [3, 4]
]

# Standard 2x2 Matrix Multiplication: (A x B)
result_matrix = [
    [
        matrix_a[0][0] * matrix_b[0][0] + matrix_a[0][1] * matrix_b[1][0],
        matrix_a[0][0] * matrix_b[0][1] + matrix_a[0][1] * matrix_b[1][1]
    ],
    [
        matrix_a[1][0] * matrix_b[0][0] + matrix_a[1][1] * matrix_b[1][0],
        matrix_a[1][0] * matrix_b[0][1] + matrix_a[1][1] * matrix_b[1][1]
    ]
]

print("Task 1 - Multiplied Matrix Result:")
for row in result_matrix:
    print(row)
print()


# Task 2: Linear Regression Prediction Function
def linear_regression_predict(x, m, c):
    return (m * x) + c

# Quick test
sample_prediction = linear_regression_predict(3, 2, 5)
print(f"Test Prediction (x=3, m=2, c=5): {sample_prediction}\n")


# Task 3: Zomato Delivery Time Prediction
# Equation: y = 4x + 10 (m = 4, c = 10)
distances_km = [2, 5, 8]
slope_m = 4
intercept_c = 10

print("Zomato Delivery Times:")
for dist in distances_km:
    predicted_time = linear_regression_predict(dist, slope_m, intercept_c)
    print(f"Distance: {dist} km -> Predicted Delivery Time: {predicted_time} minutes")
print()


# Task 4: Slope and Intercept Intuition (Flipkart Price vs. Rating)
"""
Task 4 Explanation:

Slope (m):
The slope represents the expected change in product price for every one-unit increase in customer rating.
A positive slope indicates that as product quality or user satisfaction rises, the market value or listing price increases proportionately.

Intercept (c):
The intercept represents the baseline price of a product when its rating is zero.
It sets the foundational manufacturing or base operational cost below which a product cannot be priced, regardless of customer feedback.
"""
print("explanation printed in code docstring above.\n")


# Task 5: Matrix Multiplication in Spotify Recommendation Model
"""
Task 5 Summary:
Spotify uses collaborative filtering techniques, such as Matrix Factorization, where large user-song interaction matrices are broken down into smaller user and song latent feature vectors.
Matrix multiplication allows the system to compute the dot product between a user profile vector and thousands of song attribute vectors in parallel.
This calculation produces predicted preference scores, enabling real-time generation of tailored playlists like Discover Weekly.
"""
print("summary printed in code docstring above.")
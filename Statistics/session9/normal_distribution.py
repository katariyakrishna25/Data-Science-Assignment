import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Task 1: Generate 100 Random Numbers and Plot Bell Curve

mean = 50
std_dev = 10
data = np.random.normal(loc=mean, scale=std_dev, size=100)

plt.figure(figsize=(8, 4))
count, bins, ignored = plt.hist(data, bins=15, density=True, alpha=0.6, color='skyblue', edgecolor='black')
curve = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((bins - mean) / std_dev) ** 2)
plt.plot(bins, curve, color='darkblue', linewidth=2)
plt.title("Normal Distribution (Mean=50, Std=10)")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.show()


# Task 2: Fitness Tracker Step Counts (Mean, Median, Mode)

steps = np.array([
    7800, 8100, 7950, 8000, 8200, 7900, 8050, 8150, 8000, 7850,
    8100, 8000, 8250, 7950, 8050, 8100, 7900, 8000, 8150, 8050
])

mean_steps = np.mean(steps)
median_steps = np.median(steps)
mode_steps = stats.mode(steps).mode

print(f"Mean: {mean_steps}, Median: {median_steps}, Mode: {mode_steps}")
is_symmetric = np.isclose(mean_steps, median_steps, atol=100)
print(f"Are Mean, Median, and Mode approximately equal? {is_symmetric}")


# Task 3: Online Game Player Scores (68-95-99 Rule)

scores = np.random.normal(loc=70, scale=15, size=200)

within_one_std = np.sum((scores >= 55) & (scores <= 85))
percentage_within = (within_one_std / 200) * 100

print(f"Players scored between 55 and 85: {within_one_std} out of 200 ({percentage_within:.1f}%)")
# According to the 68-95-99.7 empirical rule, ~68% of data falls within 1 standard deviation of the mean.


# Task 4: Real-World Scenario (Zomato Food Delivery Times)

"""
Scenario: Delivery times for Zomato food orders typically follow a normal distribution.
Most deliveries take an average duration (e.g., 30 minutes) centered around the mean.
Minor variations (traffic, kitchen prep) balance out on both sides, making delays (45+ mins)
and rapid deliveries (under 15 mins) symmetrically rare as extreme tail events.
"""
print("explanation printed in code docstring above.")
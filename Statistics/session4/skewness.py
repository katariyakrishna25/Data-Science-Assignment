# Task 1: Swiggy Order Counts

import matplotlib.pyplot as plt

orders = [12, 15, 17, 14, 13, 16, 200, 18, 14, 15]

plt.plot(orders, marker="o")
plt.title("Daily Swiggy Orders")
plt.xlabel("Days")
plt.ylabel("Orders")
plt.show()

# The data is right skewed because 200 is a very high value
# compared to the other order counts.


# Task 2: Instagram Followers

followers = [5, 7, 8, 8, 9, 10, 12, 15, 95]

mean = sum(followers) / len(followers)
median = sorted(followers)[len(followers) // 2]

print("Mean:", mean)
print("Median:", median)

# Mean is higher than median because 95 is an unusually high value.
# Therefore, the data is right skewed.


# Task 3: Real-world example of right-skewed data

youtube_views = [100, 150, 200, 250, 300, 500, 1000, 5000]

# Most videos have lower views, while a few videos have very high views.
# Therefore, YouTube video views are usually right skewed.


# Task 4: Flipkart Ratings

ratings = [3, 3, 4, 4, 4, 5, 5, 5, 5, 5]

plt.hist(ratings, bins=[2.5, 3.5, 4.5, 5.5], edgecolor="black")
plt.title("Flipkart Product Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()

# The distribution is left skewed because most ratings are 5,
# while fewer ratings are present at 3 and 4.
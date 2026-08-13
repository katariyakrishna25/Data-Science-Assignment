# Task 1: Find Mean

plays = [120, 135, 150, 200, 120, 90, 200]

mean = sum(plays) / len(plays)

print("Mean:", mean)


# Task 2: Find Median

delivery_times = [30, 25, 40, 35, 30, 45, 30]

delivery_times.sort()

n = len(delivery_times)
median = delivery_times[n // 2]

print("Median:", median)


# Task 3: Find Mode

def most_common_rating(ratings):
    return max(set(ratings), key=ratings.count)

ratings = [5, 4, 4, 3, 5, 4, 2, 4]

print("Mode:", most_common_rating(ratings))


# Task 4: Mean, Median and Mode

channel1 = [100, 120, 110, 105, 5000]
channel2 = [100, 120, 110, 105, 115]
channel3 = [50, 60, 60, 70, 80]

channels = [channel1, channel2, channel3]

for i in range(len(channels)):
    data = channels[i]

    mean = sum(data) / len(data)

    data.sort()
    median = data[len(data) // 2]

    mode = max(set(data), key=data.count)

    print("Channel", i + 1)
    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)

print("Channel 1 is most affected by outliers because of 5000.")


# Task 5: Real Dataset using Pandas

import pandas as pd

df = pd.read_csv("ipl.csv")

column = "Runs"

print("Mean:", df[column].mean())
print("Median:", df[column].median())
print("Mode:", df[column].mode()[0])
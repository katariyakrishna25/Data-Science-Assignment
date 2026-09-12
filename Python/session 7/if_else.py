# Task 1: Check Spotify listening time

listening_time = int(input("Enter Spotify listening time in minutes: "))

if listening_time > 120:
    print("You are a true music fan!")
else:
    print("Keep listening!")


# Task 2: Check Zomato order amount

order_amount = int(input("Enter Zomato order amount: "))

if order_amount > 300:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")


# Task 3: Flipkart discount

total = int(input("Enter Flipkart cart total: "))

if total > 2000:
    print("You get a 10% discount")
elif total > 1000:
    print("You get a 5% discount")
else:
    print("No discount available")


# Task 4: IPL fantasy team points

points = int(input("Enter IPL fantasy team points: "))

if points > 800:
    print("Champion")
else:
    if points >= 500:
        print("Top Performer")
    else:
        print("Keep Trying")
# Task 1: Print 5 favorite food delivery apps

apps = ["Zomato", "Swiggy", "Uber Eats", "Blinkit", "Zepto"]

for app in apps:
    print(app)


# Task 2: Find first day above 10,000 steps

steps = [6500, 8200, 9500, 8500, 11000, 9000, 12000]

day = 0

while day < len(steps):
    if steps[day] > 10000:
        print("First day above 10,000 steps:", day + 1) 
        break
    day += 1


# Task 3: Print IPL teams with names longer than 6 characters

def long_team_names(teams):
    for team in teams:
        if len(team) <= 6:
            continue
        print(team)

teams = ["Mumbai Indians", "CSK", "Rajasthan Royals", "KKR", "Punjab Kings"]

long_team_names(teams)



# Task 4: Print song position and duration

durations = [210, 185, 240, 195, 300]

for position, duration in enumerate(durations, start=1):
    print(f"Song {position}: {duration} seconds")


# Task 5: Shopping cart total

prices = [500, 0, 500, 900, 300, 400]

total = 0

for price in prices:
    if price == 0:
        continue

    total += price

    if total > 2000:
        break

print("Final total:", total)
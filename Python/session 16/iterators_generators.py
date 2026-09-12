# Task 1
apps = ["Zomato", "Swiggy", "Dominos", "Uber Eats", "EatSure"]

app_iterator = iter(apps)

while True:
    try:
        app = next(app_iterator)
        print(app)
    except StopIteration:
        break


# Task 2
def playlist_generator(songs):
    for song in songs:
        yield song


songs = ["Believer", "Perfect", "Senorita", "Levitating", "Shape Of You"]

playlist = playlist_generator(songs)

for song in playlist:
    print("Song:", song)


# Task 3
cart = ["Pizza", "Burger", "Fries", "Coke"]

for index, item in enumerate(cart, start=1):
    print(index, item)


# Task 4
teams = ["Mumbai Indians", "Chennai Super Kings", "RCB", "KKR"]
points = [18, 16, 14, 12]

for team, point in zip(teams, points):
    print("Team:", team, "Points:", point)


# Task 5
def order_id_generator():
    order_id = 1001

    while True:
        yield order_id
        order_id += 1


orders = order_id_generator()

print("Order ID:", next(orders))
print("Order ID:", next(orders))
print("Order ID:", next(orders))
print("Order ID:", next(orders))
print("Order ID:", next(orders))
import random

# Task 1: Probability Function & Coin Toss
def calculate_probability(event_count, total_outcomes):
    return event_count / total_outcomes

p_heads = calculate_probability(1, 2)
print(f"Probability of Heads: {p_heads}")


# Task 2: Dice Roll Simulation (100 rolls)
count_six = 0
total_rolls = 100

for _ in range(total_rolls):
    roll = random.randint(1, 6)
    if roll == 6:
        count_six += 1

prob_six = count_six / total_rolls
print(f"Count of 6s: {count_six}, Experimental Probability: {prob_six}")


# Task 3: Spotify Song Genre Probability
recent_songs = [
    'pop', 'rock', 'pop', 'hiphop', 'pop', 'jazz', 'rock', 'pop', 'hiphop', 'pop',
    'classical', 'rock', 'pop', 'pop', 'hiphop', 'jazz', 'pop', 'rock', 'pop', 'lofi'
]

pop_count = recent_songs.count('pop')
total_songs = len(recent_songs)
prob_pop = pop_count / total_songs

print(f"Probability of picking a 'pop' song: {prob_pop}")


# Task 4: Zomato Food & Dessert Orders
def calculate_both_order_probability(food_users, dessert_users):
    set_food = set(food_users)
    set_dessert = set(dessert_users)

    both_orders = set_food.intersection(set_dessert)
    total_unique_users = set_food.union(set_dessert)

    return len(both_orders) / len(total_unique_users)

food_customers = ['UserA', 'UserB', 'UserC', 'UserD', 'UserE']
dessert_customers = ['UserC', 'UserE', 'UserF', 'UserG']

prob_both = calculate_both_order_probability(food_customers, dessert_customers)
print(f"Probability of ordering both food and dessert: {prob_both:.2f}")


# Task 5: Flipkart Conditional Recommendation
phone_buyers = {'User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7', 'User8', 'User9', 'User10'}
bought_both = {'User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7'}

prob_headphones_given_phone = len(bought_both) / len(phone_buyers)
print(f"Conditional Probability P(Headphones | Phone): {prob_headphones_given_phone}")
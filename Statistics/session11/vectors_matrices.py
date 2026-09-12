# Task 1: Playlist Total Duration
playlist = [210, 180, 245, 200, 175]
total_duration = sum(playlist)

print(f"Playlist: {playlist}")
print(f"Total Duration: {total_duration} seconds\n")


# Task 2: 3x3 Ratings Matrix (Friends x Food Items)
# Rows: Friends (Friend 1, Friend 2, Friend 3)
# Columns: Items (Dish 1, Dish 2, Dish 3)
ratings_matrix = [
    [4, 5, 3],  # Friend 1
    [3, 4, 4],  # Friend 2
    [5, 2, 5]   # Friend 3
]

print("Ratings Matrix:")
for row in ratings_matrix:
    print(row)

# The second food item is at column index 1
for i, row in enumerate(ratings_matrix):
    print(f"Friend {i + 1} rating for second food item: {row[1]}")
print()


# Task 3: Total Orders for Each Dish Across 3 Days
# Rows: Days (Day 1, Day 2, Day 3)
# Columns: Dishes (Dish A, Dish B, Dish C, Dish D)
orders_matrix = [
    [12, 25, 8, 15],  # Day 1
    [10, 30, 6, 20],  # Day 2
    [14, 22, 11, 18]  # Day 3
]

num_dishes = len(orders_matrix[0])
total_orders_per_dish = [sum(orders_matrix[day][dish] for day in range(len(orders_matrix))) for dish in range(num_dishes)]

print("Orders Matrix (Days x Dishes):")
for row in orders_matrix:
    print(row)

for dish_idx, total in enumerate(total_orders_per_dish):
    print(f"Total orders for Dish {dish_idx + 1}: {total}")
print()


# Task 4: Flipkart Products Revenue (Price x Quantity)
# Matrix format: [Price, Quantity] for 5 products
flipkart_products = [
    [499, 12],   # Product 1
    [1299, 5],   # Product 2
    [299, 25],   # Product 3
    [899, 8],    # Product 4
    [1999, 3]    # Product 5
]

def calculate_revenues(products_matrix):
    revenues = []
    for idx, (price, quantity) in enumerate(products_matrix, start=1):
        revenue = price * quantity
        revenues.append(revenue)
        print(f"Product {idx} (Price: {price}, Qty: {quantity}) -> Total Revenue: {revenue}")
    return revenues

print("Flipkart Product Revenues:")
total_revenues = calculate_revenues(flipkart_products)
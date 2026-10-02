# SESSION 5 - Data Collection using Pandas (Part 2)


# Task 1 - Read Restaurants Data from MySQL/PostgreSQL

import pandas as pd
from sqlalchemy import create_engine

# Database connection
# Change username, password and database name according to your database

engine = create_engine(
    "mysql+pymysql://root:krishna@localhost/exam"
)

restaurants = pd.read_sql(
    "restaurants",
    engine
)

print("First 5 Restaurants:")
print(restaurants.head())


# Task 2 - Read Movies with Rating Above 8

movies = pd.read_sql_query(
    "SELECT name, rating FROM movies WHERE rating > 8",
    engine
)

print("\nMovies with Rating Above 8:")
print(movies)


# Task 3 - Read JSON Data from URL

users = pd.read_json(
    "https://jsonplaceholder.typicode.com/users"
)

print("\nUsernames:")
print(users["username"])


# Task 4 - Merge Orders and Users

from pathlib import Path

folder_path = Path(".")

orders_path = folder_path / "orders.csv"
users_path = folder_path / "users.csv"

orders = pd.read_csv(orders_path)
users_data = pd.read_csv(users_path)

combined_data = pd.merge(
    orders,
    users_data,
    on="user_id"
)

print("\nCombined Orders and Users:")
print(combined_data)


# Task 5 - Concatenate Today's and Yesterday's Orders

today_orders = pd.DataFrame({
    "order_id": [101, 102, 103],
    "item": ["Pizza", "Burger", "Pasta"],
    "price": [250, 180, 220]
})

yesterday_orders = pd.DataFrame({
    "order_id": [104, 105, 106],
    "item": ["Sandwich", "Biryani", "Dosa"],
    "price": [150, 300, 120]
})

combined_orders = pd.concat(
    [today_orders, yesterday_orders],
    ignore_index=True
)

print("\nCombined Orders:")
print(combined_orders)
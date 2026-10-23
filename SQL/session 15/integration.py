# SESSION 15 - SQL + Python Integration

import sqlite3
import pandas as pd

# QUESTION 1
# Create foodie.db database and Restaurants table.

conn = sqlite3.connect("foodie.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Restaurants (
    id INTEGER PRIMARY KEY,
    name TEXT,
    cuisine TEXT,
    rating REAL
)
""")

conn.commit()

# QUESTION 2
# Insert three sample restaurants and fetch ratings above 4.0.

restaurants = [
    (1, "La Pino'z Pizza", "Italian", 4.5),
    (2, "Honest", "Indian", 4.2),
    (3, "Domino's", "Italian", 3.8)
]

cursor.executemany("""
INSERT OR IGNORE INTO Restaurants (id, name, cuisine, rating)
VALUES (?, ?, ?, ?)
""", restaurants)

conn.commit()

cursor.execute("""
SELECT name
FROM Restaurants
WHERE rating > 4.0
""")

print("Restaurants with rating above 4.0:")
for row in cursor.fetchall():
    print(row[0])

# QUESTION 3
# Load all restaurants into a Pandas DataFrame and display top 2 rows.

df = pd.read_sql_query("SELECT * FROM Restaurants", conn)

print("\nTop 2 restaurants:")
print(df.head(2))

# QUESTION 4
# Add delivery_charge and calculate final_rating.

df["delivery_charge"] = 50

df["final_rating"] = df.apply(
    lambda row: row["rating"] + 0.1
    if row["cuisine"] == "Italian"
    else row["rating"],
    axis=1
)

print("\nDataFrame with delivery charge and final rating:")
print(df)

# QUESTION 5
# Fetch restaurants with rating above 4.5 and save as CSV.

top_rated_df = pd.read_sql_query("""
SELECT *
FROM Restaurants
WHERE rating > 4.5
""", conn)

top_rated_df.to_csv("top_rated_restaurants.csv", index=False)

print("\nTop-rated restaurants saved to top_rated_restaurants.csv")

conn.close()

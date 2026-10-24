# DATA SCIENCE ASSESSMENT – M4-A1
# Modules 3–4: Data Collection, Cleaning & Visualization
# Topic: Working with Databases
# Stack: Python 3 / SQL (SQLite)

# ============================================================
# SECTION A – CONCEPT APPLICATION
# ============================================================

# QUESTION 1
# Scenario:
# A food delivery startup has 50,000 order records. delivery_time_mins has 14%
# missing values and customer_rating contains strings such as '4.5'.

# Question:
# Explain whether to drop rows or use mean/median imputation for
# delivery_time_mins, based on missing percentage and skewness. Also explain the
# exact Pandas steps to fix customer_rating before analysis.

# ANSWER:
# 14% is a noticeable amount of missing data, so dropping all missing rows may
# waste useful information. Imputation is generally better. Use mean when the
# data is approximately normally distributed. Use median when delivery time is
# skewed or has outliers.

df['delivery_time_mins'] = df['delivery_time_mins'].fillna(
    df['delivery_time_mins'].median()
)
df['customer_rating'] = pd.to_numeric(
    df['customer_rating'], errors='coerce'
)


# QUESTION 2
# Scenario:
# A NumPy array contains daily order counts for 30 days. Surge days are days
# where order count is more than mean + 1.5 standard deviations. Revenue is stored
# in a matching array.

# Question:
# Explain Boolean indexing, np.mean and np.std for finding surge days without a
# Python loop.

# ANSWER:
mean_orders = np.mean(order_counts)
std_orders = np.std(order_counts)
threshold = mean_orders + 1.5 * std_orders
surge_mask = order_counts > threshold
surge_revenue = revenue[surge_mask]
total_revenue = np.sum(surge_revenue)

# A Boolean mask contains True/False values. True selects matching elements.
# NumPy performs element-wise operations efficiently, so a Python loop is not
# required.

# ------------------------------------------------------------

# QUESTION 3
# Scenario:
# EDA contains restaurant_category, average_order_value, customer_rating and
# delivery_time_mins. The team wants to know whether delivery time is correlated
# with rating and how average order value is distributed across categories.

# Question:
# Identify the analysis type and one suitable Seaborn chart for each question.

# ANSWER:
# (a) delivery_time_mins vs customer_rating:
# Bivariate analysis. Use a Seaborn scatterplot.

sns.scatterplot(data=df, x='delivery_time_mins', y='customer_rating')

# (b) average_order_value across restaurant_category:
# Bivariate analysis. Use a Seaborn boxplot.

sns.boxplot(data=df, x='restaurant_category',
            y='average_order_value')

# Scatterplot shows the relationship between two numerical variables. Boxplot
# shows median, spread and outliers across categories. These are more suitable

# QUESTION 4
# Scenario:
# A database has orders, restaurants and customers. The report must show every
# restaurant and total revenue, including restaurants with zero orders.

# Question:
# Which JOIN is required? What happens with INNER JOIN?

# ANSWER:
# Use LEFT JOIN starting from restaurants.
'''
SELECT r.name,
       COALESCE(SUM(o.order_value), 0) AS total_revenue
FROM restaurants r
LEFT JOIN orders o
ON r.restaurant_id = o.restaurant_id
GROUP BY r.restaurant_id, r.name;
'''

# LEFT JOIN keeps every restaurant even when no order matches it. COALESCE changes
# NULL to 0. INNER JOIN would remove restaurants that have no orders.

# ------------------------------------------------------------

# QUESTION 5
# Scenario:
# Management wants to rank delivery agents within each city by completed
# deliveries for the current month and compare each agent with the agent directly
# above them.

# Question:
# Identify the two window functions and explain PARTITION BY.

# ANSWER:
# Use RANK() for ranking and LAG() for the previous row.
'''
SELECT city, agent_name, completed_deliveries,
       RANK() OVER (
           PARTITION BY city
           ORDER BY completed_deliveries DESC
       ) AS delivery_rank,
       LAG(completed_deliveries) OVER (
           PARTITION BY city
           ORDER BY completed_deliveries DESC
       ) AS previous_count
FROM agent_summary;
'''

# PARTITION BY creates a separate ranking group for every city. Window functions
# keep individual rows visible while calculating ranking and previous-row values.

# ------------------------------------------------------------

# QUESTION 6
# Scenario:
# A report first finds the top 5 restaurant categories by total order count and
# then retrieves full order details for those categories.

# Question:
# Compare a CTE with a nested subquery. When would you prefer the nested subquery?

# ANSWER:
# A CTE makes a multi-step query easier to read and debug.
'''
WITH top_categories AS (
    SELECT category
    FROM orders
    GROUP BY category
    ORDER BY COUNT(*) DESC
    LIMIT 5
)
SELECT *
FROM orders
WHERE category IN (
    SELECT category FROM top_categories
);
'''

# Use a nested subquery when the intermediate calculation is simple, used only
# once, and the query remains easy to understand. CTEs are useful for complex
# multi-step logic.

# ============================================================
# SECTION B – PRACTICAL CODING TASKS
# ============================================================

# TASK 1 – NUMPY DAILY ORDER ANALYSIS
# ------------------------------------------------------------
# QUESTION:
# Create 30 days of order counts and revenue using np.random.seed(42). Print
# total orders, total revenue, mean/std daily orders, highest-revenue day, days
# where orders exceed mean + 1 standard deviation, their count and revenue, and
# 5x6 block sums using axis=1.

# ANSWER:
# Save as: task1_numpy_food_delivery.py

import numpy as np

np.random.seed(42)

order_counts = np.random.randint(100, 801, 30)
revenue = np.random.uniform(5000, 50000, 30)

print("Total Orders:", np.sum(order_counts))
print("Total Revenue:", round(np.sum(revenue), 2))

mean_orders = np.mean(order_counts)
std_orders = np.std(order_counts)

print("Mean Daily Orders:", round(mean_orders, 2))
print("Standard Deviation:", round(std_orders, 2))

highest_day = np.argmax(revenue)
print("Highest Revenue Day Index:", highest_day)

mask = order_counts > (mean_orders + std_orders)

print("Number of High-Order Days:", np.sum(mask))
print("Revenue from High-Order Days:", round(np.sum(revenue[mask]), 2))

order_matrix = order_counts.reshape(5, 6)
print("5 x 6 Matrix:")
print(order_matrix)

print("Block Totals:")
print(np.sum(order_matrix, axis=1))


# TASK 2 – PANDAS DATA CLEANING
# ------------------------------------------------------------
# QUESTION:
# Create at least 20 rows with order_id, customer_name, restaurant_name,
# category, delivery_time_mins, order_value and rating. Add at least 4 missing
# values and 3 duplicate rows. Fill numeric missing values using medians, rating
# using mean rounded to 1 decimal, category using mode, remove duplicates, print
# before/after shape and null counts, detect order_value outliers using IQR, print
# them and cap them using clip().

# ANSWER:
# Save as: task2_pandas_cleaning.py

import pandas as pd
import numpy as np

data = {
    "order_id": range(1, 21),
    "customer_name": [
        "Amit","Riya","Rahul","Neha","Karan","Pooja","Vijay","Anjali",
        "Rohit","Priya","Arjun","Sneha","Mohan","Kavya","Nitin","Meera",
        "Raj","Simran","Akash","Tina"
    ],
    "restaurant_name": [
        "Spice Hub","Food Point","Pizza House","Burger King","Spice Hub",
        "Food Point","Pizza House","Burger King","Spice Hub","Food Point",
        "Pizza House","Burger King","Spice Hub","Food Point","Pizza House",
        "Burger King","Spice Hub","Food Point","Pizza House","Burger King"
    ],
    "category": [
        "Indian","Fast Food","Pizza","Fast Food","Indian",
        "Fast Food","Pizza","Fast Food","Indian","Fast Food",
        "Pizza","Fast Food","Indian","Fast Food","Pizza",
        "Fast Food","Indian","Fast Food","Pizza","Fast Food"
    ],
    "delivery_time_mins": [
        30,35,40,25,32,38,45,28,31,36,42,27,34,39,44,29,33,37,41,26
    ],
    "order_value": [
        250,320,450,200,280,350,500,220,270,330,480,210,290,360,520,
        230,310,340,470,190
    ],
    "rating": [
        4.2,4.5,4.0,3.8,4.3,4.1,4.6,3.9,4.4,4.2,4.5,3.7,4.1,4.3,
        4.6,3.8,4.2,4.0,4.5,3.9
    ]
}

df = pd.DataFrame(data)

df.loc[2, "delivery_time_mins"] = np.nan
df.loc[5, "order_value"] = np.nan
df.loc[8, "rating"] = np.nan
df.loc[11, "category"] = np.nan

df = pd.concat([df, df.iloc[[0, 1, 2]]], ignore_index=True)

print("Null counts BEFORE:")
print(df.isnull().sum())

print("Shape BEFORE:", df.shape)

df["delivery_time_mins"] = df["delivery_time_mins"].fillna(
    df["delivery_time_mins"].median()
)
df["order_value"] = df["order_value"].fillna(
    df["order_value"].median()
)
df["rating"] = df["rating"].fillna(round(df["rating"].mean(), 1))
df["category"] = df["category"].fillna(df["category"].mode()[0])

print("Null counts AFTER:")
print(df.isnull().sum())

df = df.drop_duplicates()
print("Shape AFTER:", df.shape)

Q1 = df["order_value"].quantile(0.25)
Q3 = df["order_value"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["order_value"] < lower) |
    (df["order_value"] > upper)
]

print("Outlier Rows:")
print(outliers)

df["order_value"] = df["order_value"].clip(
    lower=lower,
    upper=upper
)


# TASK 3 – FOOD DELIVERY VISUALISATION DASHBOARD
# ------------------------------------------------------------
# QUESTION:
# Create a 2x2 figure:
# 1. Seaborn countplot – order count by category.
# 2. Seaborn boxplot – delivery time by category.
# 3. Matplotlib horizontal bar chart – average order value by restaurant.
# 4. Seaborn heatmap – correlation matrix of numeric columns with annot=True.
# Add title/x/y labels, use tight_layout(), and save as
# food_delivery_dashboard.png at dpi=150.

# ANSWER:
# Use the cleaned df from Task 2:

import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.countplot(data=df, x="category", ax=axes[0, 0])
axes[0, 0].set_title("Order Count by Category")
axes[0, 0].set_xlabel("Category")
axes[0, 0].set_ylabel("Order Count")

sns.boxplot(
    data=df,
    x="category",
    y="delivery_time_mins",
    ax=axes[0, 1]
)
axes[0, 1].set_title("Delivery Time by Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Delivery Time (Minutes)")

avg_value = df.groupby("restaurant_name")["order_value"].mean().sort_values()
axes[1, 0].barh(avg_value.index, avg_value.values)
axes[1, 0].set_title("Average Order Value by Restaurant")
axes[1, 0].set_xlabel("Average Order Value")
axes[1, 0].set_ylabel("Restaurant")

corr = df.select_dtypes(include="number").corr()
sns.heatmap(corr, annot=True, ax=axes[1, 1])
axes[1, 1].set_title("Correlation Matrix")
axes[1, 1].set_xlabel("Numeric Columns")
axes[1, 1].set_ylabel("Numeric Columns")

plt.tight_layout()
plt.savefig(
    "food_delivery_dashboard.png",
    dpi=150,
    bbox_inches="tight"
)
print("Dashboard saved as food_delivery_dashboard.png")
plt.show()


# TASK 4 – SQLITE + PYTHON RESTAURANT PERFORMANCE REPORT
# ------------------------------------------------------------
# QUESTION:
# Create food_delivery.db, create restaurants and orders tables, insert at least
# 8 restaurants and 25 orders, use GROUP BY with COUNT(), SUM() and
# ROUND(AVG(), 2), load using pd.read_sql_query(), add revenue_rank using rank(),
# sort by rank, print the full table and Top 5 by revenue, and export
# restaurant_performance_report.csv.

# ANSWER:
# Save as: task4_sql_restaurant_report.py

import sqlite3
import pandas as pd

conn = sqlite3.connect("food_delivery.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS restaurants (
    restaurant_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    restaurant_id INTEGER,
    order_value REAL,
    delivery_time_mins REAL,
    rating REAL
)
""")

restaurants = [
    (1,"Spice Hub","Indian","Ahmedabad"),
    (2,"Pizza House","Pizza","Surat"),
    (3,"Burger Point","Fast Food","Ahmedabad"),
    (4,"Food Corner","Indian","Vadodara"),
    (5,"Tasty Bites","Fast Food","Surat"),
    (6,"Curry Palace","Indian","Rajkot"),
    (7,"Pizza World","Pizza","Ahmedabad"),
    (8,"Healthy Bowl","Healthy","Vadodara")
]

orders = [
    (1,1,350,32,4.2),(2,1,420,35,4.5),(3,1,280,30,4.1),
    (4,2,500,40,4.4),(5,2,450,38,4.2),(6,2,550,42,4.6),
    (7,3,250,25,3.9),(8,3,320,28,4.0),(9,3,290,27,4.1),
    (10,4,400,35,4.3),(11,4,380,34,4.2),(12,4,450,36,4.4),
    (13,5,300,29,4.0),(14,5,350,31,4.1),(15,5,330,30,4.2),
    (16,6,480,39,4.5),(17,6,520,41,4.6),(18,6,450,38,4.4),
    (19,7,600,45,4.7),(20,7,550,43,4.6),(21,7,620,46,4.8),
    (22,8,280,26,4.3),(23,8,300,27,4.2),(24,8,320,28,4.4),
    (25,1,390,33,4.3)
]

cursor.executemany(
    "INSERT OR REPLACE INTO restaurants VALUES (?, ?, ?, ?)",
    restaurants
)
cursor.executemany(
    "INSERT OR REPLACE INTO orders VALUES (?, ?, ?, ?, ?)",
    orders
)

conn.commit()

query = """
SELECT
    r.restaurant_id,
    r.name,
    r.category,
    r.city,
    COUNT(o.order_id) AS total_orders,
    SUM(o.order_value) AS total_revenue,
    ROUND(AVG(o.rating), 2) AS avg_rating
FROM restaurants r
LEFT JOIN orders o
ON r.restaurant_id = o.restaurant_id
GROUP BY r.restaurant_id, r.name, r.category, r.city
"""

df = pd.read_sql_query(query, conn)

df["revenue_rank"] = (
    df["total_revenue"]
    .rank(ascending=False, method="min")
    .astype(int)
)

df = df.sort_values("revenue_rank")

print("FULL REPORT")
print(df)

print("TOP 5 BY REVENUE")
print(df.sort_values("total_revenue", ascending=False).head(5))

df.to_csv("restaurant_performance_report.csv", index=False)
print("Report saved as restaurant_performance_report.csv")

conn.close()


# ============================================================
# SECTION C – MINI CAPSTONE PROJECT
# ============================================================

# QUESTION:
# Build a menu-driven Food Delivery Analytics Console Application integrating
# data cleaning, SQL and visualization.

# Required menu:
# 1. Load & Clean Data
# 2. Run SQL Analysis
# 3. View Charts
# 4. Export Report
# 0. Exit

# Option 1: load simulated data, impute missing values, remove duplicates,
# detect/cap order_value outliers and show before/after quality summaries.

# Option 2: connect to SQLite and run one GROUP BY query with COUNT/SUM/AVG and
# one JOIN between restaurants and orders.

# Option 3: show side-by-side countplot of orders by category and barplot of
# average delivery time by city.

# Option 4: export cleaned data and SQL analysis to separate sheets in
# food_delivery_report.xlsx using pandas.ExcelWriter.

# ANSWER:
# Save as food_delivery_capstone.py

# Use the following structure. The cleaning and SQL functions below can use the
# data/database from Tasks 2 and 4:

import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cleaned_df = None
sql_report = None

def load_and_clean_data():
    global cleaned_df
    cleaned_df = pd.DataFrame({
        "order_id": range(1, 21),
        "category": ["Indian","Pizza","Fast Food","Indian"] * 5,
        "city": ["Ahmedabad","Surat","Ahmedabad","Vadodara"] * 5,
        "delivery_time_mins": [
            30,40,25,35,32,42,28,36,31,39,
            27,34,33,41,29,37,35,43,30,38
        ],
        "order_value": [
            250,500,220,400,280,550,300,450,270,520,
            240,390,310,600,260,420,290,580,230,410
        ],
        "rating": [
            4.2,4.4,3.9,4.3,4.1,4.6,4.0,4.2,4.4,4.5,
            3.8,4.3,4.2,4.7,4.0,4.1,4.3,4.6,3.9,4.2
        ]
    })

    cleaned_df.loc[2, "delivery_time_mins"] = np.nan
    cleaned_df.loc[5, "order_value"] = np.nan
    cleaned_df.loc[8, "rating"] = np.nan

    print("BEFORE CLEANING")
    print(cleaned_df.isnull().sum())

    cleaned_df["delivery_time_mins"] = cleaned_df[
        "delivery_time_mins"
    ].fillna(cleaned_df["delivery_time_mins"].median())

    cleaned_df["order_value"] = cleaned_df[
        "order_value"
    ].fillna(cleaned_df["order_value"].median())

    cleaned_df["rating"] = cleaned_df[
        "rating"
    ].fillna(round(cleaned_df["rating"].mean(), 1))

    cleaned_df = cleaned_df.drop_duplicates()

    q1 = cleaned_df["order_value"].quantile(0.25)
    q3 = cleaned_df["order_value"].quantile(0.75)
    iqr = q3 - q1
    upper = q3 + 1.5 * iqr

    cleaned_df["order_value"] = cleaned_df[
        "order_value"
    ].clip(upper=upper)

    print("AFTER CLEANING")
    print(cleaned_df.isnull().sum())


def run_sql_analysis():
    global sql_report

    conn = sqlite3.connect("food_delivery.db")

    query = """
    SELECT
        r.name AS restaurant_name,
        r.category,
        r.city,
        COUNT(o.order_id) AS total_orders,
        SUM(o.order_value) AS total_revenue,
        ROUND(AVG(o.rating), 2) AS avg_rating
    FROM restaurants r
    LEFT JOIN orders o
    ON r.restaurant_id = o.restaurant_id
    GROUP BY r.restaurant_id, r.name, r.category, r.city
    """

    sql_report = pd.read_sql_query(query, conn)
    print(sql_report)

    join_query = """
    SELECT r.name AS restaurant_name,
           o.order_id,
           o.order_value,
           o.delivery_time_mins,
           o.rating
    FROM restaurants r
    JOIN orders o
    ON r.restaurant_id = o.restaurant_id
    """

    print(pd.read_sql_query(join_query, conn))
    conn.close()


def view_charts():
    if cleaned_df is None:
        print("Please run Option 1 first.")
        return

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    sns.countplot(
        data=cleaned_df,
        x="category",
        ax=axes[0]
    )
    axes[0].set_title("Orders by Category")
    axes[0].set_xlabel("Category")
    axes[0].set_ylabel("Order Count")

    city_data = cleaned_df.groupby(
        "city",
        as_index=False
    )["delivery_time_mins"].mean()

    sns.barplot(
        data=city_data,
        x="city",
        y="delivery_time_mins",
        ax=axes[1]
    )
    axes[1].set_title("Average Delivery Time by City")
    axes[1].set_xlabel("City")
    axes[1].set_ylabel("Average Delivery Time")

    plt.tight_layout()
    plt.show()


def export_report():
    if cleaned_df is None or sql_report is None:
        print("Please run Option 1 and Option 2 first.")
        return

    with pd.ExcelWriter("food_delivery_report.xlsx") as writer:
        cleaned_df.to_excel(
            writer,
            sheet_name="Cleaned Data",
            index=False
        )
        sql_report.to_excel(
            writer,
            sheet_name="SQL Analysis",
            index=False
        )

    print("Report exported to food_delivery_report.xlsx")


while True:
    print("\nFOOD DELIVERY ANALYTICS")
    print("1. Load & Clean Data")
    print("2. Run SQL Analysis")
    print("3. View Charts")
    print("4. Export Report")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        load_and_clean_data()
    elif choice == "2":
        run_sql_analysis()
    elif choice == "3":
        view_charts()
    elif choice == "4":
        export_report()
    elif choice == "0":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")


# ============================================================
# SECTION D – AI-AUGMENTED LEARNING
# ============================================================

# STEP 1 – BUILD WITH AI

# QUESTION:
# Use an AI tool to build a program that connects to a SQLite orders table with
# order_id, restaurant_name, category, order_value, rating and delivery_time_mins.
# Find the top 3 restaurants by average rating, exclude restaurants with fewer
# than 5 orders, load into Pandas, calculate revenue share among the top 3, create
# a horizontal rating chart with revenue-share labels, and handle a missing
# database or empty result without crashing.



# AI ORIGINAL CODE:
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("food_delivery.db")

query = """
SELECT restaurant_name,
       COUNT(*) AS total_orders,
       SUM(order_value) AS total_revenue,
       AVG(rating) AS avg_rating
FROM orders
GROUP BY restaurant_name
HAVING COUNT(*) >= 5
ORDER BY avg_rating DESC
LIMIT 3
"""

df = pd.read_sql_query(query, conn)
total_revenue = df["total_revenue"].sum()

df["revenue_share_percent"] = (
    df["total_revenue"] / total_revenue * 100
)

plt.barh(df["restaurant_name"], df["avg_rating"])
plt.xlabel("Average Rating")
plt.ylabel("Restaurant")
plt.title("Top 3 Restaurants by Average Rating")

for i, value in enumerate(df["revenue_share_percent"]):
    plt.text(df["avg_rating"].iloc[i], i, f"{value:.1f}%")

plt.tight_layout()
plt.show()
conn.close()


# STEP 2 – TEST & DEBUG WITHOUT AI

# QUESTION:
# Find at least one bug, limitation or improvement in the AI solution and fix it
# yourself.

# ANSWER – CORRECTED VERSION:
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

db_file = "food_delivery.db"

if not os.path.exists(db_file):
    print("Database file not found. Please create food_delivery.db first.")
else:
    conn = sqlite3.connect(db_file)

    query = """
    SELECT restaurant_name,
           COUNT(*) AS total_orders,
           SUM(order_value) AS total_revenue,
           ROUND(AVG(rating), 2) AS avg_rating
    FROM orders
    GROUP BY restaurant_name
    HAVING COUNT(*) >= 5
    ORDER BY avg_rating DESC
    LIMIT 3
    """

    df = pd.read_sql_query(query, conn)

    if df.empty:
        print("No restaurant data was found for the analysis.")
    else:
        total_revenue = df["total_revenue"].sum()

        if total_revenue == 0:
            df["revenue_share_percent"] = 0
        else:
            df["revenue_share_percent"] = (
                df["total_revenue"] / total_revenue * 100
            )

        plt.barh(df["restaurant_name"], df["avg_rating"])
        plt.xlabel("Average Rating")
        plt.ylabel("Restaurant")
        plt.title("Top 3 Restaurants by Average Rating")

        for i in range(len(df)):
            plt.text(
                df["avg_rating"].iloc[i],
                i,
                f"Revenue Share: "
                f"{df['revenue_share_percent'].iloc[i]:.1f}%"
            )

        plt.tight_layout()
        plt.show()

    conn.close()



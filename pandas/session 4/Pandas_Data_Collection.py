# SESSION 4 - Data Collection using Pandas (Part 1)


# Task 1 - IPL Cricket Match Scores

import pandas as pd

ipl_data = pd.read_csv("ipl.csv")

print("First 5 IPL Rows:")
print(ipl_data.head())


# Task 2 - Trending Songs JSON

songs_data = pd.read_json("trending_songs.json")

print("\nTrending Songs Information:")
songs_data.info()


# Task 3 - Zomato TSV Data

zomato_data = pd.read_csv("zomato.tsv", sep="\t")

print("\nZomato Summary Statistics:")
print(zomato_data.describe(include="all"))


# Task 4 - Flipkart Large Excel File

flipkart_data = pd.read_excel("flipkart_products.xlsx")

for start in range(0, len(flipkart_data), 2000):
    chunk = flipkart_data.iloc[start:start + 2000]
    print("Rows in this chunk:", len(chunk))

# Task 5 - Paytm Transactions

paytm_data = pd.read_csv(
    "paytm_transactions.csv",
    sep=";"
)

null_counts = paytm_data.isnull().sum()

print("\nPaytm Null Values:")
print(null_counts)

print("\nColumns Having Null Values:")

for column in paytm_data.columns:
    if paytm_data[column].isnull().sum() > 0:
        print(column)

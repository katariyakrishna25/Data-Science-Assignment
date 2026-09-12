# Task 1
def get_song_duration_per_minute(total_duration, num_songs):
    try:
        result = total_duration / num_songs
        print("Average song duration:", result, "minutes")
    except ZeroDivisionError:
        print("Error: Number of songs cannot be zero.")
    finally:
        print("Song duration calculation done")


get_song_duration_per_minute(120, 10)


# Task 2
total_cart = float(input("Enter total cart amount: "))
item_count = int(input("Enter number of items: "))

try:
    price_per_item = total_cart / item_count
    print("Price per item:", price_per_item)
except ZeroDivisionError:
    print("Error: Item count cannot be zero.")


# Task 3
class NoOffersApplied(Exception):
    pass


total_spend = float(input("Enter total spend: "))
offers = int(input("Enter number of offers applied: "))

try:
    if offers == 0:
        raise NoOffersApplied("No offers were applied.")
    
    cashback = total_spend / offers
    print("Average cashback per offer:", cashback)

except NoOffersApplied as e:
    print("Error:", e)


# Task 4
def calculate_average_rating(total_rating, num_reviews):
    try:
        return total_rating / num_reviews
    except ZeroDivisionError:
        print("Error: Number of reviews cannot be zero.")
        return 0
    finally:
        print("Thank you for using the calculator")


print(calculate_average_rating(500, 0))


# Task 5
def safe_divide_for_zomato(bill_amount, people):
    try:
        result = bill_amount / people
    except ZeroDivisionError:
        print("Error: Number of people cannot be zero.")
    else:
        print("Amount per person:", result)
    finally:
        print("Split calculation done")


safe_divide_for_zomato(1000, 4)
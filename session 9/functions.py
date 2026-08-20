# Task 1: Calculate final price

def calculate_final_price(price, discount_rate):
    discount = price * discount_rate / 100
    return price - discount

print(calculate_final_price(500, 10))


# Task 2: Delivery charge

def get_delivery_charge(amount, city="Ahmedabad"):
    if city == "Ahmedabad":
        return 0
    else:
        return 50

print(get_delivery_charge(500))
print(get_delivery_charge(500, "Mumbai"))


# Task 3: Format price

def format_price(price, currency="INR"):
    if currency == "INR":
        return "₹" + str(price)
    else:
        return "$" + str(price)

print(format_price(500))
print(format_price(500, "USD"))


# Task 4: Apply coupon

def apply_coupon(price, coupon_code=None):
    if coupon_code == "ZOMATO10":
        return price - (price * 10 / 100)
    else:
        return price

print(apply_coupon(500))
print(apply_coupon(500, "ZOMATO10"))
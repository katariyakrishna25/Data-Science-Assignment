# SESSION 4 - Strings

# 1 . use string methods to convert is lowercase() and replace() and print .

text = "Flipkart-Sale2024"

text = text.lower()
text = text.replace("-", " ")

print(text)


# 2 . removing extra spaces and converting all letters uppercase,strip and replace .

product_name = "  OnePlus Nord-CE 3  "

product_name = product_name.strip()
product_name = product_name.upper()
product_name = product_name.replace("-", ":")

print(product_name)


# 3 . string like 'ZOMATO-FOOD-2024' and returns a list of its parts using the split() method. 

def split_product_code(product_code):
    return product_code.split("-")


product_code = "ZOMATO-FOOD-2024"

result = split_product_code(product_code)

print(result)


# 4 .  use string slicing to extract and print only the word 'Premium'.

text = "Spotify_Premium_Offer"

premium = text[8:15]

print(premium)


# 5 .  using string formatting.

product = "Myntra Shirt"
price = 799.5

print(f"Deal: {product} is available at ₹{price} only!")
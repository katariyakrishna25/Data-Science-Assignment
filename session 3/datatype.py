#data type in python topics 
# 1. variable in python and use the use the type() function to display.

age =10
height=151.10
name="krishna"
spotify=True

print(age,type(age))
print(height,type(height))
print(name,type(name))
print(spotify,type(spotify))

# 2. write a funcation total_cart_amout(price) and use float() convert into string .

def total_cart_amout(prices):
    total=0

    for price in prices:
        total = total + float(price)

    return total 

prices=['199.99', '49', '350.75']

result = total_cart_amout(prices)

print("total cart amount",result) 


# 3.input their cricket score as a string .

cricket_score = input("enter your cricket score :")

cricket_score = int(cricket_score)

if cricket_score >= 50 :
    print("Half-century !")
else :
    print("Keep going")


# 4 . the variable is_premium code convert into boolean and print its type .

is_premium = "True"

is_premium = is_premium == "True"

print(is_premium)
print(is_premium,type(is_premium))
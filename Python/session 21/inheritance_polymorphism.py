# SESSION 21 - Inheritance & Polymorphism


# TASK 1 - Product Class

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price - (self.price * 10 / 100)


product = Product("Shoes", 1000)

print("Product:", product.name)
print("Discounted Price:", product.get_discounted_price())


# TASK 2 - Electronics Class

class Electronics(Product):

    def get_discounted_price(self):
        return self.price - (self.price * 20 / 100)


electronics = Electronics("Headphones", 2000)

print("Electronics:", electronics.name)
print("Discounted Price:", electronics.get_discounted_price())


# TASK 3 - Polymorphism

def show_final_price(item):
    print("Product:", item.name)
    print("Final Price:", item.get_discounted_price())


print("\nPolymorphism Example:")

show_final_price(product)
show_final_price(electronics)


# TASK 4 - Ticket Class

class Ticket:
    def __init__(self, price):
        self.price = price

    def get_final_price(self):
        return self.price


class PremiumTicket(Ticket):

    def get_final_price(self):
        return super().get_final_price() + 50


ticket = Ticket(200)
premium_ticket = PremiumTicket(200)

print("\nMovie Ticket:")
print("Normal Ticket Price:", ticket.get_final_price())

print("Premium Ticket Price:", premium_ticket.get_final_price())
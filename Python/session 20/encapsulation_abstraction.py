# SESSION 20 - Encapsulation & Abstraction


# TASK 1 - Playlist Class

class Playlist:
    def __init__(self):
        self._songs = []

    def add_song(self, song):
        self._songs.append(song)

    def show_playlist(self):
        print("Playlist:", self._songs)


playlist = Playlist()

playlist.add_song("Tum Hi Ho")
playlist.add_song("Kesariya")
playlist.add_song("Apna Bana Le")

playlist.show_playlist()


# TASK 2 - Product Class

class Product:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price


product = Product(500)

print("Original Price:", product.get_price())

product.set_price(600)

print("Updated Price:", product.get_price())


# TASK 3 - Movie Class

class Movie:
    def __init__(self, rating):
        self._rating = 0
        self.set_rating(rating)

    def get_rating(self):
        return self._rating

    def set_rating(self, rating):
        if 0 <= rating <= 10:
            self._rating = rating
        else:
            print("Error: Rating must be between 0 and 10.")


movie = Movie(8.5)

print("Movie Rating:", movie.get_rating())

movie.set_rating(9)

print("Updated Rating:", movie.get_rating())

movie.set_rating(12)


# TASK 4 - Abstraction

from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class Paytm(PaymentMethod):

    def pay(self, amount):
        print("Paytm payment of Rs.", amount, "successful.")


class PhonePe(PaymentMethod):

    def pay(self, amount):
        print("PhonePe payment of Rs.", amount, "successful.")


paytm = Paytm()
phonepe = PhonePe()

paytm.pay(500)
phonepe.pay(750)
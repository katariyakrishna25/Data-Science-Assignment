# Task 1: Song Class


class Song:

  def __init__(self, title, artist, duration):
    self.title = title
    self.artist = artist
    self.duration = duration


fav_song = Song("Bohemian Rhapsody", "Queen", 354)
print(
    f"Title: {fav_song.title}, Artist: {fav_song.artist}, Duration:"
    f" {fav_song.duration}s"
)


# Task 2: Add play_preview Method



class SongWithPreview:

  def __init__(self, title, artist, duration):
    self.title = title
    self.artist = artist
    self.duration = duration

  def play_preview(self):
    print(f"Playing 30-second preview of {self.title} by {self.artist}")


fav_song_preview = SongWithPreview("Bohemian Rhapsody", "Queen", 354)
fav_song_preview.play_preview()




# Task 3: FoodOrder Class


class FoodOrder:

  def __init__(self, restaurant_name, items, total_price):
    self.restaurant_name = restaurant_name
    self.items = items
    self.total_price = total_price


order = FoodOrder(
    "Punjabi Tadka", ["Paneer Butter Masala", "Butter Naan"], 420
)
print(f"Restaurant: {order.restaurant_name}")
print(f"Items: {order.items}")
print(f"Total: Rs. {order.total_price}")



# Task 4: Extend FoodOrder with add_item

class FoodOrderExtended:

  def __init__(self, restaurant_name, items, total_price):
    self.restaurant_name = restaurant_name
    self.items = items
    self.total_price = total_price

  def add_item(self, item_name, item_price):
    self.items.append(item_name)
    self.total_price += item_price


order_ext = FoodOrderExtended(
    "Punjabi Tadka", ["Paneer Butter Masala", "Butter Naan"], 420
)
order_ext.add_item("Gulab Jamun", 80)
order_ext.add_item("Lassi", 60)
print(f"Updated Items: {order_ext.items}")
print(f"Updated Total: Rs. {order_ext.total_price}")



# Task 5: Refactor Song with Optional Duration


class SongOptionalDuration:

  def __init__(self, title, artist, duration=0):
    self.title = title
    self.artist = artist
    self.duration = duration


song1 = SongOptionalDuration("Shape of You", "Ed Sheeran", 233)
song2 = SongOptionalDuration("Unknown Melody", "Indie Artist")

print(f"{song1.title}: {song1.duration}s")
print(f"{song2.title}: {song2.duration}s (default)")
# Task 1: Recursive Playlist

def print_playlist_songs(songs):
    if len(songs) == 0:
        return

    print(songs[0])
    print_playlist_songs(songs[1:])


songs = ["Shape Of You", "Believer", "Perfect", "Senorita"]

print_playlist_songs(songs)


# Task 2: Recursive Unread Messages

def count_unread_messages(messages):
    total = messages.get("count", 0)

    for group in messages.get("subgroups", []):
        total += count_unread_messages(group)

    return total


messages = {
    "count": 5,
    "subgroups": [
        {
            "count": 3,
            "subgroups": []
        },
        {
            "count": 4,
            "subgroups": [
                {
                    "count": 2,
                    "subgroups": []
                }
            ]
        }
    ]
}

print("Total unread messages:", count_unread_messages(messages))


# Task 3: Local and Global Variables

x = "global"

def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"

    inner()
    print("Inside outer:", x)


outer()
print("Outside:", x)

# x = "global" is a global variable.
# x = "outer" is a local variable of outer().
# nonlocal x changes outer's x to "inner".
# Output:
# Inside outer: inner
# Outside: global


# Task 4: Recursive Number Formatting

def format_number_short(n):
    if n >= 1000000:
        return str(round(n / 1000000, 1)) + "M"
    elif n >= 1000:
        return str(round(n / 1000, 1)) + "K"
    else:
        return str(n)


print(format_number_short(1500))
print(format_number_short(1200000))
print(format_number_short(500))
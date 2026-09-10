import re

# Task 1: Extract Phone Numbers

text1 = "Call +91-9876543210 or +91-9123456789. Ignore +91-123."
phone_numbers = re.findall(r"\+91-\d{10}", text1)
print("Phone Numbers:", phone_numbers)


# Task 2: Validate Date (DD/MM/YYYY)


def check_date(text):
    return bool(
        re.search(r"\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b", text)
    )


print("Is valid date present?:", check_date("Meeting on 15/08/2024"))


# Task 3: Extract Prices and Calculate Sum


text3 = "Book: Rs. 299, Pen: Rs. 45, Bag: Rs. 1500"
prices = [int(p) for p in re.findall(r"Rs\.\s*(\d+)", text3)]
print("Prices found:", prices)
print("Total Sum:", sum(prices))


# Task 4: Mask Email Addresses


text4 = "Contact support@example.com or admin123@work.org for help."
hidden_text = re.sub(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "[hidden email]",
    text4,
)
print("Masked Text:", hidden_text)


# Task 5: Instagram Usernames


comments = """
1. Great shot @alex_travels!
2. Thanks @john_doe
3. Follow @photo_lover for more
4. DM sent @maria_design
5. Too short @ab
6. Awesome @alex_travels
7. Superb @nature_hub
8. Nice @travel_bug_99
9. Tagging @maria_design
10. Cheers @dev_team_2024
"""

with open("comments.txt", "w") as f:
    f.write(comments.strip())

with open("comments.txt", "r") as f:
    content = f.read()

unique_users = sorted(set(re.findall(r"@([A-Za-z0-9_]{3,})\b", content)))
print("Unique Usernames:", ["@" + u for u in unique_users])
# =====================================
# 1. Function with *args
# =====================================


# def total_marks(*scores):
#     return sum(scores)


# print(total_marks(55, 3, 7, 3))
# print(total_marks(50))
# print(total_marks())


# =====================================
# 2. Function with Default Arguments
# =====================================


# def book_ticket(name, seat_type="Economy"):
#     return f"{name} booked a {seat_type} seat."


# print(book_ticket("dattu"))
# print(book_ticket("shreya", "Business"))
# print(book_ticket(name="Riya", seat_type="First class"))


# =====================================
# 3. Function with Default Arguments + *args
# =====================================


# def calculate_total(price, tax_rate=0.18, *discount):
#     total = (price - sum(discount)) * (1 + tax_rate)
#     return total


# print(calculate_total(1000, 0.18, 50, 100))
# print(calculate_total(500))


# =====================================
# 4. Discount Calculator Challenge
# =====================================

# def apply_discount(price, discount_percent=10, *extra_flat_discount):
#     discount_amount = (price * discount_percent) / 100
#     remaining = price - discount_amount
#     remaining = remaining - sum(extra_flat_discount)
#     return round(remaining, 2)

# print(apply_discount(2000, 20, 100, 50))
# print(apply_discount(1000))


# Thik ahe. **kwargs test karूया:

# Question:

# Function lihi student_profile(name, **details) je:

# name (required) ghete
# **details madhे kितीही keyword arguments (jasे age=20, city="Sholapur", course="Python") ghete
# Return karте ek string: "<name>'s profile: " त्यानंतर pratyek key-value pair key: value format madhे, comma ने separated

# Example: student_profile("Dattu", age=20, city="Sholapur")
# → Return: "Dattu's profile: age: 20, city: Sholapur"


# Hint: **kwargs ek dictionary asते, tयामुळे .items() वापरून loop karता येईल key-value pairs काढण्यासाठी.
def student_profile(name, **details):
    profile = []

    for key, value in details.items():
        profile.append(f"{key}: {value}")

    return f"{name}'s profile: {', '.join(profile)}"


print(student_profile("Dattu", age=20, city="Allapalli"))

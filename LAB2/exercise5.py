"""
Create a list of dictionaries representing four products.
Each dictionary must contain a product name, price, and quantity.
Use a loop to calculate the total cost. Write a function named apply_discount(total) that applies a
10% discount when the total is at least 2,000. Otherwise, return the original total.

"""
products = [
    {"name": "Laptop", "price": 80000, "quantity": 1},
    {"name": "Mouse", "price": 500, "quantity": 2},
    {"name": "Keyboard", "price": 1500, "quantity": 1},
    {"name": "Headphone", "price": 2000, "quantity": 1}
]

total = 0

for product in products:
    total += product["price"] * product["quantity"]

def apply_discount(total):
    if total >= 2000:
        return total * 0.90
    else:
        return total

final_total = apply_discount(total)

print("Total cost:", total)
print("Final cost after discount:", final_total)
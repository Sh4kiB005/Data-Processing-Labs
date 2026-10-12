""" 
Calculate each product’s line total using price *
quantity. Calculate the total inventory value and identify the product with the highest line total.

"""
products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]

total = 0
highest = 0
highest_product = ""

for product in products:
    line_total = product["price"] * product["quantity"]

    print(product["name"], "Line total:", line_total)

    total += line_total

    if line_total > highest:
        highest = line_total
        highest_product = product["name"]

print("Total inventory value:", total)
print("Product with highest line total:", highest_product)
print("Highest line total:", highest)
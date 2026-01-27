inventory ={
    "Laptop": (999.99, 5),
"Mouse": (29.99, 15),
"Keyboard": (79.99, 10),
"Monitor": (299.99, 8)
}

print("=== Current Inventory ===")

for item, (price, quantity) in inventory.items():
    print(f"{item}: -  Price: ${price} - Quantity: {quantity}")

electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}
union_set =accessories.union(electronics)
print("All product categories:", union_set )

prices = [price for price, quantity in inventory.values()]
print("Price List:", prices)
prices.sort()
print("Sorted prices:", prices)
print("Lowest price:", prices[1])
print("Highest price:", prices[3])

print("===Final Inventory===")
inventory["Headphones"] = (49.99, 20)
price, _ = inventory["Mouse"]
inventory["Mouse"] = (price, 12)
del inventory["Monitor"]
print("=== Updated Inventory ===")
for item, (price, quantity) in inventory.items():
    print(f"{item}: ${price} - Quantity: {quantity}")

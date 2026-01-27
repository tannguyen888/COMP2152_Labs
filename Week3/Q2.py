print("=" * 50)
print("Question 2: Shopping Cart")
print("=" * 50)

cart = ["apple", "banana", "silk", "bread", "apple", "eggs"]

apple_count = cart.count("apple")
print("Number of apple:", apple_count)
milk_position = cart.index(milk)
print("Position of milk:", milk_position)
remove_item = cart.pop(math.random())
print("Remove item using pop:", remove_item)
print("Is banana in the cart?", "banana" in cart)
print("Final cart:", cart)
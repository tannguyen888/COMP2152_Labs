monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")
print("Monday Class:", monday_class)
print("Wednesday Class:", wednesday_class)
attend_both = monday_class.intersection(wednesday_class)
print("Attend both classes:", attend_both)
attend_either = monday_class.union(wednesday_class)
print("Attend either class:", attend_either)


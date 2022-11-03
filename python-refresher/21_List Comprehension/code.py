numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

print(doubled)

friends = ["Rolf", "Anna", "Saven", "Saurabh", "Jen"]

# not so easy to type and think of...
starts_s = [f for f in friends if f.startswith("S")]

print(starts_s)

# id of objects is related to memory address in which list is stored,
# important function for later in the course!
print (f"friends: {id(friends)} starts_s: {id(starts_s)}")
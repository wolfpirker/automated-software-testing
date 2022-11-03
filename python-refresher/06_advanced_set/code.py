friends = {"Bob", "Rolf", "Anna"}
abroad = {"Bob", "Anna"}

# difference: takes one sets and takes the difference to another
local_friends = friends.difference(abroad)

print(f"local friends {local_friends}")

local = {"Rolf"}
abroad = {"Bob", "Anna"}

# friends = ...
# If we have 1 local friend and 2 abroad friends, we could calculate the total friends by using `.union`

friends = local.union(abroad)
print(friends)

# other method: intersection
# to create a intersection of sets!
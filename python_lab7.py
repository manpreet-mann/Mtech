# 7. Write a Python program to create, access, update and delete tuples.
#  Write a Python program to create, access, update and delete sets.

# 1. Create a tuple
t = (10, 20, 30, 40, 50)
print("Original tuple:", t)

# 2. Access tuple elements
print("First element:", t[0])
print("Third element:", t[2])
print("Last element:", t[-1])

# 3. Update a tuple
# Convert tuple into a list, modify it, and convert back
temp = list(t)
temp[1] = 25
t = tuple(temp)
print("Updated tuple:", t)

# 4. Delete an element (create a new tuple without it)
t = t[:2] + t[3:]
print("Tuple after deleting an element:", t)

# 5. Delete the entire tuple
del t
print("Tuple deleted successfully")

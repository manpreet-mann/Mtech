# Program to create, access, update and delete a list
fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Original list:", fruits)

print("First element:", fruits[0])
print("Second element:", fruits[1])

# Updating an element
fruits[1] = "Grapes"
print("After updating:", fruits)

# Adding an element
fruits.append("Pineapple")
print("After adding:", fruits)

# Deleting an element
fruits.remove("Mango")
print("After deleting Mango:", fruits)

# Deleting an element using index
del fruits[0]
print("After deleting first element:", fruits)


# Real-life example: Shopping List
shopping_list = ["Milk", "Bread", "Eggs", "Rice"]

print("\nReal-life Shopping List:")
print(shopping_list)

# Access
print("Item to buy:", shopping_list[2])

# Update
shopping_list[1] = "Brown Bread"

# Add
shopping_list.append("Fruits")

# Delete
shopping_list.remove("Rice")

print("Updated Shopping List:", shopping_list)
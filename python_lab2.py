a = 10
b = 3

# 1. Arithmetic Operators
print("Arithmetic Operators")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)


# 2. Comparison Operators
print("\nComparison Operators")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# 3. Assignment Operators
print("\nAssignment Operators")
x = 10
x += 5
print(x)

x -= 2
print(x)

x *= 2
print(x)

x /= 2
print(x)


# 4. Logical Operators
print("\nLogical Operators")
print(a > 5 and b < 5)
print(a > 5 or b > 5)
print(not(a > 5))


# 5. Bitwise Operators
print("\nBitwise Operators")
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)


# 6. Membership Operators
print("\nMembership Operators")
numbers = [1, 3, 5, 10]
print(10 in numbers)
print(7 not in numbers)


# 7. Identity Operators
print("\nIdentity Operators")
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)
print(x is z)
print(x is not z)
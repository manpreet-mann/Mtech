# Conditional Statements

marks = int(input("Enter your marks: "))

# if statement
if marks >= 40:
    print("You have passed.")


# if-else statement
if marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail") 


# if-elif-else statement
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")
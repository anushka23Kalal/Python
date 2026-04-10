# --------  CONDITIONAL STATEMENTS --------

marks = int(input("Enter marks: "))

# if condition
if marks >= 90:
    print("Grade A")

# if-elif-else condition
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

print("\n---------------------\n")


# Checking even or odd number

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# POSITIVE / NEGATIVE CHECK


num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

print("\n=============================\n")

# MENU DRIVEN CALCULATOR

print("Calculator Menu")
print("1. Addition 2. Subtraction 3. Multiplication 4. Division ")
choice = int(input("Enter your choice: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print("Result:", a + b)

elif choice == 2:
    print("Result:", a - b)

elif choice == 3:
    print("Result:", a * b)

elif choice == 4:
    print("Result:", a / b)

else:
    print("Invalid choice")

    print("\n------------------------\n")


# Q1. Variables and Data Types

name = "Anas"
age = 19
height = 5.8
is_student = True

print("\n--- Q1: Variables and Data Types ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

print("Name Type:", type(name))
print("Age Type:", type(age))
print("Height Type:", type(height))
print("Student Type:", type(is_student))


# Q2. Arithmetic Operators

num1 = 20
num2 = 10

print("\n--- Q2: Arithmetic Operators ---")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)
print("Power:", num1 ** 2)


# Q3. Comparison Operators

a = 15
b = 10

print("\n--- Q3: Comparison Operators ---")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)


# Q4. Logical Operators

age = 20
has_id = True

print("\n--- Q4: Logical Operators ---")
print("AND:", age >= 18 and has_id == True)
print("OR:", age >= 18 or has_id == False)
print("NOT:", not has_id)


# Q5. Check Even or Odd Number

print("\n--- Q5: Even or Odd ---")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Q6. Check Positive, Negative or Zero

print("\n--- Q6: Positive, Negative or Zero ---")

number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Number is Zero")


# Q7. Voting Eligibility

print("\n--- Q7: Voting Eligibility ---")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# Q8. Find Largest of Two Numbers

print("\n--- Q8: Largest Number ---")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("First number is largest")
elif num2 > num1:
    print("Second number is largest")
else:
    print("Both numbers are equal")


# Q9. Student Grade System

print("\n--- Q9: Student Grade System ---")

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Fail")


# Q10. Simple Calculator

print("\n--- Q10: Simple Calculator ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Operator")


# Assignment Completed

print("\nCongratulations! Assignment 2 Completed.")
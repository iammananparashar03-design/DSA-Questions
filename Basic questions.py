'''
Question 1:
Program to calculate electricity bill with the following information:
- Units: 100 units, 101 to 300 units, above 300 units
- Respective prices: ₹3 per unit, ₹4 per unit, and ₹5 per unit
Question 2: Write a program to check whether a given number is even or odd. 
Question 3: Write a program to find the largest and smallest of three numbers. 
Question 4: Grade the following students with the following remarks:
- Students having marks 90 to 100 will be remarked as excellent.
- 70 to 90 to be remarked as very good.
- 60 to 70 to be remarked as good.
- 50 to 60 to be remarked as fair.
- Below 50 to be remarked as poor.
Question number 5: Write a program for printing out tables from 1 to n, 
where n is taken from the user as an input. 
'''
# Question 1:
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 3
elif units <= 300:
    bill = 100 * 3 + (units - 100) * 4
else:
    bill = 100 * 3 + 200 * 4 + (units - 300) * 5

print(f"Total bill: ₹{bill}")

# Question 2:
n = int(input("Enter a number: "))
print(f"{n} is", "even" if n % 2 == 0 else "odd")

# Question 3:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = max(a, b, c)
smallest = min(a, b, c)

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")

# Question 4:
marks = float(input("Enter marks: "))

if 90 <= marks <= 100:
    print("Excellent")
elif 70 <= marks < 90:
    print("Very Good")
elif 60 <= marks < 70:
    print("Good")
elif 50 <= marks < 60:
    print("Fair")
else:
    print("Poor")

# Question 5:
n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    print(f"Table of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()
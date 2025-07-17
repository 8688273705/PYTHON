# largest ex 2
a = input("Enter three numbers separated by commas (e.g., 10,20,30): ")
x, y, z = a.split(",")
num1 = int(x)
num2 = int(y)
num3 = int(z)

# Find the greatest number
great = num1
if num2 > great:
    great = num2
if num3 > great:
    great = num3

print("The greatest number is:", great)
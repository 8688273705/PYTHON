a = input("Enter three numbers separated by commas: ")
x, y, z = a.split(",")
num1 = int(x)
num2 = int(y)
num3 = int(z)
great = num1
if num1>num2:
    if num1>num3:
        great = num2
    else:
        great = num3
elif num2>num1:
    if num2>num3:
        great = num2
    else:
        great = num3
elif num3>num1:
    if num3>num2:
        great = num3
    else:
        great = num2
print(great)
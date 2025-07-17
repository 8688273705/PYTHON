# input statement :
# Example 7 in
# 10,5
x,y =input("Enter a and b values:").split(",")
a = int(x)
b = int(y)
print("Addition:",a+b,",Subtraction:",a-b,",Multiplication:",a*b,",Division:",a/b,sep = "")
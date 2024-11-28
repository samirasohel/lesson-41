#Write a Python program to create a calculator. 
# Create individual functions for different operators - addition, subtraction, division, multiplication and return the output value.

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def duv(a,b):
    return a/b
def prod(a,b):
    return a*b

num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))

print("sum of",num1,"and",num2,"is",add(num1,num2))
print("defference of",num1,"and",num2,"is",sub(num1,num2))
print("Quotient",num1,"and",num2,"is",duv(num1,num2))
print("product of",num1,"and",num2,"is",prod(num1,num2))
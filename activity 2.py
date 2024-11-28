#Write a Python program that finds the factorial of a number using recursion and returns the result. (Example - If number = 5, factorial = 5*4*3*2*1 = 120)

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter a number"))
if(num<0):
    print("Cannot find factorial for negative number")
elif num==0:
    print("Factorial of o is 1")
else:
    print("Factorial of",num,"is",fact(num)) 
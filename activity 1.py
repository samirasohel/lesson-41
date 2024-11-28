#Write a Python program that takes a name as an input from the user and then creates a function that accepts the same name as a parameter and introduces the user.

def intro(n):
    print("Hello, My Name is",n)
name=input("Enter your name")
intro(name)
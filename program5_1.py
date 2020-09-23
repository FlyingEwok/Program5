''' Create a function that can accept two arguments name and age and print its value'''

def myFunction(name, age):
    print("Hello, your name is %s, and you're %s years old."%(name, age))

myFunction(input("Enter your name: "), input("Enter your age: "))
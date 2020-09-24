''' Create a function that can accept two arguments name and age and print its value'''

#Create function that prints a senetnce with variables that user sets when function is called
def myFunction(name, age):
    print("Hello, your name is %s, and you're %s years old."%(name, age))

#Call my function
myFunction(input("Enter your name: "), input("Enter your age: "))
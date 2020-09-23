'''Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call'''

print("This program uses a function to add and subtract x and y the spit out the answer for both of them.")

def calculation(x, y):
    return x + y, x - y

#Put into variables for nicer looking print statement
x = (int(input("Enter a X value: ")))
y = (int(input("Enter a Y value: ")))

#Print the outcome
print(calculation(x, y))

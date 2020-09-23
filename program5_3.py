'''Create an inner function to calculate the addition in the following way'''

#print program purpose 
print("This program takes 2 numbers entered by the user and adds them together then to add 5 to the sum of those 2 numbers.")

#Make the function to calculate everything
def additionouterfunc(a, b):
    def additioninnerfunc():
        return a + b
    return additioninnerfunc() + 5

#put into variable to make print statement look nicer
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

#Print the value
print(additionouterfunc(a, b))

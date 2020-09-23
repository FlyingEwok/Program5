'''Write a Python function to multiply all the numbers in a list.'''

#Print program purpose
print("This program will ask you to create a list of numbers and then multiply all numbers in that list with eachother.")


#Make function that multiplies all numbers in a list with eachother
def multiplynuminList(MyList):
    #Multiply elements one by one
    result = 1
    for x in MyList:
        result = result * x
    return result

#Make a list of user inputed numbers
list1 = []

#Ask user to enter numbers until they're done
while True:
  list1.append(int(input("Enter a number: ")))
  i = input("Type done if done otherwise press enter to continue: ")
  if i == "done":
    break
  else:
    continue

print("This is the list: ", list1)

#use function to multiply all numbers in this list
print("This is all the values in the list multiplied together: ", (multiplynuminList(list1)))
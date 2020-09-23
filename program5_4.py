'''Write a Python function to multiply all the numbers in a list.'''

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

print(multiplynuminList(list1))
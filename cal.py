#we are making a small calculator
#we are going to add, subtract, multiply, divide
#we are making a small calculator
#we are going to add, subtract, multiply, divide

print("AMAN's CAlCULATOR")

print("Press 1. for adiition")
print("Press 2. for subtraction")
print("Press 3. for multiplication")
print("press 4. for division")

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
x=int(input("Enter your choice:"))

match x:
  case 1:
    c=a+b
    print("The Addition  of the numbers is",c)
  case 2:
    c=a-b
    print("The substraction of the numbers is",c)
  case 3:
    c=a*b
    print("The multiplication of the numbers is",c)
  case 4:
    c=a/b
    print("The division of the numbers is",c)
  case _:
    print("Wrong choice")

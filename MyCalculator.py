#magic calculator
print("press 1. for addition")
print("press 2. for substraction")
print("press 3. for multiplication")
print("press 4. for division ")
a=int(input ("enter the first number"))
b=int(input("enter the secand number"))
x=int(input("enter your choice:"))

match x:
  case 1:
  c=a+b
  print("the addition of two numbers is:",c)
  case 2:
  c=a-b
  print ("the substraction of the number is:",c)
  case 3:
  c=a*b
  print("the multiplication  of the number is:",c)
  case 4:
  c=a/b
  print("the division of the number is:",c)
  case_:
  print("invalid coice")

age = int(input("Enter your age: "))

if age < 21:
    print("You are a teenager.")
elif age >= 21 and age < 60:
    print("You are an adult.")
else:
    print("You are old.")

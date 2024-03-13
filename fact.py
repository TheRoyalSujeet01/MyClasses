def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    print("Factorial of {} is: {}".format(n, s))
n = int(input("Enter your number: "))
fact(n)

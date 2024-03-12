Start_From = int(input("Enter Start Range "))
End_Num = int(input("Enter End Range "))
total_sum = 0
n = int(input("Enter the number by which you divide "))
for num in range(Start_From, End_Num+1):
    if num % n == 0:
        total_sum += num
print("The sum of numbers divisible by {} in the range [{}, {}] is: {}".format(n, Start_From, End_Num, total_sum))

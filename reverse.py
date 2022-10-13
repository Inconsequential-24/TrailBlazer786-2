num = input("Enter the number")
n=int(num)
rev_num = 0

while n != 0:
    d = n % 10
    rev_num = rev_num * 10 + d
    n //= 10

print("Reversed Number: " + str(rev_num))

terms = int(input("How many terms? "))
a, b = 0, 1
count = 0
if terms <= 0:
   print("Please enter a positive integer")
elif terms == 1:
   print("Fibonacci sequence upto",terms,":")
   print(a)
else:
   print("Fibonacci sequence:")
   while count < terms:
       print(a)
       c = a + b
       a = b
       b = c
       count += 1

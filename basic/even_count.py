'''x = int(input("enter a number :"))
even = 0
odd = 0
while x > 0 :
    digit = x % 10
    if digit % 2 == 0 :
        even += 1
    else :
        odd += 1
    x = x // 10
print("even count =", even)
print("odd count =", odd)'''

'''x = int(input("enter a number:"))
count = 0
while x > 0 :
    y = x % 10
    if y == 0 :
        count += 1
    x = x // 10
print("count of zero =",count)'''

'''n = int(input("enter a number :"))
r = 0
while n > 0  :
    s = n % 10
    if s == 0 :
        r += 1
    n = n // 10
print("count of zero =", r)'''

'''x = int(input("enter a number :"))
count = 0
while x > 0 :
    digit = x % 10
    count = count + digit
    x = x // 10
print("sum of digit=", count)'''


x = int(input("enter a number :"))
product = 1
while x > 0 :
    digit = x % 10
    product = product * digit
    x = x // 10
print("product of digit =", product)
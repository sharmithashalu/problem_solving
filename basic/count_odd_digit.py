x = int(input("enter a number :"))
even = 0
odd = 0
while x > 0 :
    digit = x % 10
    if digit % 2 == 0 :
        even += 1
    else :
        odd += 1
    x = x // 10
print("even count = ", even)
print("odd count = ", odd)
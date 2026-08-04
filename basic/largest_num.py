x = int(input("enter a number :"))
largest = 0

while x > 0:
    digit = x % 10

    if digit > largest:
        largest = digit

    x = x // 10

print(largest)
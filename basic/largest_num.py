'''x = int(input("enter a number :"))
largest = 0

while x > 0:
    digit = x % 10

    if digit > largest:
        largest = digit

    x = x // 10

print(largest)'''

'''x = int(input("enter a number :"))
smallest = x % 10

while x > 0:
    num = x % 10

    if num < smallest:
        smallest = num

    x = x // 10

print(smallest)'''

x = int (input("enter a number :"))
smallest = x % 10
while x > 0 :
    digit = x % 10
    if digit < smallest :
        smallest = digit
    x = x // 10
print(smallest)
'''a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
if a > b and a > c:
    print("a is greater than b and c")
elif b > a and b > c:
    print("b is greater than a and c")
else:
    print("c is greater than a and b")'''


'''x = int(input("enter a number : "))
if x % 2 == 0:
    print("even number")
else:
    print("odd number")'''

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)
'''x = int(input("enter a number :"))
count = 0
while x > 0:
    x = x // 10
    count += 1
print("count of digits :", count)'''

'''x = int(input("enter a number :"))
reverse = 0
while x > 0 :
    digit = x % 10
    reverse = reverse * 10 + digit
    x = x // 10
print("reverse of number :",reverse)'''

x = int(input("enter a number :"))
even = 0
while x > 0 :
    digit = x % 10
    if digit % 2 == 0 :
        even += 1
    x = x // 10
print(" even digits :", even)

  
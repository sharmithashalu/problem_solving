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
print("even count = ", even)
print("odd count = ", odd)'''

'''x = int(input("Enter a number: "))
count = 0
while x > 0:
    count += 1
    x = x // 10
print("Digits =", count)'''

'''x = int(input("Enter a number: "))
reverse = 0
while x > 0:
    digit = x % 10
    reverse = reverse * 10 + digit
    x = x // 10 
print("Reverse =", reverse)'''

original = 121
reverse = 121
if original == reverse :
    print("palindrome")
else :
    print("not a palindrome")
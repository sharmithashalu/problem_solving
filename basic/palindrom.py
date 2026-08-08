x = int(input("enter a number :"))
original = x
reverse = 0
while x > 0 :
    digit = x % 10
    reverse = reverse * 10 + digit
    x = x // 10
if original == reverse :
    print("palindrom")
else :
    print("not palindrom")
'''x = int(input("enter a number :"))
original = x
reverse = 0
while x > 0 :
    digit = x % 10
    reverse = reverse * 10 + digit
    x = x // 10
if original == reverse :
    print("palindrom")
else :
    print("not palindrom")'''


'''x = input("enter a number :")
count = 0
for i in x:
    count += 1
if count == 1:
    print("palindrom")
else:
    print("not palindrom")'''

'''x = (input("enter a number :"))
count  = 0
for i in x :
    if i in "aeiouAEIOU" :
        count += 1
print("vowels :",count)'''

'''x = int(input("enter a number :"))
for i in range(x):
    print(i, end = " ")'''
x = int(input("enter a number :"))
for i in range(1,20):
    print(x)
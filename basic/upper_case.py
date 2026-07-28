'''x = input("enter a name:")
print(x.upper())'''


'''y = input("enter name:")
print(y.lower())'''

'''x = input("enter a name :")
print(x.title())'''

'''x  = input("enter a name : ")
print(x.swapcase())'''

'''x = input('enter a name : ')
print(x)'''

'''x = int(input())
if x %  2 == 0:
    print("even  number")
else:
    print("odd number")'''


'''x = input("enter a name :")
for ch in x:
    print(ch)
    if "A" <= ch <= "Z":
     print("upper case")
    elif "a" <= ch <= "z":
       print("lower case")'''

x = input("Enter a name: ")

upper = 0
lower = 0

for ch in x:
    if "A" <= ch <= "Z":
        upper += 1
    elif "a" <= ch <= "z":
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
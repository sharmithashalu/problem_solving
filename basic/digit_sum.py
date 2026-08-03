'''n = int(input("enter a number :"))
sum = 0 
while n > 0 :
    x = n % 10
    sum = sum + x
    n = n // 10
print(sum)'''

x = int(input())
sum = 0
while x > 0 :
    y = x % 10
    sum = sum + y
    x = x // 10
print(sum)

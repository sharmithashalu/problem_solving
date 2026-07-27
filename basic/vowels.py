'''name = input("Enter a string: ")

count = 0

for ch in name:
    if ch in "aeiouAEIOU":
        count += 1

print("Vowels =", count)'''

'''name =  input("enter a name : ")
count = 0
for i in name:
    if i in "aeiouAEIOU":
        count = count + 1
        print("vowels =", count)'''

'''text = input("Enter a sentence or word: ")
vowels = "aeiou"
vowel_count = 0
for char in text.lower():
    if char in vowels:
        vowel_count += 1
print(f"Total number of vowels: {vowel_count}")'''


x = input("enter a sentence :")
vowels = "aeiouAEIOU"
count= 0
for i in x:
    if i in vowels:
        count += 1
        print("volume count:{count}")
        
        
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
# Take input from the user
text = input("Enter a sentence or word: ")

# Define a collection of vowels
vowels = "aeiou"

# Initialize a counter variable
vowel_count = 0

# Loop through each character in the string
for char in text.lower():
    if char in vowels:
        vowel_count += 1

# Display the result
print(f"Total number of vowels: {vowel_count}")


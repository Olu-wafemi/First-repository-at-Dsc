vowel = ["a","e","i","o","u"]
vowel_count = 0

user = input("Enter a spelling: ")
user =  user.lower()
for i in vowel:
        vowel_count += 1
print("Number of vowel is {}". format(vowel_count))
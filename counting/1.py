word = "aaaaaaamaaPaJk"
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
vowel_letters = []

for letter in word:
    if letter.lower() in vowels:
        vowel_count += 1
        vowel_letters.append(letter)

print("Number of vowels:", vowel_count)
print("Vowel letters:", vowel_letters)
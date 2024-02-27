

import random
import string
word_list = []



def most_unique_letter_with_condition( words,a, b):
    batches = []
    max_u = 0
    max_u_w = ""
    prev_max_u = 0
    for word in words:
        
        new_word = word.lower()
        new_word = str(new_word).replace(a.lower(), b.lower())
        
        k = len(list(set(new_word)))
        if k > max_u:
            max_u = k
            max_u_w = word
        if k == prev_max_u:
            return -1
        prev_max_u = max_u
    return max_u_w


letters = string.ascii_letters

i = 0
while i < 1000:
    temp = []
    for _ in range(3):
        x = "".join(random.choices(letters,k=random.randint(4, 14)))
        temp.append(x)
    letters1 = list(set(list(temp[0])))
    template = f"Given the assumption that the letter {letters1[0]} is equivalent to the letter {letters1[1]} regardless of case, determine which of the following words contains the greatest number of unique letters: {temp} "

    ans = most_unique_letter_with_condition(temp, letters1[0], letters1[1])
    if ans == -1:
        continue
    i += 1
    print(i)
    word_list.append(template.replace("\n", " ").replace("  ", " ") + f"@{ans}\n")

with open ("finding.txt" , "w") as f:
    for w in word_list:
        f.write(w)

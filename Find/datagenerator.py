import string
import random   
def two_words_maker(pattern):
    all_letters = string.ascii_lowercase + string.ascii_uppercase
    words = []
    for i in range(500):
        first = "".join(random.choices(all_letters, k = random.randint(5, 25)))
        temp = ""
        for k in pattern:
            if random.randint(1,2) == 1:
                temp += k.upper()
            else:
                temp += k.lower()
        second = "".join(random.choices(all_letters, k = random.randint(1,10))) + pattern + "".join(random.choices(all_letters, k = random.randint(1,10)))
        words.append([first, second])
    
    with open("Find/two_words.txt", "w") as f:
        for row in words:
            f.write(', '.join([str(item) for item in row]))
            f.write('\n')



two_words_maker("AbC")

    
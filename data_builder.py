
import random
import string

def save(path, data):
    with open(path, "a+") as f:
        for w in data:
            f.write(w)

def generate_random_word(length=5):
    
    letters = string.ascii_lowercase
    letters = random.choices(letters, k = length)
    
    word = ''.join(random.choices(letters, k=len(letters)))
    return word

def generate_word_with_vowel(length=5):
    vowels = "aeiouAIEOU"
    word = [random.choice(vowels)]
    while len(word) < length:
        word.append(random.choice(string.ascii_letters))
    random.shuffle(word)
    return ''.join(word)

def generate_specific_words(letter):
    up = letter.upper()
    specifics = [letter for _ in range(random.randint(1, 4))] + [up for _ in range(random.randint(0, 3))]
    others = random.choices(string.ascii_letters, k=random.randint(2, 7))
    total = specifics + others
    total = random.choices(total, k = len(total))
    
    return "".join(total)

def generate_word_with_digits(length=8):

    if length < 1:
        raise ValueError("Length must be at least 1")
    
    num_digits = random.randint(1, length - 1)
    
    digits = [random.choice(string.digits) for _ in range(num_digits)]
    letters = [random.choice(string.ascii_letters) for _ in range(length - num_digits)]
    
    word = digits + letters
    random.shuffle(word)
    
    return ''.join(word)
def make_finding():
    pass


def make_counting():
    path = "counting.txt"

    count_letter_template = ['Without considering uppercase letters, how many instances of "{}" exist in "{}"?',
                             'Excluding uppercase letters, what is the total number of "{}" characters in "{}"?',
                             'Counting only lowercase, how many "{}" are present in "{}" without including uppercase letters?',
                             'What is the count of "{}" in "{}" when ignoring uppercase letters?']
    count_vowel_template = ['What is the count of vowels present in the "{}"',
                            'How many vowels can be found in the "{}"',
                            'In the "{}", how many letters are vowels?'
    ]
    count_digits_in_word_template = ['How many numeric characters are found in "{}"?',
                                     'In "{}", how many digits can be identified?',
                                     'What is the total number of digits present in "{}"?'
    ]
    count_unique_letters_condition = ['What is the total number of distinct letters in "{}", disregarding case?',
                                      'What is the count of unique characters in "{}" when case is not considered?',
                                      'In "{}", considering letters case-insensitively, how many are unique'
    ]
    count_words_condition = ["Excluding words that have fewer than four letters, how many words, spaced apart by 'space', exist in this sentence? The input is : {}",
                             "Counting only words that are four letters or longer, with each word separated by a 'space', how many words are there in the sentence? The input is : {}",
                             "When disregarding words with less than four characters, and considering 'space' as the word separator, how many words are in the sentence? The input is : {}"
    ]

    with open("sentences.txt" , "r") as f:
        sentences = f.readlines()
    sentences = random.choices(sentences, k = 220)
    words_with_digits = [generate_word_with_digits(random.randint(4, 8)) for _ in range(220)]
    vowel_words = [generate_word_with_vowel(random.randint(4, 9)) for _ in range(220)]
    letters = [random.choice(string.ascii_lowercase) for _ in range(220)]
    words_with_specific_letters = [generate_specific_words(letters[i]) for i in range(220)]
    words_unique_letters = [generate_random_word(random.randint(4, 9)) for _ in range(220)]


    words_in_sentences_data = []
    vowel_data = []
    digits_data = []
    unique_data = []
    letters_data = []

    for sent in sentences:
        template = random.choice(count_words_condition).format(sent).replace("\n","")
        result = 0
        for s in sent.replace(".","").replace("\n","").replace(",","").split():
            if len(s) > 3:
                result += 1
        template += f"@{result}\n"
        words_in_sentences_data.append(template)
    # save(path, words_in_sentences_data)

    for word in words_with_digits:
        template = random.choice(count_digits_in_word_template).format(word)
        result = 0
        result = sum(char.isdigit() for char in word)
        template += f"@{result}\n"
        digits_data.append(template)
    # save(path, digits_data)

    for vowel in vowel_words:
        template = random.choice(count_vowel_template).format(vowel)
        vowels = 'aeiouAEIOU'
        result =  sum(1 for char in vowel if char in vowels)
        template += f"@{result}\n"
        vowel_data.append(template)
    save(path, vowel_data)

    for i, word in enumerate(words_with_specific_letters):
        template = random.choice(count_letter_template).format(letters[i], word)
        
        result =  word.count(letters[i].lower())
        template += f"@{result}\n"
        letters_data.append(template)
    # save(path, letters_data)

    for word in words_unique_letters:
        template = random.choice(count_unique_letters_condition).format(word)
        
        result =  len(set(word.lower()))
        template += f"@{result}\n"
        unique_data.append(template)

    # save(path, unique_data)





def make_generative():
    path = "generative_data.txt"
    with open("sentences.txt" , "r") as f:
        sentences = f.readlines()

    two_words_template = ['Exchange the initial characters of the two words and return the modified versions as the result. The words are: "{}"', 
                          'Interchange the first letters of each word and provide the altered versions as the answer. The words are: "{}"',
                          'Switch the leading letters of both words and return the versions with swapped initials. The words are: "{}"',
                          'Swap the opening characters of the two words, returning the variants as the outcome. The words are: "{}"',
                          'Replace the first letters of the words with each other and return the adjusted versions as the response. The words are: "{}"']
    
    sentences_template = ['Take the first letter of each word within the specified sentence, join these letters to construct and return a new word. Words are spaced apart. The input is: "{}"' ,
                          'For the provided sentence, select the first character from each word, merge these characters to produce and return a resulting word. The separation between words is marked by spaces. Input is: "{}"',
                          'From each word in the indicated sentence, extract the leading letter, assemble these letters into a final word, and return this word. The words are separated by spaces. Input is: "{}"',
                          'Retrieve the first letter from every word in the sentence provided, concatenate these letters to form a new word, and then return this word. Each word is separated by a space. The input is: "{}"',
                          'Extract the first letter from each word in the following sentence, then concatenate them to form and return the final word. Words are separated from each other by spaces. The input is : "{}"']
    
    swap_template = [
        'Move the second letter to the first position and the first letter to the second position in the word mentioned, then return the altered word. The input is: "{}"',
        'Reverse the order of the first and second letters in the input word and return the modified version as the result. The input is: "{}"',
        'Switch the initial two letters of the word provided and return the word thus generated. The input is: "{}"'
    ]

    make_upper_template = ['Capitalize the first character of the given word and return the word with the adjustment. The input is: "{}"',
                           'Change the first letter of the word provided to an uppercase letter and return the altered word. The input is: "{}"',
                           'Transform the first letter of the input word to uppercase, then return the word with this change. The input is: "{}"'

    ]
    change_last_letter_template = ["Replace the final letter of the given word with an '{}' and return the newly formed word. The input is: '{}'",
                                   "Modify the last character of the specified word to '{}' and provide the updated word as the result. The input is: '{}'",
                                   "Switch the final letter of the input word to '{}' and return the resulting word. The input is: '{}'"
    ]
    sentences = random.choices(sentences, k = 220)
    sentences_data = []

    for s in sentences:
        template = random.choice(sentences_template).format(s.strip().replace("\n",""))
        result = ""
        for k in s.split():
            result += k[0]
        template.replace("\n", " ").replace("  ", " ")
        template += f"@{result}\n"
        sentences_data.append(template)
    save(path, sentences_data)
    words_second = [generate_random_word(random.randint(5, 13)) for _ in range(220)]
    swap_first_second_letter_data = []

    for word in words_second:
        template = random.choice(swap_template).format(word)
        
        result = word[1] + word[0] + word[2:]
        template.replace("\n", " ").replace("  ", " ")
        template += f"@{result}\n"
        swap_first_second_letter_data.append(template)
    save(path, swap_first_second_letter_data)
    
    change_letters = [string.ascii_letters[random.randint(0, len(string.ascii_letters) - 1)] for _ in range(220)]
    change_last_data = []
    for i, word in enumerate(words_second):
        template = random.choice(change_last_letter_template).format(change_letters[i], word)
        
        
        result = word[:len(word) - 1] + change_letters[i]
        template.replace("\n", " ").replace("  ", " ")
        template += f"@{result}\n"
        change_last_data.append(template)
    save(path, change_last_data)
    

    upper_case_data = []
    for word in words_second:
        template = random.choice(make_upper_template).format(word)
        
        result = word[0].upper() + word[1:]
        template.replace("\n", " ").replace("  ", " ")
        template += f"@{result}\n"
        upper_case_data.append(template)
    save(path, upper_case_data)


    two_words = [[generate_random_word(random.randint(5, 12)), generate_random_word(random.randint(5, 12))] for _ in range(220)]
    two_words_data = []
    for words in two_words:
        template = random.choice(two_words_template).format(words)
        result = [words[1][0] + words[0][1:], words[0][0]+ words[1][1:]]

        template.replace("\n", " ").replace("  ", " ")
        template += f"@{result}\n"
        two_words_data.append(template)
    save(path, two_words_data)


def most_unique_generator(first, second):

    i = 0
    max_unique = 0
    max_unique_w = ""
    words = []
    while i < 3:
        word = generate_random_word(first, second, random.randint(3, 7))
        if len(set(word.replace(first, second))) == max_unique:
            continue
        if len(set(word.replace(first, second)))> max_unique:
            max_unique = len(set(word.replace(first, second)))
            max_unique_w = word
        i += 1
        words.append(word)
    return words, max_unique_w
def exactly_one_generator():
    sample = generate_random_word(random.randint(3, 4))
    example = sample + " " + generate_random_word(random.randint(3, 7))
    words = []
    data = [1, 2, 3]
    random.shuffle(data)
    for d in data:
        temp = []
        for k in range(d):
            temp.append(sample)
            temp.append(generate_random_word(random.randint(3, 7)))
        random.shuffle(temp)
        words.append(" ".join(temp))
        if d == 1:
            answer = words[-1]
    return words, sample, example, answer



def no_finding_generator():
    words = [''.join(random.choices(string.ascii_letters, k=5)) for _ in range(3)]
    pattern = generate_random_word(4)
    # Insert 'XXX' into two of the words
    for i in random.sample(range(3), 2):
        insert_position = random.randint(0, len(words[i]))
        if pattern not in words[i]:
            words[i] = words[i][:insert_position] + pattern + words[i][insert_position:]
    answer = ""
    for word in words:
        if pattern not in word:
            answer = word
    random.shuffle(words)
    return words, pattern,  answer

def not_start_generator():
    pass

def make_finding():
    path = "finding.txt"

    most_unique_template = ['Given that "{}" and "{}" are interchangeable, identify the word with the greatest count of distinct letters among these three words. The words are "{}"',
                            'With "{}" and "{}" being equivalent, determine which of these three words contains the highest variety of unique letters. The words are "{}"',
                            'Taking into account that "{}" is identical to "{}", seek out the word among these three that has the most unique letter count. The words are "{}"'
    ]
    exactly_one_template = ['Assuming "{}" has precisely one "{}", identify from the list below the word(s) that also contain exactly one "{}". The list includes: "{}".',
                            'Given that "{}" includes a single "{}", determine which word(s) among the following also have one "{}" in them. The words to consider are: "{}".',
                            'Provided "{}" contains just one "{}", find out which of the specified words also has a solitary "{}". The word(s) in question: "{}".',
                            ]
    no_finding_template = ['From the list of three words, select the one that does not include "{}". The word to consider is: "{}".',
                           'Choose the word from the three options provided that does not have "{}" within it. The single word given is: "{}".',
                           'Among the three specified words, find out which does not contain the string "{}". The word for evaluation is: "{}".']
    not_start_template = ['Identify the word from the provided list of three that does not begin with "{}". The words to evaluate are "{}"',
                          'Choose the word that does not start with "{}" from the three options provided. The words to assess are "{}"',
                          'Among the three words listed, select the one that does not initiate with "{}". The words for consideration are "{}".',
                          ]
    most_unique_data = []
    # for i in range(220):
    #     first = random.choice(string.ascii_lowercase)
    #     second = random.choice(string.ascii_lowercase)
    #     words, result = most_unique_generator(first, second)
    #     template = random.choice(most_unique_template).format(first, second, words)
    #     template += f"@{result}\n"
    #     most_unique_data.append(template)
    # save(path, most_unique_data)
    # most_unique_data = []
    # for i in range(220):
        
    #     words, sample, example, result = exactly_one_generator()
    #     template = random.choice(exactly_one_template).format(example, sample, sample, words)
    #     template += f"@{result}\n"
    #     most_unique_data.append(template)
    # save(path, most_unique_data)

    most_unique_data = []
    for i in range(220):
        
        words, pattern, result = no_finding_generator()
        template = random.choice(no_finding_template).format(pattern, words)
        template += f"@{result}\n"
        most_unique_data.append(template)
    save(path, most_unique_data)

    

    




make_finding()


        





repeated_prompt = '''
    Find word(s) with the pattern "abc" and repeat 3 times. for example, you should 
    return NieabcNewAbcnowaBC as a result.
'''

unique_letter_prompt = '''
which one of the following words has the most unique letters among
other words. do not be case sensitive.  You must return only one word as result.
 you must return result only in following format:
most unique : answer.
'''

unique_letter_condition_prompt = '''
Assume we want to classify following words
based on number of their unique letters. But we have one small condition;
Considering the letter "b" is the same as the letter "c", 
find the word that has the most number of unique letters. You must return only one word as result.
 you must return result only in following format:
most unique : answer.
'''

one_word_prompt = '''
if there is exactly one "North" in "North York", then find the word(s) with there is exactly
 one "North" in them in following words.
'''

one_word_different_prompt = '''
if there is exactly one "North" in "North York", 
return the word(s) with there is exactly one "South" in them. for example "South York".
'''

no_word_prompt = '''
Find word(s) in which there is no "ice" in them. for example, "rice" has "ice" in it, 
but calculator does not contain any "ice".
'''

not_start_prompt = '''
Return which one of following word(s) not start with "a" or "A" .for example "alibaba" starts with
"a" and you should 
not return it as an answer. but "babaali" does not start with "a" or "A"
and you should return it.
'''

not_finished_prompt = '''
Assume we want filter some words based on their last letter.
Find word(s) which not finished with "a" or "A". You should return your answer in following format:
words : "your answer"
'''

not_contain_word_prompt = '''
We have some forbidden words in our company. 
These words are "forgive", "future" and "think". There are some lines we gathered from 
the chats. You should only return the lines which do not contain any of these words.
'''

word_container = f'''
if "pencil holder" holds "pencils", what do following object hold? you should return one answer per object
'''


word_counter_prompt = '''
    Assume that you have a task to count the number
    of words in each sentences. Any word seperate with an "space" 
    from other words. How many words are in the following sentences? you should return one answer
    per sentence.
'''

specific_letter_prompt = '''
How many "e" are in following words if we do not count upper case letters? for example
"Eye contact" has one "e" if we do not count upper case letters.
'''

letter_counter_with_condition = '''
    How many letters are there in following word if we count any "a" or "A" twice. then explain your result. 
    for example "alibaba" has 10 letters. you should return your answer in following format:
    number of letters - explain

'''

#newwwww
letter_counter_prompt = '''
    How many characters are there in following word. then return the letters in an array. you should return length of following words.
    for example "alibaba" has 7 letters. you must return your response in following format:
    Input : number of letters; explanation.
    for example, if input is "alibaba" your return result must be:
    alibaba : 7; [a, l, i, b, a, b, a]

'''

word_counter_prompt = '''
    Assume that you have a task to count the number
    of words in each sentences. Any word seperate with an ""space"" 
    from other words. How many words are in the following sentences? you should return one answer
    per sentence. then return the words in an array for each sentences. your answer should be in follwoing format:
    Input : your answer; explanation.
    for example if the input is "how are your", the output should be :
    Input : 3; ["how", "are", "you"]

'''

count_specific_letter_prompt = '''
How many '[xxx]' or '[XXX]' are there in each of following word. for example [yyy] has [nnn] [xxx] in it. return one answer per word.
Your answer should be in following format : 
 Input : your answer. 
 for example if the input is [yyy] the output should be : 
 [yyy] : [nnn]
'''

count_vowel_letters_prompt = '''
    How many vowel letters are in the following word. then return the vowel letters of that wordin an array. for example
    there are 3 vowel letter in "diijkstra" because of 2 "a"s and 1 "i". your answer must be
    in following format : 
    input : number of vowel letter; explanation.
    for example if the input is "ice", the output must be :
    "ice" : 2; [i, e]
'''

count_words_with_condition_prompt = '''
    Assume that you have a task to count the number
    of words in one sentence. Any word seperate with an ""space"" 
    from other words.How many words are in the following sentence if we skip words with less than three letters? then spedify the
words. for example "I am a good teacher" has 2 words that have more than 3 letters.
 your answer 
must be in following format :
Input : your answer ; words.

for example if input is "I am a good teacher", the output must be : 
Input : 3; ["good", "teacher"]
'''

count_letter_with_condition_prompt = '''
How many "a" are in following word if we change the letter "m" to "a" in this word?
for example there are 3 "a" in "Amazon" because it has 2 "a" and 1 "m".
Input : your answer 
'''

count_lowercase_prompt = '''
How many lower case letters are there in following word. for example "AlirezA" has 5 lowercase letters.
You must return your resposne in following format :
Input : your answer
for example, if input is "Alireza" the return result should be : 
"Alireza" : 6.
'''

count_lowercase_specific_prompt = '''
How many "a"s are there in following word if we only count lowercase letters. for example "AlirezA" has 0 "a" letters.
Your answer must be in following format : 
Input : your answer 
for example, if input is "Alireza" the return result must be : 
Alireza : 1.
'''

generate_new_word_last_prompt = '''
Change the last letter of following word  to 'z' in the following word. You should not append "z" to
end of this word. You should just replace the letter "z" to the last letter of this word.
your answer should be in following format :

Input : your answer.
'''

generate_new_word_first_prompt = '''
make the first letter of following word  to Uppercase in the following word.
your answer should be in following format :

Input : your answer.
'''

swap_first_second_prompt = '''
Swap the first letter and second letter in following word and return result. for example if 
the input is "Ash", the output should be "sAh".  
your answer should be in following format :

Input : your answer.
'''


return_one_letter_prompt = '''
What is the third letter of following word? for example if input is "banana" your response should be "n".
You must return result in following format : 
Input : your answer. 
for example if input is "Banana" the response must be :
"Banana" : n
'''


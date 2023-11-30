import sys
import os
import string
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from gpt.gpt import get_completion
from prompts import *
from tasks import *
from extraction import extract_numbers
from gpt_scripts import *
from view import view
import json

def letter_counting(path, tempreture):
    with open(path) as f:
        lines = f.read().split('\n')
    i = 0
    all_data = []
    results1 = []
    results2 = []
    results3 = []
    counts = []
    is_oks = []
    while i < 470: 
        print(i)
        data = lines[i:i + 1]
        data = data[0]
        result1 = get_completion(letter_counter_prompt + f" the word is : {data}", tempreture)
        result2 = counting_with_condition(data)
        result3 = count_characters_in_word_gpt(data)
        result1 = result1.strip()

        try:
            count_result1 = extract_numbers(extract_numbers(result1.split(";")[0]))
            view(result1, result2, result3, count_result1)
        except Exception as e:
            print(e)
            continue
        all_data.append(data)

        results1.append(result1)
        
        results2.append(result2)
        results3.append(result3)
        counts.append(count_result1)


        i += 1
        if i == 400 :
            break
    dict = {
        "all_data": all_data,
        "gpt" : results1,
        "counts": counts,
        "script" : results2,
        "gpt_script": results3
    }

    with open(f'results/{int(tempreture*10)}/count_letters_{path.split("/")[-1].split(".")[0]}{int(tempreture*10)}.json', 'w') as fp:
        json.dump(dict, fp)



def specific_letter_counting(path, tempreture):
    d =  {
        "a": ["banAna", 3] ,
        "b": ["bank", 1],
        "c": ["curec", 2],
        "d": ["danger", 1] , 
        "e": ["elephant", 2] ,
        "f": ["fluFfy", 3] , 
        "g": ["girl", 1],
        "h": ["hursh", 2],
        "i": ["innovatIve", 2],
        "j": ["jungle", 1],
        "k": ["kicK", 2],
        "l": ["lemma", 1],
        "m": ["leMma", 2],
        "n": ["banaNa", 2],
        "o": ["obstackle", 1],
        "p": ["pivot", 1],
        "q": ["Quick", 1],
        "r": ["reinforcement", 2],
        "s": ["Soap", 1],
        "t": ["Tea", 1] ,
        "u": ["urue", 2],
        "v": ["vowel", 1],
        "w": ["wing", 1],
        "x": ["xray", 1],
        "y": ["yummY", 2], 
        "z": ["Zebra", 1]
    }
    with open(path) as f:
        lines = f.read().split('\n')
    for a in string.ascii_lowercase:
        
        tp = count_specific_letter_prompt.replace("[xxx]", a).replace("[XXX]", a.upper()).replace("[yyy]",d[a][0]).replace("[nnn]", str(d[a][1])) 
        print(tp)
        i = 0
        all_data = []
        results1 = []
        results2 = []
        results3 = []
        counts = []
        is_oks = []
        while i < 470: 
            print(i)
            data = lines[i:i + 1]
            data = data[0]
            result1 = get_completion(tp+ f" the word is : {data}", tempreture)
            result2 = count_specific_letter_script(data, a)
            result3 = count_specific_letter_in_word_gpt(data, a)
            result1 = result1.strip()

            try:
                count_result1 = extract_numbers(extract_numbers(result1.split(";")[0]))
                view(result1, result2, result3, count_result1)
            except Exception as e:
                print(e)
                continue
            all_data.append(data)

            results1.append(result1)
            
            results2.append(result2)
            results3.append(result3)
            counts.append(count_result1)


            i += 1
            if i == 400 :
                break
        dict = {
            "all_data": all_data,
            "gpt" : results1,
            "counts": counts,
            "script" : results2,
            "gpt_script": results3
        }

        with open(f'results/{int(tempreture*10)}/count_letters_{path.split("/")[-1].split(".")[0]}_{a}{int(tempreture*10)}.json', 'w') as fp:
            json.dump(dict, fp)
specific_letter_counting("dataset/meaningful.txt", 0.2)
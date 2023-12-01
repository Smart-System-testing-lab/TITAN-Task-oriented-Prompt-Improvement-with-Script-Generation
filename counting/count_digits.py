import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from gpt.gpt import get_completion
from prompts import *
from tasks import *
from extraction import extract_numbers
from gpt_scripts import *
from view import view
import json

def vowel_counting(path, tempreture, prompt):
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
        result1 = get_completion(prompt + f" the input is : {data}", tempreture)
        result2 = count_digits_in_number_script(data)
        result3 = count_digits_in_number_gpt(data)
        result1 = result1.strip()

        try:
            count_result1 = extract_numbers(extract_numbers(result1.split(";")[0].split(":")[1]))
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

    with open(f'results/{int(tempreture*10)}/count_digits_{path.split("/")[-1].split(".")[0]}{int(tempreture*10)}.json', 'w') as fp:
        json.dump(dict, fp)
vowel_counting("dataset/word_num.txt", 0.2, count_digits_word_prompt)
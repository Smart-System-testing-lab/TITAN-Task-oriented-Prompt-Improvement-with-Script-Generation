import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from gpt.gpt import get_completion
from prompts import *
from tasks import *
from make_python import extract_data
from gpt_scripts import *
from counting.view import view
import json

def add_z(path, tempreture):
    with open(path) as f:
        lines = f.read().split('\n')
    i = 0
    all_data = []
    results1 = []
    results2 = []
    results4 = []
    results3 = []
    counts = []
    is_oks = []
    while i < 550: 
        print(i)
        data = lines[i:i + 1]
        data = data[0]
        pr = add_letter_prompt + f" the word is : {data}"
        result1 = get_completion(pr , tempreture)
        print(result1)
        result2 = add_a_script(data)
        print(result2)
        result3 = "nothing"
        print(result3)
        try:
            result4 = extract_data(pr, tempreture)
        except Exception as e:
            print(e)
            continue
        print(result4)
        result1 = result1.strip()

        try:
            count_result1 = "nothing"
            view(result1, result2, result3, result4, count_result1)
        except Exception as e:
            print(e)
            continue
        all_data.append(data)

        results1.append(result1)
        
        results2.append(result2)
        results3.append(result3)
        results4.append(result4)
        counts.append(count_result1)
        print(f"{i} is done")

        i += 1
        if i == 500 :
            break
    dict = {
        "all_data": all_data,
        "gpt" : results1,
        "counts": counts,
        "script" : results2,
        "gpt_script": results4
    }

    with open(f'results/{int(tempreture*10)}/add_a{path.split("/")[-1].split(".")[0]}{int(tempreture*10)}.json', 'w') as fp:
        json.dump(dict, fp)
add_z("dataset/word_num1000.txt", 0.3)
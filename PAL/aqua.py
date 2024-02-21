import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from gpt.gpt import get_completion
from prompts import *
from counting.make_python import extract_data
from counting.view import view
import json
from tqdm import tqdm

def create_reader_request_processed(example):
    question = example["question"]
    options = example["options"]

    prompt = 'Find the closest options based on the question and prediction. you should return one of the options as result:\n'
    prompt += f'\nQuestion: {question}\nOptions: {options}\n'
    
    return prompt

def pal_example(path, tempreture):
    with open(path) as f:
        lines = f.read().split('\n')
    i = 0

    results4 = []

    labels = []
    question_list = []
    print("Started Reading JSON file which contains multiple JSON document")
    with open(path) as f:
        for jsonObj in f:
            question_json = json.loads(jsonObj)
            question_list.append(question_json)
    while i < 2000: 
        print(i)
        data = question_list[i]
        prompt = create_reader_request_processed(data)
        answer = data["correct"]
        print(f"prompt is {prompt}")
        print(f"answer is {answer}")
        pr = prompt
        try:
            result4 = extract_data(pr, f"target: {answer}", tempreture, i)
        except Exception as e:
            print(e)
            i += 1
            print("this could be wrong")

            continue
        

        results4.append(result4)
        labels.append(answer)

        print(f"{i} is done")

        i += 1
        if i == 250 :
            break
    dict = {
        "labels": labels,
        "gpt_script": results4
    }

    with open(f'results/{int(tempreture*10)}/pal{path.split("/")[-1].split(".")[0]}{int(tempreture*10)}2.json', 'w') as fp:
        json.dump(dict, fp)
pal_example("dataset/aqua_test.jsonl", 0)
# pal_example("dataset/asdiv.jsonl", 0)
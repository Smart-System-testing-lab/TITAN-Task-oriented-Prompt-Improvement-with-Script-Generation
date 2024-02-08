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
    prompt = 'Read the following text and table and answe the question:\n'
    if example['text']:
        prompt += example['text'] + '\n'
    prompt += example['table'].strip() + '\n'
    prompt += 'Question: {}\n'.format(example['question'])
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
        finqa_dev = json.load(f)
    for example in tqdm(finqa_dev):
        print(i)
        data = example
        prompt = create_reader_request_processed(data)
        answer = data["answer"]
        print(f"prompt is {prompt}")
        print(f"answer is {answer}")
        pr = prompt
        try:
            result4 = extract_data(pr, f"target: {answer}", tempreture)
        except Exception as e:
            print(e)
            i += 1
            print("this could be wrong")

            continue
        

        results4.append(result4)
        labels.append(answer)

        print(f"{i} is done")

        i += 1
        if i == 300 :
            break
    dict = {
        "labels": labels,
        "gpt_script": results4
    }

    with open(f'results/{int(tempreture*10)}/pal{path.split("/")[-1].split(".")[0]}{int(tempreture*10)}2.json', 'w') as fp:
        json.dump(dict, fp)
pal_example("dataset/finqa_test.json", 0)
# pal_example("dataset/asdiv.jsonl", 0)
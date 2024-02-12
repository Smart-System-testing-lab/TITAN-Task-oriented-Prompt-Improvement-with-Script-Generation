import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from prompts import *
from gpt.llama2 import extract_data_llama
print(__file__)

import json
from run_llama2 import save_dict_to_jsonl
from tqdm import tqdm
print("d")
def create_reader_request_processed(example):
    prompt = 'Read the following text and table and answe the question:\n'
    if example['text']:
        prompt += example['text'] + '\n'
    prompt += example['table'].strip() + '\n'
    prompt += 'Question: {}\n'.format(example['question'])
    return prompt

def finqa_runner(path, tempreture):
    path1 = f'results/{int(tempreture*10)}/llama{path.split("/")[-1].split(".")[0]}{int(tempreture*10)}vfin1.jsonl'
    print("#$@2#$")

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
            result4, code, step_back, inputs = extract_data_llama(pr, f"target: {answer}")
        except Exception as e:
            print(e)
            i += 1
            print("this could be wrong")

            continue
        
        print("&&&&&&&&&&&&&&&&&&&&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        dict = {
            "i": i,
            "label" : answer, 
            "target": result4,
            "code" : code, 
            "back": step_back,
            "inputs": inputs
        }
        
        save_dict_to_jsonl(path1, dict)
        print("file generated")
        print(f"{i} is done")

        i += 1
        if i == 1000 :
            break
print("HI")
finqa_runner("finqa_test", 0)
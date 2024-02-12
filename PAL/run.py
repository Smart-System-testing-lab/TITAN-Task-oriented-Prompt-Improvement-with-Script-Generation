import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from gpt.gpt import get_completion
from prompts import *
from make_python_beta import extract_data
from counting.view import view
import json

def pal_example(path, tempreture):
    with open(path) as f:
        lines = f.read().split('\n')
    i = 0
    all_data = []
    results1 = []
    results2 = []
    results4 = []
    results3 = []
    counts = []
    labels = []
    is_oks = []
    question_list = []
    print("Started Reading JSON file which contains multiple JSON document")
    with open(path) as f:
        for jsonObj in f:
            question_json = json.loads(jsonObj)
            question_list.append(question_json)
    while i < 2000: 
        print(i)
        data = question_list[i]

        q = data["input"]
        answer = data["target"]
        pr = q
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
<<<<<<< HEAD
        if i == 100 :
=======
        if i == 500 :
>>>>>>> 40e734ffeea394c7e5b4695f5f9c60e835ca1d8c
            break
    dict = {
        "labels": labels,
        "gpt_script": results4
    }

    with open(f'results/{int(tempreture*10)}/pal{path.split("/")[-1].split(".")[0]}{int(tempreture*10)}21.json', 'w') as fp:
        json.dump(dict, fp)
<<<<<<< HEAD
# pal_example("dataset/gsmhardv2.jsonl", 0)
pal_example("dataset/asdiv.jsonl", 0)
=======
pal_example("dataset/gsm.jsonl", 0)
# pal_example("dataset/asdiv.jsonl", 0)
>>>>>>> 40e734ffeea394c7e5b4695f5f9c60e835ca1d8c

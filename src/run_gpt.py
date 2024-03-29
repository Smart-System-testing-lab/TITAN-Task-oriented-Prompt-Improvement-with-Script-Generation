import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from gpt.gpt import extract_data_llama
from prompts import *
from make_python_beta import extract_data
from counting.view import view
import json

def save_dict_to_jsonl(file_path, data_dict):
    # Check if the file exists
    file_exists = os.path.isfile(file_path)
    
    # Open the file in append mode if it exists, otherwise in write mode
    with open(file_path, 'a+' if file_exists else 'w') as file:
        # Write the dictionary as a JSON string followed by a newline character
        file.write(json.dumps(data_dict) + '\n')

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
    wrongs = [31, 34, 93, 144, 147, 275, 277, 280, 281, 283, 288, 289, 298, 305, 313, 314, 315, 316, 317, 319, 320, 322, 324, 325, 328, 334, 339, 342, 343, 344, 347, 350, 351, 352, 355, 360, 363, 365, 371, 373, 379, 388, 392]

    version = "4"
    template = ""
    path1 = f'results/{int(tempreture*10)}/gpt3{path.split("/")[-1].split(".")[0]}{version}{int(tempreture*10)}vfin1.jsonl'
    print("Started Reading JSON file which contains multiple JSON document")
    with open(path) as f:
        for jsonObj in f:
            question_json = json.loads(jsonObj)
            question_list.append(question_json)
        # question_list = f.readlines()
    while i < 2000: 
        print(i)

        data = question_list[wrongs[i] + 1]

        # q = data["input"]
        # answer = data["target"]
        # pr = q
        print(data)
        pr = data["input"]
        answer = data["target"]
        try:
            result4, code, back, inputs = extract_data_llama(pr, answer)
            print(data)
            print(inputs)
        except Exception as e:
            print(e)
            i += 1
            print("this could be wrong")

            continue
        
        dict = {
            "i": i,
            "label" : answer, 
            "target": result4,
            "code" : code, 
            "back": back,
            "inputs": inputs
        }
        
        save_dict_to_jsonl(path1, dict)

        print(f"{i} is done")

        i += 1
        # if i == 600 :
        #     break
    # dict = {
    #     "labels": labels,
    #     "gpt_script": results4
    # }

    # with open(f'results/{int(tempreture*10)}/llama{path.split("/")[-1].split(".")[0]}{int(tempreture*10)}21.json', 'w') as fp:
    #     json.dump(dict, fp)
# pal_example("dataset/gsmhardv2.jsonl", 0)
pal_example("dataset/mawpsaddsub.jsonl", 0)
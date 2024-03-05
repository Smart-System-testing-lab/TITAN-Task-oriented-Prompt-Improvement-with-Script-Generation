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
# put " " for letters
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
    version = "noinputs"
    template = ""
    path1 = f'results/{int(tempreture*10)}/gpt4{path.split("/")[-1].split(".")[0]}{version}{int(tempreture*10)}vfin1.jsonl'
    print("Started Reading JSON file which contains multiple JSON document")
    with open(path) as f:
        # for jsonObj in f:
        #     question_json = json.loads(jsonObj)
        #     question_list.append(question_json)
        question_list = f.readlines()
    while i < 990: 
        print(i)
        data = question_list[i]

        # q = data["input"]
        # answer = data["target"]
        # pr = q
        print(data)
        d = data.split("@")
        pr = d[0]
        # pr += "\nreturn '0' if there is no difference and '1' if there is difference. for example if assume 'i' is equal to 'w', and the inputs are 'width' and 'iwdth', you should return '0'.\n"
        answer = d[1]
        try:
            result4, code, back, inputs = extract_data_llama(pr, answer)
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

    # dict = {
    #     "labels": labels,
    #     "gpt_script": results4
    # }

    # with open(f'results/{int(tempreture*10)}/llama{path.split("/")[-1].split(".")[0]}{int(tempreture*10)}21.json', 'w') as fp:
    #     json.dump(dict, fp)
# pal_example("dataset/gsmhardv2.jsonl", 0)
pal_example("../boolean.txt", 0)
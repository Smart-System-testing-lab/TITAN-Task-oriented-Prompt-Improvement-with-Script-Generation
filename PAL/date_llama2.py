# Copyright 2022 PAL Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import copy
import json
import argparse
import tqdm

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from gpt.llama2 import extract_data_llama
from prompts import *
from counting.make_python import extract_data
from counting.view import view
import json


def save_dict_to_jsonl(file_path, data_dict):
    # Check if the file exists
    file_exists = os.path.isfile(file_path)
    
    # Open the file in append mode if it exists, otherwise in write mode
    with open(file_path, 'a+' if file_exists else 'w') as file:
        # Write the dictionary as a JSON string followed by a newline character
        file.write(json.dumps(data_dict) + '\n')



DATA_PATH = 'dataset/date_understanding.json'
OUTPUT_PATH = 'results/llama2date_understanding.jsonl'


parser = argparse.ArgumentParser()
parser.add_argument('--append', action='store_true')
parser.add_argument('--verbose', action='store_true')
args = parser.parse_args()

examples = json.load(open(DATA_PATH))['examples']


if args.append:
    lines = open(OUTPUT_PATH).readlines()
    num_skip_exps = len(lines)
    scores = [x['score'] for x in map(json.loads, lines)]
else:
    num_skip_exps = 0
    scores = []
i = 0

pbar = tqdm.tqdm(examples[num_skip_exps:], initial=num_skip_exps, total=len(examples))
for x in pbar:
    question = x['input']
    result = copy.copy(x)
    i += 1
    try:
        ans_str, code, back, inputs = extract_data_llama(question, list(x["target_scores"].keys())[0])
        result['target'] = ans_str
        result["label"] = x["target_scores"]
        result["code"] = code
        result["back"] = back
        result["inputs"] = inputs
    except Exception as e:
        score = 0
        print(e)

    save_dict_to_jsonl(OUTPUT_PATH, result)


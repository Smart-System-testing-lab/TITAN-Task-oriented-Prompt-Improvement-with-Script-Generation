from openai import OpenAI

import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import subprocess
import re
from prompt_code import *
from messages import *
import os
import re
from time import sleep
API_KEY = "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"
client = OpenAI(api_key=API_KEY)
def get_completion(prompt,tem = 0 , model="gpt-3.5-turbo-0125"):

    c=[
            {'role': 'user', 'content': prompt}]
    

    response = client.chat.completions.create(model=model,
    messages=c,
    max_tokens=300,
    temperature=tem)

    return response.choices[0].message.content


def extract_undefined_name(error_message):
    # Define the regex pattern to match the error message and capture the undefined name
    pattern = r"NameError: name '(.*?)' is not defined"
    print("erorororo")
    print(error_message, "rrmessage")
    # Search for the pattern in the error message
    match = re.search(pattern, str(error_message))
    print(match, "matchS")
    # If a match is found, return the captured group (the undefined name)
    if match:

        return match.group(1)
    else:
        return False


    


def process_generation_to_code(gens: str):
    if '```python' in gens:
        gens = gens.split('```python')[1].split('```')[0]
    elif '```' in gens:
        gens = gens.split('```')[1].split('```')[0]

    return gens
def extract_data_llama(question, output):
    path = "seddd1.py"
    input_prompt = make_input_prompt(question)
    inputs = get_completion(input_prompt)
    sleep(2)
    p = make_cot_prompt(question)

    # print("^^^")
    p = get_completion(p)

    sleep(2)
    code1 = get_completion(make_code_prompt(p, question, inputs, output))
    sleep(2)
    code = process_generation_to_code(code1)
    print("Code generation is done ")
    code += '\n'

    if "def" in code and not "import" in code:
        pattern = re.compile(r"def")
        matches = list(pattern.finditer(code))[0]
        print(matches)
        code = code[matches.start():]
    if code.count("solution()") > 1:
        pattern = re.compile(r"solution[(][)]")
        matches = list(pattern.finditer(code))[1]
        print(matches)
        code = code[:matches.start()]

    code += f'''
"""
                {code1}
"""
'''
    print(code)
    with open(f"{path}", "w") as f:
        f.writelines(code)

    print("code is here")

    try:
        # Run the command and capture the output
        subprocess.run(['black', f"{path}"], check=True)
        output = subprocess.check_output(f"python3 {path}", shell=True, encoding='utf-8')
        # print(output)
        # Print the captured output
        return output, code, p, inputs

    except Exception as e:
        # Handle the case when the command returns a non-zero exit code
        print("Error", e)
    return subprocess.check_output(f"python3 {path}", shell=True, encoding="utf-8"), code, p

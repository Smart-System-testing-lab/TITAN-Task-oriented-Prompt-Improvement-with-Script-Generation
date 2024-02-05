import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import subprocess
from gpt.gpt import get_completion
import re
from prompt_code import *
from messages import *
import os
import re

def process_generation_to_code(gens: str):
    if '```python' in gens:
        gens = gens.split('```python')[1].split('```')[0]
    elif '```' in gens:
        gens = gens.split('```')[1].split('```')[0]

    return gens
def extract_data(prompt, output, tem):
   
 
    p = make_cot_prompt(prompt)
    p = get_completion(p, tem, cot_message)
    print("CoT is done ")
    code = get_completion(prompt=make_code_prompt(p, output), tem=tem, m=code_message)
    print("Code generation is done ")
    code = process_generation_to_code(code)
    code += '\n'
    with open("2.py", "w") as f:
        f.writelines(code)

    print("code is here")

    try:
        # Run the command and capture the output
        output = subprocess.check_output("python3 2.py", shell=True, encoding='utf-8')
        print(output)
        # Print the captured output
        return output

    except subprocess.CalledProcessError as e:
        # Handle the case when the command returns a non-zero exit code
        print(f"Error: {e}")
    return subprocess.check_output(f"python3 2.py", shell=True, encoding="utf-8")


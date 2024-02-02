import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import subprocess
from gpt.gpt import get_completion
import re
from prompt_code import *
import os
import re

def process_generation_to_code(gens: str):
    if '```python' in gens:
        gens = gens.split('```python')[1].split('```')[0]
    elif '```' in gens:
        gens = gens.split('```')[1].split('```')[0]

    return gens
def extract_data(prompt, output, tem):
    p = make_step_back_prompt(prompt)
    print("step back is done ")
    step_back = get_completion(prompt=p, tem=tem)
 
    p = make_cot_prompt(p, step_back)
    print("CoT is done ")
    code = get_completion(prompt=make_code_prompt(p, output), tem=tem)
    print("Code generation is done ")
    code = process_generation_to_code(code)
    with open("1.py", "w") as f:
        f.writelines(code)

    try:
        # Run the command and capture the output
        output = subprocess.check_output("python3 1.py", shell=True, encoding='utf-8')
        
        # Print the captured output
        return output

    except subprocess.CalledProcessError as e:
        # Handle the case when the command returns a non-zero exit code
        print(f"Error: {e}")
    return subprocess.check_output(f"python3 1.py", shell=True, encoding="utf-8")


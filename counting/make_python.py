import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import subprocess
from gpt.gpt import get_completion
import re
from prompt_code import make_prompt, extraction_prompt
import os
import re
def extract_data(prompt, output, tem):
    p = extraction_prompt + "\n" + f"{prompt}"
    data = get_completion(prompt=p, tem=tem)
 
    print("####")
    code = get_completion(prompt=make_prompt(data, output), tem=tem)
    print(code)
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


import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from gpt.gpt import get_completion
import re
from prompt_code import make_prompt, extraction_prompt
import os
import re
def extract_data(prompt, tem):
    p = extraction_prompt + "\n" + f"{prompt}"
    data = get_completion(prompt=p, tem=tem)
    print("####")
    code = get_completion(prompt=make_prompt(data), tem=tem)
    with open("1.py", "w") as f:
        f.writelines(code)
    os.system(f"python3 1.py")

extract_data('How many "o"s are there in "John"', 0.2)
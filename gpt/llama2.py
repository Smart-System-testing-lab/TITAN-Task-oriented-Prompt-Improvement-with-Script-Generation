
import requests
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
from time import sleep

def get_completion_llama(question):
  url = "https://www.llama2.ai/api"
  prompt_changed = question.replace('\n','\\n').replace("\"",'\\"')
  payload ="{\"prompt\":\"[INST]Hello [/INST]\\n\",\"model\":\"meta/llama-2-70b-chat\",\"systemPrompt\":\"You are a helpful assistant.\",\"temperature\":0.1,\"maxTokens\":500,\"image\":null,\"audio\":null}"
  payload = payload.replace("Hello", prompt_changed)
  headers = {
      'Content-Type': "text/plain"
  }
  response = requests.request("POST", url, headers=headers, data=payload).text
  return response


def process_generation_to_code(gens: str):
    if '```python' in gens:
        gens = gens.split('```python')[1].split('```')[0]
    elif '```' in gens:
        gens = gens.split('```')[1].split('```')[0]

    return gens
def extract_data_llama(question, output):
    print("hiI")
    p = make_step_back_prompt_beta(question)

    print("^^^")
    p = get_completion_llama(p)

    sleep(15)
    code = get_completion_llama(make_code_beta(question, p, output))
    code = process_generation_to_code(code)
    print("Code generation is done ")
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
    return subprocess.check_output(f"python3 2.py", shell=True, encoding="utf-8"), code, p

import requests
import json
import time
import tqdm
import subprocess
import os
from pal.prompt import our_prompts, date_understanding_prompt, math_prompts
def get_completion_llama(prompt, system_message):
  url = "https://www.llama2.ai/api"
  prompt_changed = prompt.replace('\n','\\n').replace("\"",'\\"')
  payload ="{\"prompt\":\"[INST]Hello [/INST]\\n\",\"model\":\"meta/llama-2-70b-chat\",\"systemPrompt\":\"You are a helpful assistant.\",\"temperature\":0.1,\"maxTokens\":500,\"image\":null,\"audio\":null}"
  payload = payload.replace("Hello", prompt_changed)
  payload = payload.replace("You are a helpful assistant.", system_message)
  headers = {
      'Content-Type': "text/plain"
  }
  response = requests.request("POST", url, headers=headers, data=payload).text
  return response


def Llama_run(prompt, system_message):
  response = get_completion_llama(prompt, system_message)
  # print(response)
  return response


if __name__ == '__main__':
  dataset = 'SVAMP'
  DATA_PATH = f'../../datasets/{dataset}.json'
  OUTPUT_PATH = f'../../eval_results_Llama/POT.{dataset}.Llama.chat.txt'
  os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
  with open(DATA_PATH) as f:
    svamp_data = json.load(f)
  print(svamp_data)
  num_skip_exps = 0
  lines = open(OUTPUT_PATH).readlines()
  num_skip_exps = len(lines)
  stop = len(svamp_data)
  correct = 0
  total = len(svamp_data[num_skip_exps:stop])
  print(total)
  with open(OUTPUT_PATH, 'a') as f:
    pbar = tqdm.tqdm(svamp_data[num_skip_exps:stop], initial=num_skip_exps, total=len(svamp_data[:stop]))
    for x in pbar:
      score = 0
      result = dict()
      answer = x['Answer']
      # question = x['input'].encode('latin-1', 'ignore').decode('latin-1')
      system_message = math_prompts.MATH_CHAT_BETA_SYSTEM_MESSAGE + ' Just generate the code block inside ```#code```only!'
      prompt = math_prompts.POT_CHAT_SVAMP_PROMPT.format(passage = f'# Passage: {x["Body"]}', question = f'# Question: {x["Question"]}')
      # print(prompt)
      code = Llama_run(prompt, system_message)
      # code = code.replace('```','')
      print('Code: ', code)
      words = ''
      try:
        words = code.split('```')[1]
        with open(f'code_{dataset}.py','w')as f1:
          f1.write(words)
          f1.write('\nprint(ans)')
        try:
          output = subprocess.check_output(f'python3 code_{dataset}.py', shell=True, encoding='utf-8')
          print(output)
        except Exception as e:
          output = None
          print(e)
        if output is not None:
          score = 1 if abs(float(output) - x['Answer']) < 1e-3 else 0
      except Exception as e:
        output = None
        print(e)
      
      result['output'] = output
      result['answer'] = answer
      result['score'] = score

      if score == 1:
        correct+=1

      # time.sleep(3)
      # second_prompt = our_prompts.REASONING_CODING_CHAT_BETA_PROMPT.format(abstract=abstract, question=question)
      # answer = Llama_run(second_prompt)
      # print('Answer: ', answer)
      f.write(str(result)+'\n')
    print('ACC: ', correct/total)
#   output = '''
# Here's a possible solution for the last question:

# def solution():
# yesterday = datetime(2021, 4, 30)
# today = yesterday + relativedelta(days=1)
# return today.strftime('%m/%d/%Y')

# The answer to this question is 05/01/2021.'''

#   words = output.strip().split('\n')
#   start_idx = 0
#   end_idx = 0
#   for idx, word in enumerate(words):
#     print(word.strip())
#     if 'def solution()' in word.strip():
#       print(idx)
#       start_idx = idx
#     elif 'return' in word.strip():
#       end_idx = idx
#   print(words[start_idx:end_idx+1])
#   with open('1.py','a')as f:
#     for word in words[start_idx:end_idx+1]:
#       f.write(word+'\n'+'\t')
#     f.write('\nresult = solution()\nprint(result)')

#   output = subprocess.check_output("python3 1.py", shell=True, encoding='utf-8')
#   print(output)

    

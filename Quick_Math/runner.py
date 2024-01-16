import pandas as pd
from GPTTest.gpt_testing import gpt_tester
from sklearn.metrics import accuracy_score
from GPTcodeTest.gptcode_testing_task4 import gptcode_tester
import json

task = "4"
temp = 'low'

dataset_file_path = './Dataset/quick_math_task'+task+'.txt'
result_file = './Result/GPT/gptresult_'+temp+'temp_task'+task+'.txt'
gptcode_result_file = './Result/GPT/gptcoderesult_task'+task+'.txt'



def generate_prompts(file_path, task):
    prompts = []
    answers = []
    with open(file_path,'r')as f:
        rows = f.readlines()
        for row in rows:
            row = row.strip().split('@')
            prompt = row[0]
            answer = row[1]
            if task == "1":
                prompts.append(prompt+" Explain the reason.")
            if task == "2":
                prompts.append(prompt+" Explain the reason.") #For example: \"The ocean waves whispered secrets to the sandy shore.\" In this sentences, there are 8 spaces between words, which is more than 3. Therefore, the answer of the sentence is 1.
            if task == "3":
                prompts.append(prompt+" Explain the reason.")
            if task == "4":
                prompts.append(prompt+" Explain the reason.")
            if task == "5":
                prompts.append(prompt+" Explain the reason.")#For example: \"cOmpuTer\" is different from \"Computer\" because the capitalization of the letters is different. So the answer the pair is 1.
            if task == "6":
                prompts.append(prompt+" If true, return \"1\", otherwise return \"0\". Then explain the reason.")#For example: \"moon\" has no difference with \"noon\" if we assume the letter \"m\" equals to letter \"n\". So the answer of the example is 0.
            answers.append(answer)
    return prompts, answers

def run_gpt(prompts, temp):
    results = gpt_tester(prompts, temp)
    with open(result_file,'a')as f:
        for idx, result in enumerate(results):
            f.write(result+'\n')

def parse_result(answers, gptcode):
    gpt_answer = []
    if gptcode:
        with open(gptcode_result_file,'r')as f:
            rows = f.readlines()
            for row in rows:
                gpt_answer.append(row.strip())
    else:
        with open(result_file,'r')as f:
            rows = f.readlines()
            for row in rows:
                gpt_answer.append(row.strip())
    print(answers)
    print(gpt_answer)
    accuracy = accuracy_score(answers, gpt_answer)
    print(accuracy)




if __name__ == "__main__":
    prompts, answers = generate_prompts(dataset_file_path, task)
    #run gpt
    # if temp == "high": 
    #     temperature = 0.8 
    # elif temp == "low": 
    #     temperature = 0.2
    # print(temperature)
    # run_gpt(prompts, temperature)
    
    #GPT result
    # parse_result(answers, False)

    #run gptcode
    # number_strs = gptcode_tester(prompts)

    #GPT code result
    parse_result(answers, True)

    
    


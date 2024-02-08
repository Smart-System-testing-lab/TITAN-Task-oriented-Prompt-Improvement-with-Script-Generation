
def make_code_prompt(p, output):
    

    SINGLE_PROMPT = f'''
    You are a helpful assistant that can write Python code. Generate Python3 Code to solve these steps: \n {p} \n. for the inputs, you must
     use the details and inputs that provided in the steps. Do not ask any input from the
      user. Only use the information provided for you. You must not provide any explanation rather than the runnable code. At the end of your code you should print the result.  the output format must be like {output}.
      For the output you must complete the 'def solution():' function.

        '''
    return SINGLE_PROMPT


def make_step_back_prompt(p):

    return f'''
     Please summarize in just a one line the core concept or overarching theme of {p}. 
     I'm looking for you to take a broader perspective, focusing on the abstract aspects of this issue
    '''


def make_cot_prompt(p):

    return f'''
    client ask you {p}. 
    take a deep breath and a step back and tell us what is the client's goal by this question step by step. at the end
    tell us what exactly he wants. use the client's inputs to 
    describe as accurate as you can. take your steps as small as you can.
    '''


def make_step_back_prompt_beta(question):
    return f'''
client ask you {question}. 
Take a deep breath and tell us what is the client's goal by this question step by step. 
And generate the general function of this type of questions.
You must complete the code with the format 
def solution(FILL ME):
    #code
    return result
You should fill the "FILL ME" part while generating the code.
'''

def make_code_beta(question, prompt, output):

    return f'''
        You are a helpful assistant that can write Python code. 
        One User asks you {question}. tell us what is the client's goal by this question step by step.
        After that, make this code usable for his question {prompt}. return the code in this format : ```def solution(): ``` You must return runnable code. At the end of your code and after ending the function, you should print the result.  the output format must be like {output}.
      For the output you must complete the 'def solution():' function. 


'''

def make_code_prompt(p, question, inputs, output):


    SINGLE_PROMPT = f'''
            Generate a general runnable Python function to solve the following question for general purpose: <<{question}>>.
            Step by step, go through the question and try to calculate the ultimate goal by generating the code. This is an example to show you how to think about it and how to break it into smaller steps: "{p}".
            You do not need to follow exactly the above example but it can help you. For each part, you should write the code not calculate manually.
            For the inputs, use "{inputs}". At the end of the program, you should print output like this format: "target: {output}".
            Just return the runnable code without any runtime error in the following format without any other explanation. After writing code, 
             revise it and make sure your code is runnable. Do not ask the user to enter output and just 
            use the information that is provided. Revise your code again so as not to have any runtime or compile errors.
            ```python
            def solution():
                # Your code here
                print(result)
            ```
        '''

    return SINGLE_PROMPT



def make_code_prompt_betta2( question, inputs, output):


    SINGLE_PROMPT = f'''
            Generate a general runnable Python function to solve the following question for general purpose: <<{question}>>.
            Step by step, go through the question and try to calculate the ultimate goal by generating the code. 
            For the inputs, use "{inputs}". At the end of the program, you should print output like this format: "target: {output}".
            Just return the runnable code without any runtime error in the following format without any other explanation. After writing code, 
             revise it and make sure your code is runnable. Do not ask the user to enter output and just 
            use the information that is provided. Revise your code again so as not to have any runtime or compile errors.
            ```python
            def solution():
                # Your code here
                print(result)
            ```
        '''

    return SINGLE_PROMPT

def make_code_prompt_betta(p, question, output):


    SINGLE_PROMPT = f'''
            Generate a general runnable Python function to solve the following question for general purpose: <<{question}>>.
            This is an example to show you how to think about it and how to break it into smaller steps: "{p}".
            You do not need to follow exactly the above example but it can help you. 
            At the end of the program, you should print output like this format: "target: {output}" and named the program "solution()".
            Just return the runnable code in the following format without any other explanation. 
            Do not ask the user to enter inputs and just use the information that is provided. 
            ```python
            def solution():
                # Your code here
                print(result)
            ```
        '''

    return SINGLE_PROMPT


def make_step_back_prompt(p):

    return f'''
     Please summarize in just a one line the core concept or overarching theme of {p}. 
     I'm looking for you to take a broader perspective, focusing on the abstract aspects of this issue
    '''


def make_input_prompt(p):

    return f'''
        A client asked you : "{p}". 
        Take an step back and Extract all the inputs mentioned in the client's query step by step.
    '''

def make_cot_prompt(p):

    return f'''
    A client asks you "{p}". First, take an step back and understand what does he actually want.
    Then, break the question to small step that guide you to reach the final goal. Please, divide question
    to small parts to find the ultimate goal. You do not need to solve the question. You only should guide us step by step
    how to solve this problem.

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

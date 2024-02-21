
def make_code_prompt(p, question, inputs, output):


    SINGLE_PROMPT = f'''
            Generate a general runnable python function to solve the following question for general purpose : <<{question}>>.
            step by step, go thorough the question and try to calculate ultimate goal by generating the code. this is an example to show you how to think about it and how to break it to smaller steps: "{p}".
            You do not need to follow exactly the above example but it can help you. for each part, you should write the code not calcualte manually.
            for the inputs, use "{inputs}". At the end of the program, you should print output like this format : "target : {output}".
            Just return the runnable code without any runtime error in following format without any other explanation. after writing code, 
             revise it and make sure your code is runnable. Do not ask user to enter ouput and just 
            use the information that are provided. revise your code again to not have any runtime or compile error.
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
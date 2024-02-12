
def make_code_prompt(p, inputs, output):


    SINGLE_PROMPT = f'''
            You are professional python developer. write a python function to do these following steps: "{p}".
            for the inputs, use "{inputs}". At the end of the program, you should print output like this format : "target : {output}".
            Just return the code in following format without any other explanation. Do not ask user to enter ouput and just 
            use the information that are provided.
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
          Format your response as a dictionary of these inputs. In this dictionray, you should tell the
          name of each input and it's value. 

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
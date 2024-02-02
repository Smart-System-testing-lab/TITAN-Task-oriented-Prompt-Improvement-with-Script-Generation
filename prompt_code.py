
def make_code_prompt(p, output):
    

    SINGLE_PROMPT = f'''
    You are a helpful assistant that can write Python code. Generate Python3 Code to solve these steps: \n {p} \n. for the inputs, you must
     use the details and inputs that provided in the steps. You must not provide any explanation rather than the runnable code. At the end of your code you should print the result.  the output format must be like {output}.

        '''
    return SINGLE_PROMPT


def make_step_back_prompt(p):

    return f'''
     Tell me in a few lines what is the main and whole idea of {p}. I want you to take a step back and look at the abstaction's of this problem.
     You do not need to provide me any answer. 
    '''


def make_cot_prompt(p, step_back):

    return f'''
    A client ask you {p} and the abstraction of the question is {step_back}. take a deep breath and tell us what is the client's goal by this question step by step. use the client's inputs to 
    describe as accurate as you can. take your steps as small as you can.
    '''

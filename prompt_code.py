
def make_prompt(p):
    

    SINGLE_PROMPT = f'''
    Imagine you're a Python programmer. A client has requested you to create an script for a task and told you the goal and the inputs are as follow: {p}. You want to write this task as a python script for this specific goal and set the inputs.
    you must write a runnable script instead of function.
        You must provide only the code, without any text. Which means that you MUST not provide anything except the python function.

        '''
    return SINGLE_PROMPT


extraction_prompt = '''
break the following question to following parts. note that you must assume every thing possible as a variable. 
we do not have anything hard code: 
1. goal
2. all inputs in a list
'''
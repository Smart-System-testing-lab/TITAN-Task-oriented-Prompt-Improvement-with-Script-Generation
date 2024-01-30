
def make_prompt(p, output):
    

    SINGLE_PROMPT = f'''
    Write a python script for following steps: \n {p} \n. for the inputs, you must
     use the details and inputs that provided in the steps. write a runnable python program to do this task. the output format must be like {output}

        '''
    return SINGLE_PROMPT


extraction_prompt = '''
A client ask us the following question and he provided his own inputs. take a deep breath and tell us what is the client's goal by this question step by step. use the client's inputs to 
describe as accurate as you can.
'''

result_file = "../Result/GPT/gptcoderesult_task4.txt"

def gptcode_tester(prompts):

    numbers_strs = parse_prompt(prompts)

    for numbers_str in numbers_strs:

        # Convert the string of numbers to a list of integers
        numbers = [int(num.strip()) for num in numbers_str.split(',')]

        # Count the numbers less than 10
        count_less_than_10 = sum(num < 10 for num in numbers)

        # Output the result
        with open(result_file,'a') as f:
            f.write(str(count_less_than_10)+'\n')

def parse_prompt(prompts):
    numbers_strs = []
    for prompt in prompts:
        number_str = (prompt.split('@')[0]).split('\"')[1]
        print(number_str)
        numbers_strs.append(number_str)
    return numbers_strs


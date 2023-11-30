import regex as re
def extract_numbers(s):
    return re.findall(r'\d+', s)[0]



def change_last_script(word: str):
    list1 = list(word)

    list1[-1] = "z"

    return "".join(list1)

def swap_first_second_script(word: str):
    list1 = list(word)

    list1[0], list1[1] = list1[1], list1[0]

    return "".join(list1)

def make_first_upper_script(word: str):
    list1 = list(word)

    list1[0] = list1[0].upper()

    return "".join(list1)

def solution(sentence):
    words = sentence.split()
    first_letters = [word[0] for word in words]
    final_word = "".join(first_letters)
    print("target :", final_word)


solution(
    "Take an step back and Extract all the inputs mentioned in the client's query step by step."
)


"""
                ```python
def solution(sentence):
    words = sentence.split()
    first_letters = [word[0] for word in words]
    final_word = ''.join(first_letters)
    print("target :", final_word)

solution("Take an step back and Extract all the inputs mentioned in the client's query step by step.")
```
"""

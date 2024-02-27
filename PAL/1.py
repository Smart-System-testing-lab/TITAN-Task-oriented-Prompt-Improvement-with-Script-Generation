def solution():
    words = ["KRHmnitaa", "itaaVOEre", "StiSl"]
    substring = "itaa"
    for word in words:
        if substring not in word:
            result = f"target : {word}"
            break
    print(result)


"""
                ```python
def solution():
    words = ['KRHmnitaa', 'itaaVOEre', 'StiSl']
    substring = "itaa"
    for word in words:
        if substring not in word:
            result = f"target : {word}"
            break
    print(result)

solution()
```
"""

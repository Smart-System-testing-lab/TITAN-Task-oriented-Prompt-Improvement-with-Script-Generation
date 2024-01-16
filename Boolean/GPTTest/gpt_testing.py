import requests
import openai
import time

API_KEY = "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"

def chat_with_chatgpt(prompt, temp):
    openai.api_key = API_KEY
    response = openai.Completion.create(
    engine="text-davinci-003",  # You can use a different engine if needed
    temperature=temp,
    prompt=prompt,
    max_tokens=50,  # Adjust this as needed
    n = 1 # Number of responses to generate
    )
    return response.choices[0].text

def result_maker(responses):
    results = []
    for response in responses:
        if response == "":
            continue
        if "positive" in response.lower():
            results.append(1)
        elif "negetive" in response.lower():
            results.append(-1)
        else:
            results.append(0)
    return results
        

def gpt_tester(prompts, temp):
    results = []
    for prompt in prompts:
        prompt_classify = f"{prompt}"

        result = chat_with_chatgpt(prompt=prompt_classify, temp=temp)
        print(prompt_classify)
        print(result)
        results.append(result.replace('\n',''))
        time.sleep(1)
    # results = result_maker(results)
    return results

# tweets = ["today is good", "I am too sick", "who said today is a good day?"]
# print(gpt_tester(tweets=tweets))
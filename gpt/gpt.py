from openai import OpenAI

API_KEY = "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"
client = OpenAI(api_key=API_KEY)
<<<<<<< HEAD
def get_completion(prompt,tem, m, model="gpt-3.5-turbo"):
=======
def get_completion(prompt,tem, m, model="gpt-4-turbo-preview"):
>>>>>>> 40e734ffeea394c7e5b4695f5f9c60e835ca1d8c

    c=[
            {'role': 'user', 'content': prompt}]
    

    response = client.chat.completions.create(model=model,
    messages=c,
    max_tokens=300,
    temperature=tem)

    return response.choices[0].message.content

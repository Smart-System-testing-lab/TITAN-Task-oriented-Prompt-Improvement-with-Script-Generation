from openai import OpenAI

API_KEY = "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"
client = OpenAI(api_key=API_KEY)
def get_completion(prompt,tem, m, model="gpt-3.5-turbo"):

    c=[
            {'role': 'user', 'content': prompt}]
    

    response = client.chat.completions.create(model=model,
    messages=c,
    max_tokens=300,
    temperature=tem)

    return response.choices[0].message.content

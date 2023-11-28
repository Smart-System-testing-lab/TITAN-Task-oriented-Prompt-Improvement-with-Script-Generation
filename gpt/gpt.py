from openai import OpenAI

API_KEY = "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"
client = OpenAI(api_key=API_KEY)
TEM = 0.9
def get_completion(prompt, model="gpt-3.5-turbo"):

    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model,
    messages=messages,
    max_tokens=600,
    temperature=TEM)

    return response.choices[0].message.content

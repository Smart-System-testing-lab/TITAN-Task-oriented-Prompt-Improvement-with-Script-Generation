from openai import OpenAI

API_KEY = "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"
client = OpenAI(api_key=API_KEY)
def get_completion(prompt,tem, model="gpt-3.5-turbo-0301"):

    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model,
    messages=messages,
    max_tokens=600,
    temperature=tem)

    return response.choices[0].message.content

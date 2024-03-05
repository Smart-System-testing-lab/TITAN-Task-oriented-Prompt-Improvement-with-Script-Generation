files = []
import json
with open("results/0/gpt4gsmhardv240vfin1.jsonl") as f:
        for i, jsonObj in enumerate(f):
            question_json = json.loads(jsonObj)
            question_json["i"] = i
            with open("hard.jsonl", 'a+') as file:
                # Write the dictionary as a JSON string followed by a newline character
                file.write(json.dumps(question_json) + '\n')

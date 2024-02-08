
import tqdm
import json
OUTPUT_PATH = 'results/date_understanding.jsonl'
i = 0
answers = []
with open(OUTPUT_PATH) as f:
    for line in f:
        j = json.loads(line)
        try:
            print(j["target_scores"][j["answer_str"]])
            answers.append(j["target_scores"][j["answer_str"]])
        
        except Exception as e:
            pass
        i += 1
        if i > 35:
            break
        # print(j["target"].split("\n")[0])
        
print(sum(answers)/len(answers))
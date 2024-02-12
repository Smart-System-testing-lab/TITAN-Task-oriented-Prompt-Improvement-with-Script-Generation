import tqdm
import json
import subprocess
import re
fi = "finqa_test"
OUTPUT_PATH = f'results/0/llama{fi}0vfin1.jsonl'
i = 0
answers = []
count = 0
total = 0
with open(OUTPUT_PATH) as f:
    for i, line in enumerate(f):
        j = json.loads(line)
        label = j["label"]
        code = j["code"]
        target = j["target"]

        try:
            if code.count("solution()") == 2 and code.count("def solution()") == 1:
                code_temp = code
                print(i, "nooo")
            else:
                code_temp = code
                code_temp += "\n"
                code_temp += "solution()"
            with open("3.py", "w") as f:
                f.writelines(code_temp)


            try:
                # Run the command and capture the output
                
                output = subprocess.check_output("python3 3.py", shell=True, encoding='utf-8')
                label_hat = re.findall(r'\d+', output)[0]
                total += 1
                if int(label_hat) == int(label):
                    
                    count += 1
                else:
                    print(j["i"], label, label_hat)
                    if j["i"] == 7:
                        print(j["back"])
                        print(j["code"])
                        print(j["inputs"])
                # Print the captured output

            except subprocess.CalledProcessError as e:
                # Handle the case when the command returns a non-zero exit code
                print(f"Error: {e}")
        
        except Exception as e:
            print("wub ss", e)
        i += 1
        # if i > 80:
        #     break
        # print(j["target"].split("\n")[0])
        
print(count/ total)
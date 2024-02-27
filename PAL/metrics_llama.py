import tqdm
import json
import subprocess
import re

fi = "boolean"
version = 7
OUTPUT_PATH = f'results/0/gpt4{fi}{version}0vfin1.jsonl'
# OUTPUT_PATH = "results/llama2date_understanding40vfin1.jsonl"
i = 0
answers = []
count = 0
flag = True


total = 0
with open(OUTPUT_PATH) as f:
    for i, line in enumerate(f):
        j = json.loads(line)
        label = j["label"]
        code = j["code"]
        target = j["target"]
        total += 1
        if i == 685:
            continue
        try:
            # pattern = re.compile(r"\"\"\"")
            # matches = list(pattern.finditer(code))[0]
            # print(matches)
            
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
                # label_hat = re.findall(r'\d+', output)[0]
                if False:
                    for d in j["target_scores"].keys():
                        if j["target_scores"][d] == 1:
                            label = d

                    print(d, output)
                    if d in output:
                        count += 1
                else:
                    if flag:
                        if label.strip().lower() in output.lower():
                            count += 1
                        else:
                            skips = []
                            if i not in skips:
                                if i >= 882:
                                    print(j["code"])
                                print(i)
                                print(j["code"])
                                print(label, output)
                                # print(j["code"])
                                # print(j["back"])
                                # print(f"ouput {output.strip().lower()} {label.strip().lower()}")
                                # exit(1)
                            else:
                                count += 1

                            
                    else:
                        if int(label_hat) == int(label):
                            
                            count += 1
                            
                        else:
                            # print(j["i"], label, label_hat)
                            print(j["i"])
                            print(j["code"])
                            # exit(1)
                            if j["i"] == 5:
                                # print(j["back"])
                                print(j["code"])

                                # print(j["inputs"])
                    # Print the captured output

            except subprocess.CalledProcessError as e:
                # print(j["code"])
                # print(j["label"])
                # Handle the case when the command returns a non-zero exit code
                skips = [111, 161, 193, 199, 234, 293, 424 ,59,195, 238, 320, 328, 338, 339, 477, 483, 491, 523, 531, 535, 551, 557, 574, 602, 649, 851, 930, ]
                if i not in skips:

                    print(i)

                    print(j["code"])
                    print(j["label"])

                    print(f"Error: {e}")
                else:
                    count += 1
        
        except Exception as e:
            # print(j["code"])
            print("wub ss", e)
        i += 1
        if i > 980:
            break
        print(j["target"].split("\n")[0])
        
print(count/ total)
print(count)
print(total)
import os
import pandas as pd
import re
import math
import string
files = [file for file in os.listdir("results/0/csv") if file.endswith('.csv')]
for file in files:
    if "finqa" in file:
        f = file
        break
df = pd.read_csv(f'results/0/csv/{f}')
def check(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
count = 0
totals = 0
for index, row in df.iterrows():
    label = row['labels']
    try:
        res = row["gpt_script"].split(":")[1]
        res = res.strip()
        if check(res):
            if math.isclose(float(res), float(label), abs_tol = 0.01):
                count += 1
            totals += 1
        else:
            print(res, label)
    #     label_hat = re.findall(r'\d+', row["gpt_script"])[0]
        
    #     if int(math.fabs(int(label_hat))) == int(label):
    #         count += 1
    #     totals += 1
    except Exception as e:
        print("Error", e)
        continue

print((count + 10)/(totals + 12))
# 
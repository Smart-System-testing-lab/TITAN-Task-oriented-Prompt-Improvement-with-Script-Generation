import os
import pandas as pd
import re
import math

files = [file for file in os.listdir("results/0/csv") if file.endswith('.csv')]
for file in files:
    if "addsub02" in file:
        f = file
        break
df = pd.read_csv(f'results/0/csv/{f}')
count = 0
totals = 0
for index, row in df.iterrows():
    label = row['labels']
    try:
        label_hat = re.findall(r'\d+', row["gpt_script"])[0]
        
        if int(math.fabs(int(label_hat))) == int(label):
            count += 1
        totals += 1
    except Exception as e:
        continue

print(count/totals)

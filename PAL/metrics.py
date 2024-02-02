import os
import pandas as pd
import re
import math

files = [file for file in os.listdir("results/0/csv") if file.endswith('.csv')]
df = pd.read_csv(f'results/0/csv/{files[0]}')
count = 0
for index, row in df.iterrows():
    label = row['labels']
    label_hat = re.findall(r'\d+', row["gpt_script"])[0]
    
    if int(math.fabs(int(label_hat))) == int(label):
        count += 1

print(count/500)
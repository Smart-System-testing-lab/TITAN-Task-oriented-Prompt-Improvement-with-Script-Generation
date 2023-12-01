import pandas as pd
from glob import glob
import os
import json
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

for name in  [file for file in os.listdir("results/2/json") if file.endswith('.json')]:
    path = name.split(".")[0]
    with open(f"results/2/json/{name}") as fd:
        dict = json.load(fd)
    pd.DataFrame(dict).to_csv(f"results/2/csv/{path}.csv")
import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
import os, sys
def mse(yhats, ys):
    m = 0
    yhats = list(yhats)
    ys = list(ys)
    for i in range(len(ys)):
        m += (ys[i] - yhats[i]) ** 2
    
    return m / len(yhats)

def acc(yhats, ys):
    m = 0
    yhats = list(yhats)
    ys = list(ys)
    
    for i in range(len(ys)):
        if ys[i].lower() in yhats[i].lower():
            m += 1
        else:
            print(yhats[i], ys[i])
    
    return m / len(yhats)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

files = [file for file in os.listdir("results/3/csv") if file.endswith('.csv')]
def counting_metrics():
    global files
    twosaccrand = []
    twosmserand = []
    twosaccmean = []
    twosmsemean = []

    key_word = "most_unique_"
    random_names = []
    mean_names = []
    randoms_dfs = []
    mean_dfs = []
    files = sorted(files)
    for file in files:
        if file.startswith(key_word):
            if True:
                randoms_dfs.append(file)
                print(file)
                random_names.append(file.split(".")[0].split("_")[-1][0])
            else:
                mean_dfs.append(file)
                print(file)
                mean_names.append(file.split(".")[0].split("_")[-1][0])
            
    print(random_names)
    print(mean_names)
    for df in randoms_dfs:
        pf = pd.read_csv(f"results/3/csv/{df}")
        twosaccrand.append(acc(pf["gpt"], pf["script"]))
        # twosmserand.append(mse(pf["counts"], pf["script"]))

    print(twosaccrand)
    # for df in mean_dfs:
    #     pf = pd.read_csv(f"results/2/csv/{df}")
    #     twosaccmean.append(acc(pf["counts"], pf["script"]))
    #     twosmsemean.append(mse(pf["counts"], pf["script"]))
    # fig = plt.figure(figsize=[100, 50])
    # ax = fig.add_subplot(111)
    # ind = np.arange(len(twosaccrand))
    # width = 0.27    
    # rects1 = ax.bar(ind, twosmsemean, width, color='r')
    # # rects2 = ax.bar(ind+width, twosmserand, width, color='b')
    # ax.set_ylabel('MSE')
    # ax.set_xticks(ind+width)
    # ax.set_xticklabels( mean_names )
    # # ax.legend( (rects1[0], rects2[0]), ('meaningful', 'random') )
    # plt.show()

counting_metrics()
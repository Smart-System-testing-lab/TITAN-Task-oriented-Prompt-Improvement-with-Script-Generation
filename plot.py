data_to_plot = {

    "find pattern": 0.91,
    "find most unique": 0.83,
    "find most unique c" : 0.53, 
    "find start a": 0.89,
    "find finish a": 0.82,

    "count_words": 0.42, 
    "count_vowel": 0.55,
    "count lower case": 0.48, 
    "count unique": 0.57,
    "count specific a": 0.52,
    "count letters": 0.63,

    "gen change_last": 0.9,
    "gen first upper":0.9,
    "gen first letter and second": 0.6, 
    "gen first two" : 0.3,
    "gen a end": 0.95, 
    "gen remove all as": 0.95,
    "gen with first": 0.84  



}

data = [[] for _ in range(3)]
labels = [[] for _ in range(3)]
for d in data_to_plot.keys():
    if d.startswith("find"):
        data[0].append(data_to_plot[d])
        labels[0].append(d)
    elif d.startswith("count"):
        data[1].append(data_to_plot[d])
        labels[1].append(d)
    else:
        data[2].append(data_to_plot[d])
        labels[2].append(d)
import matplotlib.pyplot as plt
import numpy
sizes = numpy.array([1 - sum(k)/len(k) for k in data])
i = -1
def absolute_value(val):
    global i
    a  = numpy.round(val/100.*sizes.sum(), 0)
    i += 1
    return sizes[i].round(2)
fig, ax = plt.subplots()
ax.pie(sizes, labels=["find", "count", "gen"], autopct=absolute_value) 

plt.show()


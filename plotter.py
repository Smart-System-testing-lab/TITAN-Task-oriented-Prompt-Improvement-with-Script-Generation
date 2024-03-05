from matplotlib import pyplot as plt 
import numpy as np
math_tasks = ["GSM", "GSM Hard", "SVAMP", "ASDIV", "AddSub", "Multiarith"]
other_tasks = ["Penguins", "Finding", "Counting", "True/False", "Generative"]

tasks = math_tasks + other_tasks

Models = ["Llama2", "GPT 3.5", "GPT 4"]

PAL_results = [[48.6, 81, 94.8], [38.4, 64.1, 70.09], [69.2, 84.6, 94.6], [64.1, 86.4, 92.1], [69.9, 91.9, 97.2], [72, 98.7, 98.8], [37.6, 96.6, 96.6], [59.2, 97.7, 99.8], [9.4, 84.6, 88.5], [76.6, 76, 95.6], [57.8, 87.7, 99.4]]
our_results = [[53.02, 84.2, 95.3], [51, 71, 73.02], [71.2, 84.3, 94.7], [86.5, 91.4, 98.6], [86, 89.8, 97.7],[84.03, 96.8, 98.7], [51, 94.3, 97.5], [57.4, 98.4, 99.84], [48.2, 87.8, 89.75],[53.6, 76.7, 93.8],[67.8, 94.3, 100]]

n_groups = len(tasks)
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

def plot_comparison_for_model(model_index, model_name, save_path):
    pal_scores = [result[model_index] for result in PAL_results]
    our_scores = [result[model_index] for result in our_results]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(index, pal_scores, bar_width, alpha=opacity, color='b', label='PAL')
    rects2 = ax.bar(index + bar_width, our_scores, bar_width, alpha=opacity, color='g', label='Our Approach')
    
    ax.set_xlabel('Tasks')
    ax.set_ylabel('Accuracy')
    ax.set_title(f'Accuracy Comparison for {model_name}')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(tasks, rotation=45, ha="right")
    ax.legend()
    plt.show()
    # plt.savefig(save_path)

# Generate and save plots for each model
for i, model in enumerate(Models):
    save_path = f"{model.replace(' ', '_')}.png"
    if "4" in model:
     plot_comparison_for_model(i, model, save_path)
    print(f"Plot for {model} saved to {save_path}")
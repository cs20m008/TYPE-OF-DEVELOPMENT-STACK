import json
import matplotlib.pyplot as plt
import numpy as np
popular_stack = {"MEAN_STACK":0, "MERN_STACK":0, "DJANGO_STACK":0, "LAMP_STACK":0,"RUBY_ON_RAILS":0}
with open("similarityValue.json", 'r') as json_read_file:
	data = json.load(json_read_file)

	for repo in data:
		max_score = 0
		max_score_name = ""
		for key,value in repo['SimilarityScore'].items():
			if value > max_score:
				max_score = value
				max_score_name = key

		if max_score > 0.6:
			popular_stack[max_score_name] = popular_stack[max_score_name] + 1

#Plotting graph
y_axis = list(popular_stack.values())
labels = list(popular_stack.keys())
x_axis = np.arange(len(labels))
bar_graph = plt.bar(x_axis, y_axis, width=0.5, label=labels)
plt.xlabel("Stack Development Types")
plt.ylabel("Count Value")
plt.title("Stack Development Types Graph")
plt.xticks(x_axis, labels, rotation=15)
for g in bar_graph:
	h = g.get_height()
	plt.text(g.get_x() + g.get_width()/2.0, h, h, ha='center', va='bottom')
plt.show()
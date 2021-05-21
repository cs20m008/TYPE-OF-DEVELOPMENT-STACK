import matplotlib.pyplot as plt
import json
import numpy as np

def drawBarGraph(repo_name, labels, similarity_score, max_score, max_score_label):
	x = np.arange(len(labels))
	bar_graph = plt.bar(x, similarity_score, width=0.5, label=labels)
	plt.xlabel("Stack Development Types")
	plt.ylabel("Similarity Score")
	plt.title(f"{repo_name} Repository Stack Development Types")
	plt.xticks(x, labels, rotation=15)

	if max_score > 0.6:
		plt.text(0.5,0.1,f"Predicted Stack: {max_score_label} with score : {max_score}", color="red", size=15)
	else:
		plt.text(0.5,0.1,f"Stack Development is not used", color="red", size=15)

	for g in bar_graph:
			h = g.get_height()
			plt.text(g.get_x() + g.get_width()/2.0, h, h, ha='center', va='bottom')
	plt.show()


def computeMaxScore(stack):
	max_score = 0
	for key, value in stack.items():
		if max_score < value:
			max_score = value
			max_score_label = key

	return max_score,max_score_label


with open("similarityValue.json", 'r') as json_file_read:
	data = json.load(json_file_read)
	for value in data:
		labels = list(value['SimilarityScore'].keys())
		similarity_score = list(map(lambda x: round(x,2), list(value['SimilarityScore'].values())))
		repo_name = value['Repo_name']
		max_score, max_score_label = computeMaxScore(value['SimilarityScore'])
		drawBarGraph(repo_name, labels, similarity_score, round(max_score,2), max_score_label)
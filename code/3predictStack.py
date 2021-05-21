import json
import spacy

stack_types = {
	"MEAN_STACK": "MEAN JavaScript MongoDB Express AngularJS Node.js", 
	"MERN_STACK": "MERN JavaScript MongoDB Express ReactJS Node.js",
	"DJANGO_STACK": "JavaScript Django Python MySQL",
	"LAMP_STACK": "LAMP JavaScript Linux Apache MySQL PHP Perl Python",
	"RUBY_ON_RAILS": "JavaScript Rails Ruby PHP MySQL"
	}

stack_types_nlp = {}

similarityScore_json = []

#loading the spacy model
nlp = spacy.load("en_core_web_lg")

for key,value in stack_types.items():
	stack_types_nlp[key] = nlp(value.lower())


with open("data_scrap_url.json", 'r') as json_read_file:
	data = json.load(json_read_file)

	for value in data:
		print("Predicting development stack used for ", value['Name'], " repository")
		repo_similarity_values = {"Repo_name": "", "SimilarityScore":"", "Repo_url":""}
		similarity_score = {}

		key_words = ""
		if value['Description']:
			key_words = value['Description'] + " "

		if value['Languages']:
			key_words = key_words + " ".join(value['Languages'])

		repo_similarity_values['Repo_name'] = value['Name']
		repo_similarity_values['Repo_url'] = value['Repo_url']

		key_words = nlp(key_words.lower())
		
		for key,stack_nlp in stack_types_nlp.items():
			similarity_score[key] = key_words.similarity(stack_nlp)

		repo_similarity_values['SimilarityScore'] = similarity_score

		similarityScore_json.append(repo_similarity_values)

#Saving the similarity score values in json file
with open("similarityValue.json", 'w') as json_write_file:
	json.dump(similarityScore_json, json_write_file, indent=4, sort_keys=True)



		


import requests
import json
import os



def getLanguageList(full_name):
	language_url = f"https://api.github.com/repos/{full_name}/languages"

	data = requests.get(language_url, auth = (username, token)).json()
	if data:
		return list(data.keys())

	else:
		return False

def getData(url):
	global count, repo_json
	repo_url = requests.get(url, auth = (username, token)).json()
	for value in repo_url['items']:
		repo_data = {"Name":" ", "Description":" ", "Languages":"", "Repo_url":""}
		user_repo = value['full_name']
		languages = getLanguageList(user_repo)

		if languages:
			repo_data['Languages'] = languages
		else:
			repo_data['Languages'] = 'null'

		print(count, "Extracting data from the ",value['name'], " repository")
		repo_data["Name"] = value['name']
		repo_data['Description'] = value['description']
		repo_data['Repo_url'] = value['html_url']

		if repo_data not in repo_json:
			repo_json.append(repo_data)
			count += 1
		else:
			print("Duplicate data, ignoring it!...")





#github credentials
username = "sumukus"
token = "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"

repo_json = []

count = 1

#https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}
urls = [
	f"https://api.github.com/search/repositories?q=fullstack-development&page=1&per_page=100&sort=stars&order=desc",
	f"https://api.github.com/search/repositories?q=application&page=1&per_page=100&sort=stars&order=desc",
	f"https://api.github.com/search/repositories?q=mean+stack&page=1&per_page=100&sort=stars&order=desc",
	f"https://api.github.com/search/repositories?q=mern+stack&page=1&per_page=100&sort=stars&order=desc",
	f"https://api.github.com/search/repositories?q=django+stack&page=1&per_page=100&sort=stars&order=desc",
	f"https://api.github.com/search/repositories?q=lamp+stack&page=1&per_page=100&sort=stars&order=desc",
	f"https://api.github.com/search/repositories?q=ruby+stack&page=1&per_page=100&sort=stars&order=desc"

]

print("Extracting repository and its information such as name, description, languages used")

for url in urls:
	getData(url)

with open("data_scrap_url.json", 'w') as jsonfile:
	json.dump(repo_json, jsonfile, indent=4, sort_keys=True)
	

print("The extraction of github repositories data completed!")
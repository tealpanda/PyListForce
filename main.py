import requests

# Todo 
# Make it //

target = "http://34.94.3.143/23f816a954/" # To be used as input
dictionary_file = "SVNDigger/all.txt" # To be used as input

with open(dictionary_file, 'r') as file:
    dictionary = file.readlines()

for word in dictionary:
    url = target + word.replace('\n', '')
    response = requests.get(url)

    if (response.status_code != 404):
        print(url)
        print(response.status_code)
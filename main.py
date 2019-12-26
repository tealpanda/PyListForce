import requests
import argparse

parser = argparse.ArgumentParser(description='Scans the target URL for potential hidden paths.')

parser.add_argument('target', help="The target URL to scan.")
parser.add_argument('--dict', default="all", help="The dictionary to use for scanning.")
args = vars(parser.parse_args())

#target = "http://34.94.3.143/23f816a954/" # To be used as input
dictionary_file = "SVNDigger/" + args['dict'] + ".txt" # To be used as input

with open(dictionary_file, 'r') as file:
    dictionary = file.readlines()

for word in dictionary:
    url = args['target'] + word.replace('\n', '')
    response = None
    try:
        response = requests.get(url)
    except:
        print(url)
        print('Exception')

    if (response):
        if (response.status_code != 404):
            print(url)
            print(response.status_code)
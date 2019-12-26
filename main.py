import requests
import argparse
import sys

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()  # As suggested by Rom Ruben (see: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console/27871113#comment50529068_27871113)

parser = argparse.ArgumentParser(description='Scans the target URL for potential hidden paths.')

parser.add_argument('target', help="The target URL to scan.")
parser.add_argument('--dict', default="all", help="The dictionary to use for scanning.")
args = vars(parser.parse_args())

#target = "http://34.94.3.143/23f816a954/" # To be used as input
dictionary_file = "SVNDigger/" + args['dict'] + ".txt" # To be used as input

with open(dictionary_file, 'r') as file:
    dictionary = file.readlines()

count = 0
for word in dictionary:
    url = args['target'] + word.replace('\n', '')
    response = None
    try:
        response = requests.get(url)
    except:
        pass
        #print(url)
        #print('Exception')

    if (response):
        if (response.status_code != 404):
            pass
            #print(url)
            #print(response.status_code)

    count += 1
    progress(count, len(dictionary), status='scanned')
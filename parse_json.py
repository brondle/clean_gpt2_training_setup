import argparse
import os
import json

parser = argparse.ArgumentParser()
parser.add_argument("-f", '--file_name')
args = parser.parse_args()

file_name = args.file_name

text = ''

with open(file_name, 'r') as json_file:
    data = json.load(json_file)
    for tweet in data:
        print('tweet: ' + tweet['tweet']['full_text'])
        text += "<|startoftext|>" +tweet['tweet']['full_text'] + "<|endoftext|>"
    output = open (file_name.split(".")[0] + ".txt", "w")
    output.write(text.encode('utf8'))
    output.close()


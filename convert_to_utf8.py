import argparse
import os
import json
import io

parser = argparse.ArgumentParser()
parser.add_argument("-f", '--file_name')
args = parser.parse_args()

file_name = args.file_name

text = ''

with io.open(file_name, 'r', encoding='utf-8') as f:
    text = f.read()
    output = io.open(file_name.split(".")[0] + "_encoded.txt", "w", encoding='utf-8')
    output.write(text)
    output.close()


import os
import csv
from nltk.corpus import stopwords
#from nltk.corpus import word_tokenize

csv_path = os.path.join("Resources", "us_wines.csv")

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    words = []

    for row in csvreader:
        words.append(row[1])

print(words)
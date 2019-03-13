from nltk.corpus import stopwords

file=open("word_cloud.txt", "r")

stop_words = set(stopwords.words('english'))

wordcount = {}

for word in file.read().split():
    word = word.lower()
    if word not in stop_words:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

filtered = []
for k, v in wordcount.items():
    filtered.append((v, k))

filtered = sorted(filtered, reverse=True)

for k in filtered:
    print '%s: %d' %(k[1], k[0])


file.close
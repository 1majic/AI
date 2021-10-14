import re

file_name = input()
words = {}
wordSplit = re.compile(r"[А-Яа-я]+")
stop = []

with open(file_name, 'r', encoding='utf-8') as f:
    fr = f.readlines()
    text = ' '.join(fr)
    text = re.sub(r"([^\s])-\n\s{1}", '\g<1>', text)
    for word in re.findall(wordSplit, text):
        if word.lower() not in stop:
            if word in words:
                words[word] = words[word] + 1
            else:
                words[word] = 1

sortedDict = [k for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)]
print(' '.join(sortedDict[0:50]))

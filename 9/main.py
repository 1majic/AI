import re

first_file = open(input(), 'r', encoding='utf-8').readlines()
second_file = open(input(), 'r', encoding='utf-8').readlines()
words = {}
wordSplit = re.compile(r"[А-Яа-я]+")
stop = []


def checker(words):
    text = ' '.join(words)
    text = re.sub(r"([^\s])-\n\s{1}", '\g<1>', text)
    for word in re.findall(wordSplit, text):
        if not word.lower() in stop:
            if word in words:
                words[word] = words[word] + 1
            else:
                words[word] = 1


sortedDict = [k for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)]
print(' '.join(sortedDict[0:50]))
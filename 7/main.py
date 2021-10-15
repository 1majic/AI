text = open(input(), 'r', encoding='utf-8').read().split()
k = 0
prep = ',.:;?!'
while k < len(text):
    if text[k] in prep:
        text[k-1] = text[k-1] + text[k]
        text.pop(k)
        k -= 1
    if
    k += 1
print(text)



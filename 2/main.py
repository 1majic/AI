def trans(chr):
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM"]

    t = thous[chr // 1000]
    h = hunds[chr // 100 % 10]
    te = tens[chr // 10 % 10]
    o = ones[chr % 10]

    return t + h + te + o


text = list(map(lambda x: x.strip('.'), input().split()))
for i in range(len(text)):
    if '.' not in text[i] and ',' not in text[i]:
        text[i] = trans(int(text[i]))
print(' '.join(text))
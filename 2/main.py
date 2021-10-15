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


text = open(input(), 'r').read().replace('\n', ' ').split()
for i in range(len(text)):
    if text[i].strip(',').strip('.').isdecimal():
        if text[i][0] in '.,':
            char = trans(int(text[i][1:])) + text[i][0]
        if text[i][-1] in '.,':
            char = trans(int(text[i][:-1])) + text[i][-1]
        else:
            char = trans(int(text[i]))
        text[i] = char
print(' '.join(text))
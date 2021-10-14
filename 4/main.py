text = open(input(), 'r', encoding='utf-8').read().replace('\n', '').replace('\r', '').replace('\t', '').split()
res = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']
god = []


def check(i):
    if i != '0x':
        char = set(i[2:])
        flag = True
        for j in char:
            if j not in res:
                flag = False
                break
        return flag
    else:
        return False


for i in text[::]:
    if i[:2] == '0x':
        if check(i):
            god.append(i)
    else:
        if check('0x' + i):
            god.append('0x' + i)

print(' '.join(god))
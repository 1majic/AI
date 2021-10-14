first = input().split()
second = input().split()
res = []
for i in second:
    if i in first:
        first.pop(first.index(i))
    else:
        res.append(i)
print(' '.join(res))
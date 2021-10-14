import codecs

denc = ["cp866",
        "cp1251",
        "koi8_r",
        "iso8859_5",
        "cp1251",
        'mac_cyrillic']
nice_symb = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789,. ;!:'[]()"

filename = input()
for i in denc:
    try:
        with codecs.open(filename, 'r', encoding=i) as f:
            fr = f.read().replace('\n', '').replace('\t', '').replace('\r', '')
            flag = True
            for j in fr[:len(fr) // 8]:
                if j not in nice_symb:
                    flag = False
                    break
            if flag:
                print(fr[:2049])
                break
    except Exception as e:
        continue
def reader():
    f = open('influenceKC111FL.csv')
    data1 = f.read()
    f.close()

    lines2 = data1.split('n')
    lines1 = data1.split(',')

    list = []

    c=0
    for line in lines1:
        # print line
        list.insert(c,line)
        c = c + 1

    return list

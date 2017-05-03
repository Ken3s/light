def reader():
    f = open('influenceKC111FL.csv')
    data1 = f.read()
    f.close()
    # print (data1)
    lines2 = data1.split('\n')
    #print lines2
    lines1 =[]
    for line in lines2:
        lines1 += line.split(',')
    # print (lines1)
    list = []

    c=0
    for line in lines1:
        # print line
        list.insert(c,line)
        c = c + 1
    # print (list)
    return list

def openOrSenior(data):
    # Hmmm.. Where to start?
    result=[]
    len=data.__len__()
    for i in range(len):
        if data[i][0]>=55 and data[i][1]>7:
            result.append('Senior')
        else:
            result.append('Open')
    return result
a=[[16, 23],[73,1],[56, 20],[1, -1]]
print openOrSenior(a)
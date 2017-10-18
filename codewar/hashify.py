# written by matthew
def hashify(string):
    #your code here
    res={}
    for i in range(len(string)):
        if res.has_key(string[i])==False:
            if i!=len(string)-1:
                res[string[i]]=string[i+1]
            else:
                res[string[i]]=string[0]
        else:
            if len(res[string[i]])==1:
                if i!=len(string)-1:
                    temp=[res[string[i]],string[i+1]]
                    res[string[i]]=temp
                else:
                    temp=[res[string[i]],string[0]]
                    res[string[i]] = temp
            else:
                if i!=len(string)-1:
                    res[string[i]].append(string[i+1])
                else:
                    res[string[i]].append(string[0])
    return res
print hashify("CcCcCcCc")
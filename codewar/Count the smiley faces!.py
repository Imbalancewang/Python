def count_smileys(arr):
    standard=[':)',':D',';)',';D',':-)',':-D',':~)',':~D',';-)',';-D',';~)',';~D']
    s=0
    for i in range(len(arr)):
        if arr[i] in standard:
            s+=1
    return s
print count_smileys([';]', ':[', ';*', ':$', ';-D'])
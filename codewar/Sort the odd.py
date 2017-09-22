def sort_array(source_array):
    odd=[x for x in source_array if x%2==1]
    odd.sort()
    for i in range(len(source_array)):
        if source_array[i]%2==0:
            odd.insert(i,source_array[i])
    return odd
print sort_array([])
def binary_array_to_number(arr):
    # your code
    dec=0
    mi=len(arr)-1
    for i in range(len(arr)):
        dec+=arr[i]*(2**mi)
        mi-=1
    return dec
print binary_array_to_number([1,1,1,1,1])

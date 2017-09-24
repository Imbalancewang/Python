def hamming(n):
    h = [1]
    i2, i3, i5 = 0, 0, 0
    for i in xrange(1, n+1):
        x = min(2 * h[i2], 3 * h[i3], 5 * h[i5])
        h.append(x)
        if 2 * h[i2] <= x: i2 += 1
        if 3 * h[i3] <= x: i3 += 1
        if 5 * h[i5] <= x: i5 += 1
    return h[n-1]
print hamming(1)
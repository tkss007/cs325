def stoogesort(L, i=0, j=None):
    if j is None:
        j = len(L) - 1
    if L[j] < L[i]:
        L[i], L[j] = L[j], L[i]
    if j - i > 1:
        t = (j - i + 1) // 3
        stoogesort(L, i, j - t)
        stoogesort(L, i + t, j)
        stoogesort(L, i, j - t)
    return L

array = []
with open("data.txt","r") as fd:
    for line in fd:
        array=line.split(' ')
        array = map(int, array)
        del array[0]
        result=" ".join(map(str,stoogesort(array)))
        print result
        with open("stooge.out","a") as f:
            f.write(result)
            f.write("\n")
fd.close()
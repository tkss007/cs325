def mergesort(lst):
    if (len(lst) <= 1): return lst
    left = mergesort(lst[:len(lst) / 2])
    right = mergesort(lst[len(lst) / 2:len(lst)])
    result = []
    while len(left) > 0 and len(right) > 0:
        if (left[0] > right[0]):
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    if (len(left) > 0):
        result.extend(mergesort(left))
    else:
        result.extend(mergesort(right))

    return result

array = []
with open("data.txt","r") as fd:
    for line in fd:
        array=line.split(' ')
        array = map(int, array)
        del array[0]
        result=" ".join(map(str,mergesort(array)))
        print result
        with open("merge.out","a") as f:
            f.write(result)
            f.write("\n")
fd.close()
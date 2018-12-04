# insert_sort
def insertsort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[min_index] > l[j]:
                min_index = j
        tmp = l[i]
        l[i] = l[min_index]
        l[min_index] = tmp
    return l


array = []
with open("data.txt","r") as fd:
    for line in fd:
        array=line.split(' ')
        array = map(int, array)
        del array[0]
        result=" ".join(map(str,insertsort(array)))
        print result
        with open("insert.out","a") as f:
            f.write(result)
            f.write("\n")
fd.close()
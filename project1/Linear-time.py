def max_subarray_linear(array):
    maximum = float('-inf')
    maxhere = 0
    n = len(array)
    subarray = []
    curarray = []
    for i in range(0, n):

        if (maxhere + array[i] > 0):
            maxhere = maxhere + array[i]
            curarray = curarray + [array[i]]
            #print curarray
            if maximum < maxhere:
                maximum = maxhere
                subarray = curarray
        else:
            curarray = []
            maxhere = 0


    return maximum, subarray


#list = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]
#print max_subarray_linear(list)

array = []
with open("MSS_TestProblems-1.txt","r") as fd:
    for line in fd:
        array=line.split(' ')
        array = map(int, array)
        result=" ".join(map(str,max_subarray_linear(array)))
        #print result
        with open("Results.txt","a") as f:
            f.write(result)
            f.write("\n")
fd.close()

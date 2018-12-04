def max_subarray_cubic(array):
    maximum = float('-inf')
    subarray = []
    n = len(array)
    for i in range(0, n):
        for j in range(i, n+1):
            current_sum = 0
            curarray = []
            for k in range(i, j):
                current_sum += array[k]
                curarray = curarray+ [array[k]]
                if current_sum > maximum:
                    maximum = current_sum
                    subarray = curarray
    return maximum, subarray


#list = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]
#print max_subarray_cubic(list)

array = []
with open("MSS_TestProblems-1.txt","r") as fd:
    for line in fd:
        array=line.split(' ')
        array = map(int, array)
        result=" ".join(map(str,max_subarray_cubic(array)))
        #print result
        with open("Results.txt","a") as f:
            f.write(result)
            f.write("\n")
fd.close()
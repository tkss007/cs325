def max_subarray_quadratic(array):
    maximum = float('-inf')
    n = len(array)
    subarray = []
    for i in range(0, n):
        curarray = []
        current_sum = 0
        for j in range(i, n):
            current_sum += array[j]
            curarray = curarray + [array[j]]
            if current_sum > maximum:
                maximum = current_sum
                subarray = curarray

    return maximum, subarray


#list = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]
#print max_subarray_quadratic(list)

array = []
with open("MSS_TestProblems-1.txt","r") as fd:
    for line in fd:
        array=line.split(' ')
        array = map(int, array)
        result=" ".join(map(str,max_subarray_quadratic(array)))
        #print result
        with open("Results.txt","a") as f:
            f.write(result)
            f.write("\n")
fd.close()
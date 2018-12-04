def max_cross_sum(array, low, mid, high):
    left_sum = float('-inf')
    cur_left = []
    sum_L = 0
    temp = []
    for i in range(mid, low-1, -1):
        sum_L += array[i]
        temp = [array[i]] + temp
        if sum_L > left_sum:
            left_sum = sum_L
            cur_left = temp

    right_sum = float('-inf')
    cur_right = []
    sum_R = 0
    temp = []
    for i in range(mid + 1, high+1):
        sum_R += array[i]
        temp = temp + [array[i]]
        if sum_R > right_sum:
            right_sum = sum_R
            cur_right = temp
    return left_sum + right_sum, cur_left + cur_right


def max_subarray_div_conquer(array, low, high):
    if low == high:
        return array[low]
    else:
        mid = (low + high) / 2
        return max(max_subarray_div_conquer(array, low, mid),
                   max_subarray_div_conquer(array, mid + 1, high),
                   max_cross_sum(array, low, mid, high))


array = []
with open("MSS_TestProblems-1.txt","r") as fd:
    for line in fd:
        array=line.split(' ')
        array = map(int, array)
        result=" ".join(map(str,max_subarray_div_conquer(array, 0, len(array)-1)))
        #print result
        with open("Results.txt","a") as f:
            f.write(result)
            f.write("\n")
fd.close()
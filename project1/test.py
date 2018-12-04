import random
import datetime

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



n = 1000
print n
list = [random.randint(-100, 100) for _ in range(n)]
print list
'''
starttime = datetime.datetime.now()
print max_subarray_cubic(list)
endtime = datetime.datetime.now()
cubictime = endtime - starttime
print (cubictime)

starttime = datetime.datetime.now()
print max_subarray_quadratic(list)
endtime = datetime.datetime.now()
quadratictime = endtime - starttime
print (quadratictime)

starttime = datetime.datetime.now()
print max_subarray_div_conquer(list, 0, len(list) - 1)
endtime = datetime.datetime.now()
div_conquer = endtime - starttime
print (div_conquer)

starttime = datetime.datetime.now()
print max_subarray_linear(list)
endtime = datetime.datetime.now()
lineartime = endtime - starttime
print (lineartime)
'''

array = []
with open("MSS_TestProblems-1.txt","r") as fd:
    for line in fd:
        array=line.split(' ')
        array = map(int, array)
        result1=" ".join(map(str,max_subarray_cubic(array)))
        result2=" ".join(map(str,max_subarray_quadratic(array)))
        result3=" ".join(map(str,max_subarray_div_conquer(array, 0, len(array)-1)))
        result4=" ".join(map(str,max_subarray_linear(array)))
        #print result
        with open("Results.txt","a") as f:
            f.write("------------------Test for each Algorithms------------------")
            f.write("\n")
            f.write(result1)
            f.write("\n")
            f.write(result2)
            f.write("\n")
            f.write(result3)
            f.write("\n")
            f.write(result4)
            f.write("\n")
            f.write("\n")
fd.close()

import datetime
import random

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

def main():
    n = 400
    print n
    lst = [random.randint(0, 10000) for _ in range(n)]


    starttime = datetime.datetime.now()
    print stoogesort(lst)
    endtime = datetime.datetime.now()
    print (endtime - starttime)


if __name__ == "__main__":
    main()
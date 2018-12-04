def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    list = []

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            list.append("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            list.append("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            list.append("Buzz")
        else:
            list.append(str(i))
    return str(list)

n = 15
print fizzBuzz(n)
print ord('A')
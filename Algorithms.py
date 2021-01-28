from utils import StringMatch, Divisors, Sumlist
from functools import lru_cache, reduce
from collections import deque

def BubbleSort(input_list: list) -> list:
    for iter_num in range(len(input_list)-1,0,-1):
        for idx in range(iter_num):
            if input_list[idx]>input_list[idx+1]:
                temp = input_list[idx]
                input_list[idx] = input_list[idx+1]
                input_list[idx+1] = temp
    return input_list

def _merge(left_half: list, right_half: list) -> list:
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

def MergeSort(unsorted_list: list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]
    left_list = MergeSort(left_list)
    right_list = MergeSort(right_list)
    return list(_merge(left_list, right_list))

def InsertionSort(InputList: list) -> list:
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element
    return InputList

def ShellSort(input_list: list) -> list:
    gap = len(input_list) // 2
    while gap > 0:
        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp
        gap = gap//2
    return input_list

def SelectionSort(input_list: list) -> list:
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
    return input_list

def zeros(sequence: list) -> list:
    zerosnum = sequence.count(0)
    sequence.sort()
    for i in range(0, zerosnum):
        sequence.remove(0)
    for i in range(0, zerosnum):
        sequence.append(0)
    return sequence

def WordsMatcher(*words: str, desiredwords: str, ignorecase: bool) -> dict:
    match = {}
    for word in words:
        match[word] = StringMatch(word, desiredwords, ignorecase)
    lowest = 100
    highest = 0
    for word in match.keys():
        if match[word] < lowest:
            lowest = match[word]
        if match[word] > highest:
            highest = match[word]
    match["lowest"] = lowest
    match["highest"] = highest
    return match

def reverse(listobj: list) -> list:
    r = []
    for i in range(0, len(listobj)-1):
        r.append(listobj.pop())
    return r

def Prime(number : int):
    if number == 0:
        return None
    elif number == 1:
        return True
    elif number == 2:
        return True
    else:
        for n in range(2, number, 2):
            if not number % n:
                return False
            else:
                return True

def Flatten(tree: list) -> list:
    nodes = []
    for node in tree:
        if type(node) != list:
            nodes.append(node)
        else:
            nodes.extend(Flatten(node))
    return nodes

@lru_cache(5000)
def Fibonacci(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def MultiplicativePersistence(n: int) -> list:
    if len(str(n)) == 1:
        return n
    digits = [int(j) for j in str(n)]
    result = 1
    for j in digits:
        result *= j
    return MultiplicativePersistence(result)

def PerfectNumber(n: int) -> bool:
    divisors = Divisors(n)
    divisors.remove(n)
    return Sumlist(divisors) == n

def FibonacciGenerator(start: int = 1, stop: int = 100, step: int = 1):
    for n in range(start, stop, step):
        yield Fibonacci(n)

def PrimeNumberGenerator(start: int = 0, stop: int = 100, step: int = 1):
    for n in range(start, stop, step):
        if Prime(n):
            yield n

def QuasiPerfectNumber(n: int) -> bool:
    divisors = Divisors(n)
    divisors.remove(n)
    return Sumlist(divisors) == n+1

def PerfectNumberGenerator(start: int = 0, stop: int = 100, step: int = 1):
    for n in range(start, stop, step):
        if PerfectNumber(n):
            yield n
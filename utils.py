from math import tanh
from math import degrees
from math import floor
from subprocess import getoutput
from os import system
from time import perf_counter

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower() + "`~!@#$%^&*()_-+=/-.|\{[]}:;'<>,./? 1234567890"+'"'

def angle(x: tuple, y: tuple) -> float:
    run = abs(x[0] - y[0])
    rise = abs(x[1] - y[1])
    slope = run / rise
    return degrees(tanh(slope))

def distance(object1: tuple, object2: tuple, dimension: int) -> dict:
    if dimension <= 3:
        dimensions = ["x", "y", "z"]
        dist = {}
        for i in range(0, dimension):
            dist[dimensions[i]] = abs(object1[i] - object2[i])
        return dist
    else:
        raise ValueError("Hmmm......really?")

def StringMatch(string1: list, string2: list, ignorecase: bool = False) -> int:
    match = 0
    for index in range(0, max(len(string1), len(string2))):
        try:
            if ignorecase:
                if string1[index].lower() == string2[index].lower():
                    match += 1
            else:
                if string1[index] == string2[index]:
                    match += 1
        except IndexError:
            pass
        finally:
            pass
    return (match / max(len(string1), len(string2))) * 100

def ConfigureCmd():
    system("echo off")
    system("color 0a")
    system("cls")

def TimedExecuter(seconds: int):
    start = perf_counter()
    while True:
        if perf_counter() - start > seconds:
            print("The Program is Terminated By the TimedExceuter")
            quit()

def reverse(input_list: list) -> list:
    rl = []
    for i in range(len(input_list)-1):
        rl.append(input_list.pop())
    return rl

def Factorial(n):
    if n == 0:
        return 1
    return n * Factorial(n-1)

def Sumlist(input_list: list) -> list:
    result = 0
    for i in input_list:
        result += i
    return result

def Divisors(n: int) -> list:
    divisors = []
    for i in range(1,n+1):
        if (n%i) == 0:
            divisors.append(i)
    return divisors

def BITVALIDITYCHECKER(n: int) -> bool:
    divisors = Divisors(n)
    divisors.remove(n)
    return (Sumlist(divisors)+1) == n

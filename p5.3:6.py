from p5_3_1c import *
import functools
import math
import itertools

TARGET = 10

N = (5,1,2,6,2,3)
SUM = sum(N)
PRODUCT = functools.reduce(lambda a, b: a*b, N, 1)

def solve(target, index, num_used):
    if num_used == target:
        if index < len(N):
            return
        else:
            yield tuple()
    elif index == len(N):
        return
    else:
        for num_to_take in range(1, target - num_used + 1):
            for choices in itertools.combinations(range(N[index]), num_to_take):
                for remaining in solve(target, index + 1, num_used+ num_to_take):
                    yield (choices, ) + remaining

def ans(k):
    count = 0
    for s in solve(k, 0, 0):
        count += 1
    return count
    #return (PRODUCT + P(SUM - len(N), k-len(N)))/math.factorial(k)

def P(n, k):
    return math.factorial(n) // math.factorial(n-k)
def C(n, k):
    return math.factorial(n) // (math.factorial(n-k)*math.factorial(k))

def gen_stuff_a():
    yield 0
    while True:
        yield 1

def gen_stuff_b(n):
    yield 0
    k = 1
    while k <= n:
        a = C(n, k)
        yield a
        k += 1
    while True:
        yield 0

t = tuple(gen_stuff_b(N[k]) for k in range(6))
g = functools.reduce(lambda a, b: generate_convolution(a, b), t[1:], t[0])
l = []
for k in range(TARGET+1):
    i = next(g)
    l.append(i)
print(l)
print(l[TARGET])
print(ans(TARGET))

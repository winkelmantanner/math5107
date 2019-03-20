import sys

def StirlingS2(n, k):
    if k == 1 or k == n:
        return 1
    elif n < k or k <= 0:
        raise Exception("StirlingS2 was passed invalid input: n=" + str(n) + ", k=" + str(k))
    else:
        return StirlingS2(n-1, k-1) + (k * StirlingS2(n-1, k))

if __name__=='__main__':
    for n in range(1, 12):
        for k in range(1, n+1):
            sys.stdout.write(" ")
            sys.stdout.write(str(StirlingS2(n, k)))
        print()


def a(k):
    if k == 1:
        return 2
    else:
        return (a(k-1) * 2) + b(k-1) + c(k-1)

def b(k):
    if k == 1:
        return 1
    else:
        return 4**(k-1)
def c(k):
    return b(k)

for k in range(1,5):
    print("a(" + str(k) + "):" + str(a(k)) + " b(" + str(k) + "):" + str(b(k)) + " c(" + str(k) + "):" + str(c(k)))

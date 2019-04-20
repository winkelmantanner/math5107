import itertools

def a():
    l = []
    for p in itertools.permutations(range(1,8+1)):
        if all(p[k] in {1,2,3,4} for k in range(4)):
            if not any(p[k] == k + 1 for k in range(8)):
                l.append(p)
    print(len(l))


a()

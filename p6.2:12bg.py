

def b(k):
    if k == 0:
        return 0
    if k == 1:
        return 8
    else:
        return (-7)*b(k-1) + 18*b(k-2)

def my_solution_to_b(k):
    return ((8/11)*(2**k) + (-8/11)*((-9)**k))

def j(k):
    known_solns = {0:2,1:1,2:0}
    if k in known_solns:
        return known_solns[k]
    else:
        return 2*j(k-1) + 9*j(k-2) + (-18)*j(k-3)


def my_solution_to_j(k):
    return (18/5)*(2**k) + (7/30)*((-3)**k) + (-11/6)*(3**k)

for k in range(10):
    print(str(b(k)) + ":" + str(my_solution_to_b(k)))
    print(str(j(k)) + ":" + str(my_solution_to_j(k)))

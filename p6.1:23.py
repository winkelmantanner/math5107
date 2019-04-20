
import itertools

def a():
    count = 0
    for p in itertools.permutations(range(1,9+1)):
        if all(p[(2 * k) - 1] == 2 * k for k in range(1,4+1)):
            if not any(p[(2*k) - 2] == (2 * k) - 1 for k in range(1,5+1)):
                count += 1
    print(count)



def b():
    count = 0
    for p in itertools.permutations(range(1,9+1)):
        num_in_natural_position = 0
        for k in range(9):
            if p[k] == k + 1:
                num_in_natural_position += 1
        if num_in_natural_position == 4:
            count += 1
    print(count)

a()
b()

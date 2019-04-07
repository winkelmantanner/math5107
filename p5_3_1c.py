TARGET_EXPONENT = 11
MINIMUMS = [3,3,2]

def generate_convolution(iterable1, iterable2):
    it1 = (e for e in iterable1)
    it2 = (e for e in iterable2)
    l1 = []
    l2 = []
    k = 0
    try:
        while True:
            l1.append(next(it1))
            l2.append(next(it2))
            my_sum = 0
            for j in range(k + 1):
                my_sum += l1[j]*l2[k-j]
            yield my_sum
            k += 1
    except StopIteration:
        return
def generate_possible_choices(minimums, target_sum):
    if not minimums and target_sum == 0:
        yield tuple()
    elif minimums:
        for k in range(minimums[0], target_sum + 1):
            for t in generate_possible_choices(minimums[1:], target_sum - k):
                yield (k,) + t


def main():
    count = 0
    for t in generate_possible_choices(MINIMUMS, TARGET_EXPONENT):
        print(t)
        count += 1
    print(count)

if __name__=='__main__':
    #main()
    print(tuple(generate_convolution(generate_convolution((0 if k < 3 else 1 for k in range(33)), (0 if k < 3 else 1 for k in range(33))), (0 if k < 2 else 1 for k in range(33))))[11])

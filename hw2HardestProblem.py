NUMBERS = tuple(range(10))

MIN_NUMBER = 0
MAX_NUMBER = 9

def generate_increasing_sequnces(length, increase_amount):
    if length == 1:
        for number in range(MIN_NUMBER, MAX_NUMBER + 1):
            yield (number, )
    else:
        for suffix_sequence in generate_increasing_sequnces(length - 1, increase_amount):
            for number in range(MIN_NUMBER, suffix_sequence[0] + 1 - increase_amount):
                yield (number, ) + suffix_sequence


counta = 0
for s in generate_increasing_sequnces(5, 1):
    counta += 1
countb = 0
for s in generate_increasing_sequnces(5, 0):
    countb += 1
print(counta)
print(countb)

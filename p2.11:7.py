DIGITS = {'1','2','3','4'}
CODEWORD_LENGTH = 12
def generate_all_codewords(number_of_digits, digit_set):
    if number_of_digits == 0:
        yield ''
    else:
        for digit in digit_set:
            for suffix in generate_all_codewords(number_of_digits - 1, digit_set):
                yield str(digit) + suffix

def contains_three_of_each_digit(codeword, digit_set):
   d = {digit: 0 for digit in digit_set}
   for character in codeword:
       d[character] += 1
   ok = True
   for character in d:
       if d[character] != 3:
           ok = False
   return ok


if __name__=='__main__':
    count = 0
    for codeword in generate_all_codewords(CODEWORD_LENGTH, DIGITS):
        if contains_three_of_each_digit(codeword, DIGITS):
            count += 1
    print(count)

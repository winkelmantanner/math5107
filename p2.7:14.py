
#Problem text:
#How many 8-letter words with no repeated letters can be constructed using the 26 letters of the alphabet if each word contains 3, 4, or 5 vowels?

LETTERS = tuple(chr(k + ord('A')) for k in range(ord('Z') - ord('A') + 1))

VOWELS = {'A', 'E', 'I', 'O', 'U'}

WORD_LENGTH = 8 # CHANGE THIS NUMBER TO 5 OR LESS TO ENABLE ENUMERATION

ACCEPTABLE_VOWEL_COUNTS = {3, 4, 5}

def generate_words_of_length_n(n):
    """
    This function generates all strings of length n consisting only of the upper case letters.
    """
    if n == 0:
        yield ''
    else:
        for word in generate_words_of_length_n(n - 1):
            for letter in LETTERS:
                yield letter + word

def count_vowels(word):
    count = 0
    for character in word:
        if character in VOWELS:
            count += 1
    return count

def does_contain_repeated_characters(word):
    character_set = set()
    for character in word:
        if character in character_set:
            return True
        character_set.add(character)
    return False

def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)

def C(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def P(n, r):
    return factorial(n) / factorial(n - r)

def compute_formula():
    count = 0
    for vowel_count in ACCEPTABLE_VOWEL_COUNTS:
        if vowel_count <= WORD_LENGTH:
            count += P(5, vowel_count) * C(WORD_LENGTH, vowel_count) * P(len(LETTERS) - len(VOWELS), WORD_LENGTH - vowel_count)
    return count

def main():
    answer_from_enumeration = 0
    if WORD_LENGTH < 6:
        count = 0
        for word in generate_words_of_length_n(WORD_LENGTH):
            if count_vowels(word) in ACCEPTABLE_VOWEL_COUNTS and not does_contain_repeated_characters(word):
                count += 1
        answer_from_enumeration = count
        print("Answer from enumeration:" + str(answer_from_enumeration))
    else:
        print("WORD_LENGTH is too big to enumerate")
    answer_from_formula = compute_formula()
    print("Answer from formula:" + str(answer_from_formula))

if __name__=='__main__':
    main()

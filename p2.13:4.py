# This program actually gets the right answer

if __name__=='__main__':
    p_sum = 0
    for starting_position in range(30 - 10 + 1):
        p = 1
        for well_index in range(starting_position-1+1):
            p *= ((20-well_index)/(30-well_index))
        for unwell_index in range(10):
            p *= ((10-unwell_index)/(30-starting_position-unwell_index))
        p_sum += p
    print(p_sum)


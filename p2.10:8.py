NUM_ELEMENTS = 11
MAX_NUM_PARTS = 3

def generate_partitions(num_elements, max_num_parts):
    return generate_partitions_with_max_part_size(num_elements, max_num_parts, num_elements)

def generate_partitions_with_max_part_size(num_elements, max_num_parts, max_part_size):
    if num_elements == 0:
        yield tuple()
    elif max_num_parts <= 0:
            return
    else:
        for first_part_size in range(1, max_part_size + 1):
            for sub_parts in generate_partitions_with_max_part_size(num_elements - first_part_size, max_num_parts - 1, min(max_part_size, first_part_size)):
                yield (first_part_size, ) + sub_parts

count = 0
for k in generate_partitions(NUM_ELEMENTS, MAX_NUM_PARTS):
    print(k)
    count += 1
print(count)

"""output
(4, 4, 3)
(5, 3, 3)
(5, 4, 2)
(5, 5, 1)
(6, 3, 2)
(6, 4, 1)
(6, 5)
(7, 2, 2)
(7, 3, 1)
(7, 4)
(8, 2, 1)
(8, 3)
(9, 1, 1)
(9, 2)
(10, 1)
(11,)
16
"""



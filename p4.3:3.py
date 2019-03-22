VALUES = {
        'A':(1,1,2,2),
        'B':(0,0,1,0),
        'C':(3,3,2,3),
        'D':(3,2,3,3),
        'E':(0,1,2,1),
        'F':(2,3,3,2)
        }



def compare_values_for_P(tuple1, tuple2):
    p = True
    for k in range(len(tuple1)):
        if tuple1[k] <= tuple2[k]:
            p = False
    return p

def compare_values_for_P_prime(tuple1, tuple2):
    p = True
    c = 0
    for k in range(len(tuple1)):
        if tuple1[k] <= tuple2[k]:
            c += 1
        if c >= 2:
            p = False
    return p

def compute_relation(values, value_comparator):
    relation = {k:set() for k in values}
    for software_package in values:
        for inner_software_package in values:
            if software_package != inner_software_package:
                if value_comparator(values[software_package], values[inner_software_package]):
                    relation[software_package].add(inner_software_package)
    return relation

print(compute_relation(VALUES, compare_values_for_P))
print(compute_relation(VALUES, compare_values_for_P_prime))

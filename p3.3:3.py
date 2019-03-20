
"""
GRAPH = \
{
        'a': {'b','c','d','f'},
        'b': {'a','c','d','e','f'},
        'c': {'a','b','d','e'},
        'd': {'a','b','c','e'},
        'e': {'b','c','d'},
        'f': {'a','b'},
}
"""
"""
GRAPH = {
        'a': {'b','f'},
        'b': {'c','e','a','d'},
        'c': {'f','e','b','d'},
        'd': {'c','b','f','e'},
        'e': {'b','c','d','f'},
        'f': {'c','a','e','d'}
}
"""
"""
GRAPH = {
        'a': {'b'},
        'b': {'a','c', 'd'},
        'c': {'b','e','d'},
        'd': {'b','c','f'},
        'e': {'c'},
        'f': {'d'}
}
"""
"""
GRAPH = {
        'a': {'b','c'},
        'b': {'a','c','d','e'},
        'c': {'a','b','d','e'},
        'd': {'b','c','e','f'},
        'e': {'b','c','d','f'},
        'f': {'d','e'}
}
"""
"""
GRAPH = {
        'a': {'b','c','d'},
        'b': {'a','c'},
        'c': {'a','b','d'},
        'd': {'a','c'},
}
"""
"""
GRAPH = {
        'a': {'b','c','d'},
        'b': {'a','c'},
        'c': {'a','b','e'},
        'd': {'a','e'},
        'e': {'c','d'}
}
"""
"""
GRAPH = {
        'a': {'b'},
        'b': {'a','c','d','e'},
        'c': {'b','e'},
        'd': {'b','e'},
        'e': {'b','c','d','f'},
        'f': {'e'}
}
"""
GRAPH = {
        'a': {'b','c'},
        'b': {'a','c','d'},
        'c': {'a','b','d'},
        'd': {'b','c'}
}

def assert_valid_graph(graph):
    for v, s in graph.items():
        for v_inner in s:
            assert v_inner in graph
            assert v in graph[v_inner]

def get_copy_of_graph(graph_to_copy):
    return {key: {a for a in s} for key, s in graph_to_copy.items()}

def get_contraction(map_of_adjacency_sets, edge_to_contract):
    """
    returns the result of contracting edge_to_contract in map_of_adjacency_sets
    """
    result = get_copy_of_graph(map_of_adjacency_sets)
    result[edge_to_contract[1]] = result[edge_to_contract[1]].union(result[edge_to_contract[0]])
    del result[edge_to_contract[0]]
    for vertex in result:
        if edge_to_contract[0] in result[vertex]:
            result[vertex].remove(edge_to_contract[0])
            result[vertex].add(edge_to_contract[1])
    result[edge_to_contract[1]].remove(edge_to_contract[1])
    assert_valid_graph(result)
    return result

def get_graph_with_edge_removed(map_of_adjacency_sets, edge_to_remove):
    """
    returns result of removing edge_to_remove from map_of_adjacency_sets
    """
    result = get_copy_of_graph(map_of_adjacency_sets)
    result[edge_to_remove[0]].remove(edge_to_remove[1])
    result[edge_to_remove[1]].remove(edge_to_remove[0])
    return result

def get_product_of_polynomials(map_from_exponent_to_coefficient_1, map_from_exponent_to_coefficient_2):
    result = dict()
    for exp1, coeff1 in map_from_exponent_to_coefficient_1.items():
        for exp2, coeff2 in map_from_exponent_to_coefficient_2.items():
            if exp1 + exp2 in result:
                result[exp1 + exp2] += coeff1 * coeff2
            else:
                result[exp1 + exp2] = coeff1 * coeff2
    return result

def get_scaled_polynomial(map_from_exponent_to_coefficient, scalar):
    return {exp: coeff * scalar for exp, coeff in map_from_exponent_to_coefficient.items()}

def get_sum_of_polynomials(map_from_exponent_to_coefficient_1, map_from_exponent_to_coefficient_2):
    result = dict()
    for exp, coeff in map_from_exponent_to_coefficient_1.items():
        result[exp] = coeff
    for exp, coeff in map_from_exponent_to_coefficient_2.items():
        if exp in result:
            result[exp] += coeff
        else:
            result[exp] = coeff
    return result

    

def get_chromatic_polynomial(map_from_vertex_to_adjacent_vertex_set):
    for vertex, edge_set in map_from_vertex_to_adjacent_vertex_set.items():
        if edge_set:
            return        get_sum_of_polynomials(get_chromatic_polynomial(get_graph_with_edge_removed(map_from_vertex_to_adjacent_vertex_set, (vertex, next(iter(edge_set))))),get_scaled_polynomial(
                get_chromatic_polynomial(
                        get_contraction(map_from_vertex_to_adjacent_vertex_set, (vertex, next(iter(edge_set))))),   -1))
    return {len(map_from_vertex_to_adjacent_vertex_set): 1}

def get_string_of_polynomial(map_from_exponenet_to_coefficient):
    first = True
    s = ''
    for exp, coeff in map_from_exponenet_to_coefficient.items():
        if not first:
            s += " + "
        first = False
        s += str(coeff) + "*x^" + str(exp)
    return s

assert_valid_graph(GRAPH)
print(get_string_of_polynomial(get_chromatic_polynomial(GRAPH)))

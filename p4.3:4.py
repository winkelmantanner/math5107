import copy

def get_digraph_from_diagram(diagram):
    """
    This function thinks a graph/diagram/digraph is a pair (V, E) or something like that.
    That doesn't work very well.  Use adjacency list/map/matrix instead.
    """

    vertex_set = diagram[0]
    edge_set = copy.deepcopy(diagram[1])
    keep_going = True
    # build transitive closure
    while keep_going:
        keep_going = False
        for v in vertex_set:
            for v2 in vertex_set:
                if (v, v2) in edge_set:

                    for v3 in vertex_set:
                        for v4 in vertex_set:
                            if (v3, v4) in edge_set:
                                edge_set.add((v, v4))
                                keep_going = True
    return (vertex_set, edge_set)



def is_after_in_diagram_adjacenty_map(d, v1, v2):
    """
    returns True if v1 is after v2, that is, returns
    True iff v2 R v1, where R is the relation given by the
    diagram
    """
    if v1 in d[v2]:
        return True
    else:
        for v in d[v2]:
            if is_after_in_diagram_adjacenty_map(d, v1, v):
                return True
    return False

def digraph_of_intersection_of_diagram_adjacency_maps(d1, d2):
    result = {k: set() for k in d1}
    for v11 in d1:
        for v12 in d1:
            if is_after_in_diagram_adjacenty_map(d1, v11, v12) and is_after_in_diagram_adjacenty_map(d2, v11, v12):
                result[v12].add(v11)
    return result

def get_diagram_from_digraph_adj_maps(digraph):
    """
    digraph must be transitive
    """
    result = {k:{e for e in digraph[k]} for k in digraph}
    edges_to_remove = set()
    for v1 in digraph:
        for v2 in digraph[v1]:
            for v3 in digraph[v2]:
                if v3 in digraph[v1]:
                    edges_to_remove.add((v1,v3))
    for edge in edges_to_remove:
        result[edge[0]].remove(edge[1])
    return result


def generate_all_linear_orders_from_diagram(diagram):
    if len(diagram) == 1:
        for element in diagram: # only iterates once
            yield (element, )
        return
    # Find a maximal element
    selected_maximal_element = 0
    for v in diagram:
        if len(diagram[v]) == 0:
            # v is maximal
            selected_maximal_element = v
            break
    subdiagram = dict()
    for element in diagram:
        if element != selected_maximal_element:
            subdiagram[element] = set()
        for element2 in diagram[element]:
            if element2 != selected_maximal_element:
                subdiagram[element].add(element2)
    for suborder in generate_all_linear_orders_from_diagram(subdiagram):
        yield suborder + (selected_maximal_element, )
        for k in range(len(suborder)):
            valid = True
            for j in range(k, len(suborder)):
                if selected_maximal_element in diagram[suborder[j]]:
                    valid = False
            if valid == True:
                yield suborder[:k] + (selected_maximal_element, ) + suborder[k:]

def get_subsets_of_size(s, size):
    if size == 0:
        yield set()
        return
    for e in s:
        for subset in get_subsets_of_size(s, size - 1):
            if not (e in subset):
                yield subset.union({e})

def get_diagram_of_linear_order(lo):
    diagram = {k:set() for k in lo}
    for k in range(len(lo)-1):
        diagram[lo[k]].add(lo[k+1])
    return diagram

def compute_dimension_from_diagram_adj_map(diagram):
    linear_orders = tuple(generate_all_linear_orders_from_diagram(diagram))
    dim = 1
    found = False
    while not found:
        for set_of_los in get_subsets_of_size(set(linear_orders), dim):
            diagram_inner = -1 # placeholder 
            for lo in set_of_los:
                if diagram_inner == -1:
                    diagram_inner = get_diagram_of_linear_order(lo)
                else:
                    diagram_inner = get_diagram_from_digraph_adj_maps(digraph_of_intersection_of_diagram_adjacency_maps(diagram_inner, get_diagram_of_linear_order(lo)))
            if diagram_inner == diagram:
                
                print("linear orders:")
                for lo in set_of_los:
                    print(lo)



                found = True
        if not found:
            dim += 1
    return dim


def get_diagram_of_intersection_of_diagrams(tuple_of_diagrams):
    """
    since dicts are unhashable, the diagrams, which are dicts, must be passed in a tuple rather than a set
    """
    aggregator_diagram = -1
    for current_diagram in tuple_of_diagrams:
        if aggregator_diagram == -1:
            aggregator_diagram = current_diagram
        else:
            aggregator_diagram = get_diagram_from_digraph_adj_maps(digraph_of_intersection_of_diagram_adjacency_maps(aggregator_diagram, current_diagram))
    return aggregator_diagram

def get_diagram_of_intersection_of_linear_orders(set_of_linear_orders):
    """
    a linear order is a tuple
    """
    diagram_tuple = tuple(get_diagram_of_linear_order(linear_order) for linear_order in set_of_linear_orders)
    return get_diagram_of_intersection_of_diagrams(diagram_tuple)


map1 = {'a':{'b'}, 'b':{'c'}, 'c':set()}
map2 = {'a':{'b', 'c'}, 'b':{'c'}, 'c':set()}

#print(get_diagram_from_digraph_adj_maps( digraph_of_intersection_of_diagram_adjacency_maps(map1, map2)))
"""
diagram4b = {
        'i':{'x','y'},
        'x':{'z','d'},
        'y':{'d','b'},
        'z':{'a'},
        'd':{'a','c'},
        'b':{'c'},
        'a':{'o'},
        'c':{'o'},
        'o':set()
}
"""
"""
diagram5a = {
        'a':{'b','c'},
        'b':{'d'},
        'c':{'d'},
        'd':set()
        }
"""
"""
test={
        'a':{'b','c'},
        'b':set(),
        'c':{'d'},
        'd':set()
        }
"""
figure4_20diagramb = {
        'b1':{'b4','b7','b5'},
        'b2':{'b6','b5'},
        'b3':{'b6','b7','b5'},
        'b4':{'b6'},
        'b5':set(),
        'b6':set(),
        'b7':set()
        }
"""
my_linear_orders = {
        ('b1','b2','b3','b5','b4','b6','b7'),
        ('b3','b2','b1','b7','b4','b6','b5'),
        ('b1','b4','b3','b7','b2','b5','b6')
        }
"""
#print(get_diagram_of_intersection_of_linear_orders(my_linear_orders))
#print(figure4_20diagramb)
#print(figure4_20diagramb == get_diagram_of_intersection_of_linear_orders(my_linear_orders))
#for lo in generate_all_linear_orders_from_diagram(figure4_20diagramb):
#    print(lo)
print(compute_dimension_from_diagram_adj_map(figure4_20diagramb))

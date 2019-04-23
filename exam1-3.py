

def find_path(graph, v_from, v_to):
    q = []
    q_ind = 0
    q.append(v_from)
    prev = dict()
    found = False
    while q_ind != len(q):
        current = q[q_ind]
        q_ind += 1
        if current == v_to:
            found = True
            break
        else:
            for adjacent_v in graph[current]:
                if adjacent_v not in prev:
                    q.append(adjacent_v)
                    prev[adjacent_v] = current
    if found:
        path = []
        current = v_to
        while current != v_from:
            path.append(current)
            current = prev[current]
        path = list(reversed(path))
        return path
    else:
        return None

def is_unilaterally_connected(adjacency_map):
    for edge in adjacency_map:
        for other_edge in adjacency_map:
            if other_edge != edge:
                if not(find_path(adjacency_map, edge, other_edge) or find_path(adjacency_map, other_edge, edge)):
                    return False
    return True



graph = {chr(n + ord('a')): set() for n in range(8)}
stop = False
while not stop:
    stop = True
    for v1 in graph:
        for v2 in graph:
            if not v2 in graph[v1]:
                if v1 != v2:
                    graph[v1].add(v2)
                    if(is_unilaterally_connected(graph)):
                        graph[v1].remove(v2)
                    else:
                        stop = False

print("maximum digraph on 8 vertices that is weakly connected but not unilaterally connected:")
print(graph)
num_arcs = 0
for v in graph:
    print(str(v) + ":" + str(len(graph[v])))
    num_arcs += len(graph[v])

print("num_arcs:" + str(num_arcs)) 


from collections import defaultdict
graph = defaultdict(list)

def add_edge(graph,u,v):
    graph[u].append(v)

def generate_edge(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node,neighbour))
    return edges

add_edge(graph,'a','c')
add_edge(graph,'b','c')
add_edge(graph,'b','e')
add_edge(graph,'c','d')
add_edge(graph,'c','e')
add_edge(graph,'c','a')
add_edge(graph,'c','b')
add_edge(graph,'e','b')
add_edge(graph,'d','c')
add_edge(graph,'e','c')

print(generate_edge(graph))
from collections import defaultdict
from heapq import *

def dijkstra(edges,source,destination):
    graph = defaultdict()
    for x,y,distance in edges:
        graph[x].append((y,distance))
    seen = set()
    distance = {source:0}
    queue = [(0,source,())]
    while queue:
        (cost,v1,path) = heappop(queue)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == destination: return (cost, path)

            for c, v2 in graph.get(v1, ()):
                if v2 in seen: continue
                prev = distance.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    distance[v2] = next
                    heappush(queue, (next, v2, path))

    return float("inf"), None

if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    print("=== Dijkstra ===")
    print(edges)
    print("A -> E:")
    print(dijkstra(edges, "A", "E"))
    print ("F -> G:")
    print(dijkstra(edges, "F", "G"))
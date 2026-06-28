import heapq

def prim(num_vertices, graph):
    visited = [False] * num_vertices
    min_heap = [(0, 0, -1)]
    mst = []
    total_cost = 0

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += weight
        if parent != -1:
            mst.append((parent, u, weight))

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    return mst, total_cost

num_vertices = 5
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)],
}

mst, cost = prim(num_vertices, graph)
print("Prim's Minimum Spanning Tree:")
print(f"{'Edge':<15} {'Weight'}")
print("-" * 25)
for u, v, w in mst:
    print(f"{u} -- {v}           {w}")
print(f"\nTotal MST Cost: {cost}")

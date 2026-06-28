class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def kruskal(num_vertices, edges):
    edges.sort(key=lambda e: e[2])
    ds = DisjointSet(num_vertices)
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

num_vertices = 5
edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9),
]

mst, cost = kruskal(num_vertices, edges)
print("Kruskal's Minimum Spanning Tree:")
print(f"{'Edge':<15} {'Weight'}")
print("-" * 25)
for u, v, w in mst:
    print(f"{u} -- {v}           {w}")
print(f"\nTotal MST Cost: {cost}")

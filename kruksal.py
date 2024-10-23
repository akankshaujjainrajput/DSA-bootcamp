# Define a class for the union-find data structure (Disjoint Set Union - DSU)
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    # Find the representative (root) of the set containing the vertex
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])  # Path compression
        return self.parent[vertex]

    # Union by rank - attach the smaller tree under the larger tree
    def union(self, root1, root2):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

# Function to perform Kruskal's Algorithm
def kruskal(graph):
    # Step 1: Sort all edges in non-decreasing order of their weight
    edges = sorted(graph['edges'], key=lambda x: x[2])
    
    # Initialize the disjoint set
    dsu = DisjointSet(graph['vertices'])
    
    mst = []  # This will store the edges of the Minimum Spanning Tree
    total_weight = 0  # To store the total weight of the MST
    
    # Step 2: Pick the smallest edge, and check if it forms a cycle using the DSU
    for u, v, weight in edges:
        root_u = dsu.find(u)
        root_v = dsu.find(v)
        
        # If u and v are in different sets, include this edge in the MST
        if root_u != root_v:
            mst.append((u, v, weight))
            total_weight += weight
            dsu.union(root_u, root_v)  # Union the sets of u and v

    return mst, total_weight

# Example graph with vertices and edges (each edge is represented as (u, v, weight))
graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
    'edges': [
        ('A', 'B', 4),
        ('A', 'F', 2),
        ('B', 'F', 5),
        ('B', 'C', 6),
        ('C', 'F', 1),
        ('C', 'D', 3),
        ('D', 'E', 7),
        ('E', 'F', 8),
    ]
}

def main():
    # Perform Kruskal's Algorithm on the graph
    mst, total_weight = kruskal(graph)
    
    # Print the edges in the Minimum Spanning Tree and the total weight
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")
    
    print(f"\nTotal weight of the Minimum Spanning Tree: {total_weight}")

if __name__ == "__main__":
    main()

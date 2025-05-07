# Kruskal's Algorithm to find the Minimum Spanning Tree (MST)
def kruskal(nodes, edges):
    # Initialize the parent for each node (used for Union-Find)
    parent = {i: i for i in nodes}

    # Function to find the root of a node with path compression
    def find(n):
        while parent[n] != n:
            parent[n] = parent[parent[n]]  # Path compression
            n = parent[n]
        return n

    # Function to unite two subsets (Union operation)
    def union(u, v):
        root1, root2 = find(u), find(v)
        if root1 != root2:
            parent[root2] = root1  # Make root1 the parent of root2
            return True
        return False  # If both nodes have same root, they are already connected

    mst_weight = 0       # Total cost of the MST
    mst_edges = []       # List to store the edges included in MST

    # Sort all edges in ascending order by weight
    edges.sort(key=lambda x: x[2])

    # Loop through each edge in sorted order
    for u, v, weight in edges:
        if union(u, v):                   # If u and v are not already connected
            mst_weight += weight         # Add the edge weight to total cost
            mst_edges.append((u, v, weight))  # Add this edge to MST

    return mst_edges, mst_weight         # Return the final MST and total cost

# Define the nodes (vertices) of the graph
nodes = ['A', 'B', 'C', 'D']

# Define the edges of the graph in the format: (node1, node2, weight)
edges = [
    ('A', 'B', 1),
    ('B', 'C', 1),
    ('A', 'C', 3),
    ('C', 'D', 5),
    ('B', 'D', 6)
]

# Run Kruskal's algorithm and capture the result
mst, cost = kruskal(nodes, edges)

# Display the output
print("Edges in MST (Kruskal):", mst)
print("Total cost:", cost)

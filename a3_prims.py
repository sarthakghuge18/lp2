# Import heapq to use the min-heap (priority queue)
import heapq

# Function to perform Prim's algorithm and return the total cost of the MST
def prim(graph, start):
    # Set to keep track of visited nodes to avoid cycles
    visited = set()
    
    # Min-heap to always process the edge with the minimum weight
    # Starts with the starting node and cost 0
    min_heap = [(0, start)]
    
    # Variable to store the total cost of the Minimum Spanning Tree
    mst_cost = 0

    # Continue until there are no more nodes in the heap
    while min_heap:
        # Pop the node with the smallest cost from the heap
        cost, node = heapq.heappop(min_heap)
        
        # If the node has not been visited, it becomes part of the MST
        if node not in visited:
            visited.add(node)        # Mark the node as visited
            mst_cost += cost         # Add its cost to the total MST cost

            # For all neighbors of the current node
            for neighbor, weight in graph[node]:
                # If the neighbor hasn't been visited yet, add to the heap
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor))

    # Return the final cost of the Minimum Spanning Tree
    return mst_cost

# Define the undirected, weighted graph as an adjacency list
# Each key is a node, and its value is a list of (neighbor, weight) tuples
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 1), ('D', 6)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 6), ('C', 5)]
}

# Call the prim function with the graph and starting node 'A'
# and print the total cost of the Minimum Spanning Tree
print("Total cost of MST (Prim):", prim(graph, 'A'))

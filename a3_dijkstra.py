# Import heapq to use a priority queue (min-heap)
import heapq

# Dijkstra's algorithm function to find shortest paths from a single source
def dijkstra(graph, start):
    # Step 1: Initialize distances of all nodes to infinity
    distances = {node: float('inf') for node in graph}
    
    # Distance to the starting node is 0
    distances[start] = 0

    # Step 2: Priority queue to store (distance, node)
    queue = [(0, start)]

    # Step 3: Process the queue
    while queue:
        # Get the node with the smallest known distance
        current_distance, current_node = heapq.heappop(queue)

        # Check all the neighbors of the current node
        for neighbor, weight in graph[current_node]:
            # Calculate the new distance through the current node
            distance = current_distance + weight

            # If the new distance is shorter, update and push to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    # Step 4: Return the dictionary of shortest distances
    return distances

# Example graph as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

# Output the shortest paths from node 'A'
print("Shortest paths from A:", dijkstra(graph, 'A'))

# A* Algorithm in Python using a graph represented as an adjacency list

class Graph:
    def __init__(self, adjacency_list):
        # Store the graph
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        # Return the neighbors and their edge weights of node v
        return self.adjacency_list.get(v, [])

    def h(self, n):
        # Heuristic function: Estimated cost from node 'n' to the goal
        H = {
            'A': 11,
            'B': 6,
            'C': 99,
            'D': 1,
            'E': 7,
            'G': 0
        }
        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # Initialize open_list with the start node
        open_list = set([start_node])
        # Closed list to track visited nodes
        closed_list = set([])

        # Store the cost from start node to current node (g value)
        g = {}
        g[start_node] = 0

        # Store the parent of each node to reconstruct path later
        parents = {}
        parents[start_node] = start_node

        while open_list:
            n = None

            # Choose node with the lowest f(n) = g(n) + h(n)
            for v in open_list:
                if n is None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n is None:
                print('Path does not exist!')
                return None

            # If goal is reached, reconstruct the path
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)
                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # Explore neighbors of current node
            for (m, weight) in self.get_neighbors(n):
                # If neighbor not visited
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    # If shorter path to m is found through n
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # Move n from open to closed (fully explored)
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

# Graph definition using adjacency list (node: [(neighbor, cost)])
adjac_lis = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'D': [('G', 1)],
    'E': [('D', 6)]
}

# Create graph object and run A* algorithm
graph = Graph(adjac_lis)
graph.a_star_algorithm('A', 'G')

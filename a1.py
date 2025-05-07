
#graph intilization
graph = {}


#add_edge
def add_edge(u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

#dfs
def dfs(node, visited):
    visited.append(node)
    print(node, end=" ")
    for neighbours in graph[node]:
        if neighbours not in visited :
            dfs(neighbours, visited)


#bfs
def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbours in graph[node]:
            if neighbours not in visited:
                visited.append(neighbours)
                queue.append(neighbours)


#main
edge = int(input("number of edges : "))

for i in range (edge):
    u = input("first point : ")
    v = input("second point : ")
    add_edge(u, v)

start = input("starting node : ")

dfs(start, [])

bfs(start)
from collections import deque

# Định nghĩa đồ thị (adjacency list)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1, 6],
    4: [1, 5],
    5: [2, 4, 6],
    6: [3, 5],
}

# DFS dùng stack (iterative)
def dfs_iterative(graph, start):
    visited = []
    stack = deque([start])

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for neighbor in reversed(graph[node]):  # đảo để giống DFS đệ quy
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

# DFS đệ quy
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

if __name__ == "__main__":
    start_node = 0
    
    # DFS iterative
    order_iter = dfs_iterative(graph, start_node)
    print("DFS (iterative) từ node", start_node, ":", order_iter)

    # DFS recursive
    order_rec = dfs_recursive(graph, start_node)
    print("DFS (recursive) từ node", start_node, ":", order_rec)




def dfs(graph, node):
    visited = []
    stack = deque()

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s,end = " ")

        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)
                
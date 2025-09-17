def BFS(graph, startNode, endNode):
    visitedNodes = []
    queue = [startNode]
    predecessorNodes = {}

    while queue:
        currentNode = queue.pop(0)
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)
            for neighbor in graph[currentNode]:
                if neighbor not in visitedNodes:
                    queue.append(neighbor)
                    predecessorNodes[neighbor] = currentNode
    
    shortestPath(predecessorNodes, startNode, endNode)
    return visitedNodes

def shortestPath(predecessorNodes, startNode, endNode):
    currentNode = endNode
    path = [endNode]

    while currentNode != startNode:
        currentNode = predecessorNodes[currentNode]
        path.append(currentNode)
    path.reverse()
    return path

# Test
graph = {
    0: [3, 9, 5],
    1: [6, 4, 7],
    2: [10, 5],
    3: [0],
    4: [1, 5, 8],
    5: [0, 2, 4],
    6: [1],
    7: [1],
    8: [4],
    9: [0],
    10: [2]
}

print("Visited order:", BFS(graph, 2, 6))
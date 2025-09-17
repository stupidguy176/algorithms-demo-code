import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import matplotlib.animation as animation

def bfs_animation(graph, start):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G, seed=42)  
    visited = set()
    queue = deque([start])
    visited.add(start)

    frames = []  
    dist = {start: 0}

    while queue:
        v = queue.popleft()
        frames.append((set(visited), list(queue), v))

        for w in graph[v]:
            if w not in visited:
                visited.add(w)
                dist[w] = dist[v] + 1
                queue.append(w)
                frames.append((set(visited), list(queue), v))

    # Vẽ animation
    fig, ax = plt.subplots(figsize=(5, 5))

    def update(frame):
        ax.clear()
        visited_nodes, queue_nodes, current = frame
        colors = []
        for node in G.nodes():
            if node == current:
                colors.append("red")  
            elif node in queue_nodes:
                colors.append("orange")  
            elif node in visited_nodes:
                colors.append("lightblue")  
            else:
                colors.append("lightgray")  
        
        nx.draw(G, pos, with_labels=True, node_color=colors, ax=ax, node_size=600, font_size=12)
        ax.set_title(f"BFS Step {frames.index(frame)+1}")

    ani = animation.FuncAnimation(fig, update, frames=frames, interval=1500, repeat=False)
    return ani

# Example graph
graph = {
    1: [2,3,9],
    2: [1,3,4,7],
    3: [1,2,5,7,9],
    4: [2],
    5: [3],
    6: [9],
    7: [2,3],
    8: [9],
    9: [1,3,6,8]
}

ani = bfs_animation(graph, 1)
ani.save("bfs_animation.gif", writer="pillow")
"bfs_animation.gif"

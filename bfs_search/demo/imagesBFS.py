# Create step-by-step BFS images that also show the internal arrays (visited, queue, dist)
import os
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
from copy import deepcopy
from matplotlib.backends.backend_pdf import PdfPages

def bfs_step_snapshots(graph, start):
    """
    Return a list of frames. Each frame is a dict with:
      - 'visited': set
      - 'queue': list
      - 'current': node being processed (or None at init)
      - 'dist': dict {node: distance}
      - 'event': text describing what just happened
    Frames include both 'pop' (visit) and 'discover' moments.
    """
    visited = set([start])
    queue = deque([start])
    dist = {start: 0}
    frames = []
    
    # initial frame (before processing anything)
    frames.append({
        "visited": deepcopy(visited),
        "queue": list(queue),
        "current": None,
        "dist": deepcopy(dist),
        "event": f"Initialize: push {start}, dist[{start}]=0"
    })
    
    while queue:
        v = queue.popleft()
        frames.append({
            "visited": deepcopy(visited),
            "queue": list(queue),
            "current": v,
            "dist": deepcopy(dist),
            "event": f"Pop {v} from queue"
        })
        for w in graph[v]:
            if w not in visited:
                visited.add(w)
                dist[w] = dist[v] + 1
                queue.append(w)
                frames.append({
                    "visited": deepcopy(visited),
                    "queue": list(queue),
                    "current": v,
                    "dist": deepcopy(dist),
                    "event": f"Discover {w}: set dist[{w}]={dist[w]}, push {w}"
                })
    return frames

def draw_frame(G, pos, frame, step_idx, outpath):
    """
    Draw a single frame: the graph (colored by state) + side panel showing arrays.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    
    visited = frame["visited"]
    q = frame["queue"]
    current = frame["current"]
    dist = frame["dist"]
    
    # color nodes by state
    colors = []
    for node in G.nodes():
        if node == current:
            colors.append("red")         # current processing
        elif node in q:
            colors.append("orange")      # in queue
        elif node in visited:
            colors.append("lightblue")   # visited
        else:
            colors.append("lightgray")   # unvisited
    
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=650, font_size=11, ax=ax)
    ax.set_title(f"BFS Step {step_idx}", pad=10)
    
    # side panel with arrays
    panel_text = []
    panel_text.append(f"Event: {frame['event']}")
    panel_text.append("")
    panel_text.append(f"Current: {current}")
    panel_text.append(f"Visited: {sorted(list(visited))}")
    panel_text.append(f"Queue: {list(q)}")
    # dist pretty print sorted by node id
    dist_items = ", ".join([f"{k}:{dist[k]}" for k in sorted(dist.keys())])
    panel_text.append(f"dist: {{{dist_items}}}")
    
    # put in text box on the right
    txt = "\n".join(panel_text)
    ax.text(1.04, 0.5, txt, transform=ax.transAxes, va="center", ha="left",
            fontsize=10, family="monospace",
            bbox=dict(boxstyle="round,pad=0.5", edgecolor="black", facecolor="#f5f5f5"))
    
    plt.tight_layout()
    fig.savefig(outpath, dpi=160, bbox_inches="tight")
    plt.close(fig)

def bfs_images_with_arrays(graph, start, outdir="bfs_steps_arrays", seed=42):
    if not os.path.exists(outdir):
        os.makedirs(outdir, exist_ok=True)
    
    # Build graph + layout
    G = nx.Graph(graph)
    pos = nx.spring_layout(G, seed=seed)
    
    # compute frames
    frames = bfs_step_snapshots(graph, start)
    
    # draw and save each frame as PNG
    file_paths = []
    for i, frame in enumerate(frames, start=1):
        fname = f"step_{i:03d}.png"
        fpath = os.path.join(outdir, fname)
        draw_frame(G, pos, frame, i, fpath)
        file_paths.append(fpath)
    
    # also compile to a single PDF for easy viewing
    pdf_path = os.path.join(outdir, "bfs_steps.pdf")
    with PdfPages(pdf_path) as pdf:
        for f in file_paths:
            img = plt.imread(f)
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.imshow(img)
            ax.axis("off")
            pdf.savefig(fig, bbox_inches="tight")
            plt.close(fig)
    
    return file_paths, pdf_path

# ----- Run on the user's example graph -----
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

pngs, pdf_file = bfs_images_with_arrays(graph, start=1)
pngs[:5], pdf_file

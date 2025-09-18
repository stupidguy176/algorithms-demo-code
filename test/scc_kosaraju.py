#!/usr/bin/env python3
import sys
from collections import deque

"""
Kosaraju's SCC (iterative DFS, memory-conscious)

Usage:
  python scc_kosaraju.py /path/to/scc.txt
  pypy3 scc_kosaraju.py /path/to/scc.txt   (recommended)

Notes:
- No recursion (iterative DFS) to avoid recursion depth issues.
- Builds both G and Grev adjacency lists in one streaming pass.
- Handles vertex labels 1..875714 (sparse-safe; missing nodes allowed).
- Prints top-5 SCC sizes as 'a,b,c,d,e'.
"""

def read_graph(path, max_label_hint=875714):
    # We don't know the true max label without a scan; use the hint,
    # and grow lists on-the-fly if we encounter larger labels.
    G = [[] for _ in range(max_label_hint + 1)]
    Gr = [[] for _ in range(max_label_hint + 1)]
    max_seen = 0

    # Stream read file
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Tolerate extra spaces / tabs
            parts = line.split()
            if len(parts) < 2:
                continue  # ignore malformed lines
            try:
                u = int(parts[0])
                v = int(parts[1])
            except ValueError:
                continue  # ignore header-esque junk lines

            if u > max_seen: max_seen = u
            if v > max_seen: max_seen = v

            # Grow adjacency lists if needed
            if max_seen >= len(G):
                grow = max_seen + 1 - len(G)
                G.extend([] for _ in range(grow))
                Gr.extend([] for _ in range(grow))

            G[u].append(v)
            Gr[v].append(u)
    return G, Gr, max_seen


def iterative_dfs_order(Grev, N):
    """
    First pass: on reversed graph.
    Returns finishing order list.
    """
    visited = [False] * (N + 1)
    order = []

    for s in range(N, 0, -1):
        if visited[s]:
            continue
        if not Grev[s]:
            # Still need to mark isolated vertices
            visited[s] = True
            order.append(s)
            continue

        # Simulate recursion for DFS(s) to compute finishing times
        stack = [(s, 0)]  # (node, next_child_idx)
        visited[s] = True
        while stack:
            node, i = stack[-1]
            if i < len(Grev[node]):
                nxt = Grev[node][i]
                stack[-1] = (node, i + 1)
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append((nxt, 0))
            else:
                # all children processed => finished
                order.append(node)
                stack.pop()
    return order


def iterative_dfs_scc(G, order, N):
    """
    Second pass: on original graph in decreasing finishing order.
    Returns a list of SCC sizes.
    """
    visited = [False] * (N + 1)
    scc_sizes = []

    for s in reversed(order):
        if s < 1 or s > N or visited[s]:
            continue
        if not G[s]:
            # isolated vertex or sink with no outgoing edges
            visited[s] = True
            scc_sizes.append(1)
            continue

        # Explore one SCC starting at s
        size = 0
        stack = [s]
        visited[s] = True
        while stack:
            node = stack.pop()
            size += 1
            # manual loop (slightly faster than for n in G[node])
            adj = G[node]
            for j in range(len(adj)):
                nxt = adj[j]
                if nxt <= N and not visited[nxt]:
                    visited[nxt] = True
                    stack.append(nxt)
        scc_sizes.append(size)
    return scc_sizes


def main():
    if len(sys.argv) < 2:
        print("Usage: python scc_kosaraju.py /path/to/scc.txt", file=sys.stderr)
        sys.exit(2)

    path = sys.argv[1]
    # 1) Read graph + reverse
    G, Grev, N = read_graph(path)
    # 2) First pass on reverse graph: finishing order
    order = iterative_dfs_order(Grev, N)
    # 3) Second pass on original graph: SCC sizes
    scc_sizes = iterative_dfs_scc(G, order, N)

    # Top 5 in decreasing order, zero-padded
    scc_sizes.sort(reverse=True)
    top5 = (scc_sizes + [0, 0, 0, 0, 0])[:5]
    print(",".join(str(x) for x in top5))


if __name__ == "__main__":
    main()

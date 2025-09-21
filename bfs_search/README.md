

## 📘 Lecture Content

1. **Introduction to BFS (Breadth-First Search)**

   * Explore the graph layer by layer.
   * Applications: computing the **shortest path** and finding **connected components**.
   * Running time: **O(m + n)** (linear in the number of edges + vertices).

2. **BFS Algorithm Pseudocode**

   * Initialization: mark the starting vertex as explored, put it into a queue.
   * Loop: remove the first element from the queue, traverse all edges (v, w).

     * If w has not been explored → mark it as explored and put it into the queue.
   * The queue is **FIFO** (First In, First Out).

3. **Basic Properties**

   * **Claim 1:** BFS correctly finds the set of vertices reachable from source s.
   * **Claim 2:** Running time of the main loop is **O(ns + ms)**, where ns = number of reachable vertices, ms = number of reachable edges.

4. **BFS and Shortest Path**

   * Define **dist(v)** = the minimum number of edges on the path from s to v.
   * While traversing edge (v, w): if w is unexplored → `dist(w) = dist(v) + 1`.
   * Result: dist(v) = i ⇔ v belongs to layer i (corresponding to the number of edges in the shortest path).

5. **Application: Connected Components (undirected graph)**

   * Definition of connected component: a set of vertices where every pair is connected by a path.
   * Method:

     * Initialize all vertices as unexplored.
     * Traverse all vertices; if a vertex is unexplored → run BFS(G, i) to find the connected component containing i.
   * Total running time: **O(m + n)**.

---

## 🔑 Key Terms

* **Graph primitives**
* **Breadth-First Search (BFS)**
* **Layers**
* **Queue (FIFO)**
* **Explored / unexplored**
* **Shortest paths**
* **dist(v)**
* **Connected components**
* **O(m + n)** (linear complexity)

---

## Links

[https://www.coursera.org/learn/algorithms-graphs-data-structures](https://www.coursera.org/learn/algorithms-graphs-data-structures)
[https://www.youtube.com/watch?v=HZ5YTanv5QE](https://www.youtube.com/watch?v=HZ5YTanv5QE)
[https://www.youtube.com/watch?v=xlVX7dXLS64](https://www.youtube.com/watch?v=xlVX7dXLS64)


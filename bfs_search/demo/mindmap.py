from graphviz import Digraph

# Create a mindmap with Graphviz
dot = Digraph(comment="BFS Mindmap", format="png")
dot.attr(rankdir="LR", size="8,5")

# Main topic
dot.node("BFS", "Breadth-First Search (BFS)", shape="oval", style="filled", color="lightblue")

# Subtopics
dot.node("Def", "Định nghĩa & Ý tưởng\n- Duyệt theo lớp (layers)\n- Sử dụng Queue (FIFO)", shape="box", color="lightyellow")
dot.edge("BFS", "Def")

dot.node("Code", "Thuật toán BFS\n- Mark explored\n- Queue\n- While loop", shape="box", color="lightyellow")
dot.edge("BFS", "Code")

dot.node("Props", "Tính chất\n- v được thăm <=> có đường từ s\n- Thời gian: O(ns+ms)", shape="box", color="lightyellow")
dot.edge("BFS", "Props")

dot.node("SP", "Ứng dụng 1: Shortest Paths\n- dist(v)\n- dist(s)=0, others=∞\n- Cập nhật: dist(w)=dist(v)+1", shape="box", color="lightyellow")
dot.edge("BFS", "SP")

dot.node("CC", "Ứng dụng 2: Connected Components\n- Duyệt BFS với các đỉnh chưa thăm\n- Tìm thành phần liên thông\n- Thời gian: O(m+n)", shape="box", color="lightyellow")
dot.edge("BFS", "CC")

# Save mindmap
file_path = "bfs_mindmap"
dot.render(file_path, cleanup=True)
print(file_path + ".png")




## 📘 Nội dung bài giảng

1. **Giới thiệu DFS (Depth-First Search)**

   * Khám phá “sâu nhất có thể”, chỉ backtrack khi cần thiết.
   * Ứng dụng:

     * Tính **thứ tự topo (topological ordering)** trong đồ thị có hướng không chu trình (DAG).
     * Tìm **các thành phần liên thông mạnh (SCCs)** trong đồ thị có hướng.
   * Thời gian chạy: **O(m + n)**.

2. **Thuật toán DFS**

   * Có thể mô phỏng BFS nhưng dùng **stack** thay cho queue.
   * Phiên bản đệ quy:

     * Đánh dấu đỉnh s đã thăm.
     * Với mỗi cạnh (s, v): nếu v chưa thăm → gọi đệ quy DFS(G, v).

3. **Tính chất cơ bản**

   * **Claim 1:** Một đỉnh v được đánh dấu đã thăm ⇔ tồn tại đường đi từ s đến v.
   * **Claim 2:** Thời gian chạy **O(ns + ms)** với ns = số đỉnh reachable từ s, ms = số cạnh reachable từ s.
   * Mỗi đỉnh được duyệt nhiều nhất 1 lần, mỗi cạnh nhiều nhất 2 lần.

4. **Ứng dụng: Topological Sort**

   * **Định nghĩa:** Một thứ tự topo là gán nhãn các đỉnh {1,…,n} sao cho với mọi cạnh (u, v) thì f(u) < f(v).
   * Điều kiện: Đồ thị có chu trình có hướng ⇒ không tồn tại thứ tự topo.
   * **DFS-Loop algorithm:**

     * Gán nhãn ngược theo thứ tự hoàn tất của DFS.
     * Thời gian chạy O(m + n).
   * **Tính đúng đắn:** Nếu (u, v) là cạnh thì f(u) < f(v).

5. **Ứng dụng khác: Strongly Connected Components (SCCs)**

   * DFS là công cụ quan trọng để phân tích cấu trúc của đồ thị có hướng, đặc biệt trong việc tìm các SCCs (sẽ thường học tiếp trong các phần sau).

---

## 🔑 Từ khóa quan trọng

* **Graph primitives**
* **Depth-First Search (DFS)**
* **Stack** / **Recursion**
* **Explored / unexplored**
* **Topological ordering**
* **Directed Acyclic Graph (DAG)**
* **Strongly Connected Components (SCCs)**
* **O(m + n)** (độ phức tạp tuyến tính)
* **DFS-Loop**
* **Finishing times**

---

## 📊 So sánh BFS và DFS

| Đặc điểm              | **BFS (Breadth-First Search)**                                            | **DFS (Depth-First Search)**                                           |
| --------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Chiến lược duyệt**  | Đi theo **tầng/lớp** (layers), mở rộng đều từ đỉnh gốc                    | Đi theo **nhánh sâu nhất** có thể, chỉ backtrack khi cần               |
| **Cấu trúc dữ liệu**  | **Queue (FIFO)**                                                          | **Stack (LIFO)** hoặc **Recursion**                                    |
| **Ứng dụng chính**    | - Tìm đường đi ngắn nhất (unweighted graph)<br>- Tìm connected components | - Topological sort (DAG)<br>- Tìm Strongly Connected Components (SCCs) |
| **Độ phức tạp**       | **O(m + n)**                                                              | **O(m + n)**                                                           |
| **Kết quả điển hình** | Cho ta số lớp (distance = số cạnh ít nhất từ s)                           | Cho ta thời điểm bắt đầu/kết thúc (useful cho topo sort, SCC)          |
| **Tư duy**            | Giống lan tỏa sóng nước                                                   | Giống đào sâu một con đường                                            |

---
---

## Links

https://www.coursera.org/learn/algorithms-graphs-data-structures
https://www.youtube.com/watch?v=Urx87-NMm6c&t=105s
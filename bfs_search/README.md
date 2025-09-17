
## 📘 Nội dung bài giảng

1. **Giới thiệu BFS (Breadth-First Search)**

   * Khám phá đồ thị theo từng “lớp” (layers).
   * Ứng dụng trong việc tính **đường đi ngắn nhất** và tìm **thành phần liên thông**.
   * Thời gian chạy: **O(m + n)** (tuyến tính theo số cạnh + số đỉnh).

2. **Giả mã thuật toán BFS**

   * Khởi tạo: đánh dấu đỉnh bắt đầu là explored, cho vào hàng đợi (queue).
   * Vòng lặp: lấy phần tử đầu tiên ra khỏi queue, duyệt tất cả cạnh (v, w).

     * Nếu w chưa được khám phá → đánh dấu explored, đưa vào queue.
   * Queue là **FIFO** (First In, First Out).

3. **Các tính chất cơ bản**

   * **Claim 1:** BFS tìm chính xác tập các đỉnh reachable từ đỉnh s.
   * **Claim 2:** Thời gian vòng lặp chính là **O(ns + ms)**, với ns = số đỉnh reachable, ms = số cạnh reachable.

4. **BFS và Shortest Path**

   * Định nghĩa **dist(v)** = số cạnh ít nhất trên đường đi từ s đến v.
   * Khi duyệt cạnh (v, w): nếu w chưa explored → `dist(w) = dist(v) + 1`.
   * Kết quả: dist(v) = i ⇔ v nằm ở lớp i (tương ứng với số cạnh trong đường đi ngắn nhất).

5. **Ứng dụng: Connected Components (đồ thị vô hướng)**

   * Định nghĩa thành phần liên thông: tập đỉnh mà giữa mọi cặp đều có đường đi.
   * Cách làm:

     * Khởi tạo tất cả đỉnh chưa explored.
     * Duyệt qua tất cả các đỉnh, nếu chưa explored → chạy BFS(G, i) để tìm thành phần liên thông chứa i.
   * Thời gian chạy tổng: **O(m + n)**.

---

## 🔑 Từ khóa quan trọng

* **Graph primitives**
* **Breadth-First Search (BFS)**
* **Layers**
* **Queue (FIFO)**
* **Explored / unexplored**
* **Shortest paths**
* **dist(v)**
* **Connected components**
* **O(m + n)** (độ phức tạp tuyến tính)

---

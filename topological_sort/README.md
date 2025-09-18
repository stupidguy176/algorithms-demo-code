

## 📘 Nội dung bài giảng về **Topological Sort**

### 1. Định nghĩa

* **Topological ordering** của một đồ thị có hướng $G$ là một gán nhãn $f$ cho các đỉnh sao cho:

  1. Các nhãn $f(v)$ là tập $\{1, 2, …, n\}$.
  2. Với mọi cạnh $(u, v)$ thì $f(u) < f(v)$.

👉 Nghĩa là: các đỉnh được sắp xếp sao cho **mọi cạnh luôn đi từ đỉnh có nhãn nhỏ → đỉnh có nhãn lớn**.

### 2. Điều kiện tồn tại

* Nếu đồ thị có **chu trình có hướng (directed cycle)** → **không tồn tại** thứ tự topo.
* Nếu đồ thị là **DAG (Directed Acyclic Graph)** → luôn có ít nhất một thứ tự topo.

### 3. Ứng dụng

* Lập lịch công việc (sắp xếp các tasks mà có ràng buộc trước-sau).
* Biểu diễn dependency (ví dụ: biên dịch code, course prerequisites).

### 4. Thuật toán cơ bản (Straightforward solution)

* Mọi DAG luôn có một **sink vertex** (đỉnh không có cạnh đi ra).
* Cách làm:

  1. Chọn một sink vertex $v$.
  2. Gán $f(v) = n$.
  3. Xóa $v$ khỏi đồ thị.
  4. Lặp lại cho đến khi hết đỉnh.

⏳ Độ phức tạp: $O(m + n)$.

### 5. Thuật toán DFS (Slick solution)

* Dùng DFS để tìm **thứ tự hoàn tất (finishing times)**:

  * Khi DFS kết thúc ở một đỉnh $s$, gán cho nó nhãn $f(s) = current\_label$.
  * Giảm `current_label` sau mỗi bước.
* Cuối cùng, sắp xếp các đỉnh theo thứ tự nhãn giảm dần → được **topological order**.

### 6. Tính đúng đắn

* Với mỗi cạnh $(u, v)$:

  * Nếu $u$ được duyệt trước $v$: lời gọi đệ quy DFS(v) hoàn tất trước DFS(u). → $f(v) > f(u)$.
  * Nếu $v$ được duyệt trước $u$: lời gọi DFS(v) hoàn tất hoàn toàn trước khi DFS(u) bắt đầu. → $f(v) > f(u)$.
* Vì đồ thị không có chu trình, ta luôn đảm bảo $f(u) < f(v)$.

---

## 🔑 Từ khóa quan trọng

* **Topological ordering**
* **Directed Acyclic Graph (DAG)**
* **Sink vertex**
* **DFS finishing times**
* **DFS-Loop**
* **No directed cycles → topo order exists**
* **O(m + n)**

## Links

https://www.youtube.com/watch?v=7J3GadLzydI

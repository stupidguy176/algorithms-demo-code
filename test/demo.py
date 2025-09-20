# demo_fast.py
from bisect import bisect_left, bisect_right

L, H = -10000, 10000

# 1. Read numbers into a set (for fast lookup) and a sorted list
with open("algo1-programming_prob-2sum.txt") as f:
    numbers = {int(line) for line in f}

A = sorted(numbers)  # sorted list of unique numbers
targets = set()

# 2. For each x, only scan y in the valid range
for x in A:
    lo, hi = L - x, H - x  # y must be within this range
    Lidx = bisect_left(A, lo)
    Ridx = bisect_right(A, hi)
    for y in A[Lidx:Ridx]:
        if y != x:
            t = x + y
            if L <= t <= H:
                targets.add(t)

# 3. Print result
print(len(targets))

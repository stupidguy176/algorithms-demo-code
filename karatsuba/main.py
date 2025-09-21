import timeit
import random

# --- Code A ---
def karatsuba_A(x, y):
    if x < 10 or y < 10:  # Base case: single-digit multiplication
        return x * y
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    half_val = (10 ** half)
    a = x // half_val
    b = x % half_val
    c = y // half_val
    d = y % half_val
    ac = karatsuba_A(a, c)
    bd = karatsuba_A(b, d)
    ad_plus_bc = karatsuba_A(a + b, c + d) - ac - bd
    return ac * (10 ** (2 * half)) + (ad_plus_bc * half_val) + bd

# --- Code B ---
def karatsuba_B(x, y):
    if x < 10 or y < 10:  # Base case: single-digit multiplication
        return x * y
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    a = x // 10 ** half
    b = x % 10 ** half
    c = y // 10 ** half
    d = y % 10 ** half
    ac = karatsuba_B(a, c)
    bd = karatsuba_B(b, d)
    ad_plus_bc = karatsuba_B(a + b, c + d) - ac - bd
    return ac * (10 ** (2 * half)) + (ad_plus_bc * 10 ** half) + bd

# --- Generate two random numbers with 1000 digits ---
x = int("".join(str(random.randint(0, 9)) for _ in range(1000)))
y = int("".join(str(random.randint(0, 9)) for _ in range(1000)))

# --- Benchmark ---
setup_A = "from __main__ import karatsuba_A, x, y"
setup_B = "from __main__ import karatsuba_B, x, y"

time_A = timeit.timeit("karatsuba_A(x,y)", setup=setup_A, number=1)
time_B = timeit.timeit("karatsuba_B(x,y)", setup=setup_B, number=1)

print("Code A (1000 digits):", time_A, "seconds")
print("Code B (1000 digits):", time_B, "seconds")

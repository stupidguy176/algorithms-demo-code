import sys

# 123456
def karatsuba(x,y):
    # Base case
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)),len(str(y)))
    half = n // 2
    half_val = (10 ** (half))
    print("half_val", half_val)

    a = x // half_val
    b = x % half_val
    c = y // half_val
    d = y % half_val

    print("a", a)
    print("b", b)
    print("c", c)
    print("d", d)

    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_plus_bc = karatsuba(a+b,c+d) - ac - bd

    return ac * (10 ** (2*half)) + (ad_plus_bc * half_val) + bd

if __name__ == "__main__":
    if len(sys.argv) > 1:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print(karatsuba(x,y))
    else:
        print(karatsuba(123456,789123))

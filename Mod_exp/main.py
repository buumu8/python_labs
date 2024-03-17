def FastModularExponentiation(b, k, m):

    assert m > 0 and k >= 0
    if k == 0:
        return b
    if k == 1:
        return b * b
    if k % 2 == 0:
        return FastModularExponentiation((b**k) % m, k // 2, m)
    else:
        return (FastModularExponentiation(b, k - 1, m) * b * b) % m


print(FastModularExponentiation(2, 5, 2))

def pow(a, b):
    if b == 0:
        return 1
    result = 1
    exp = abs(b)
    while exp > 0:
        result *= a
        exp -= 1
    return result if b > 0 else 1 / result

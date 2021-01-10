def recursion(a, b):
    if b == 1:
        return a
    else:
        return a + recursion(a, b-1)
print(recursion(4,2))

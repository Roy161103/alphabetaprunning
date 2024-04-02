def is_valid(A, B, C):
    return A > B and B != C and A != C


def backtracking(A, B, C):
    if len(A) == 0:
        return None

    a = A.pop(0)
    for b in B:
        if b in A:
            continue
        for c in C:
            if c in (A + [b]):
                continue
            if is_valid(a, b, c):
                return (a, b, c)
    return backtracking(A, B, C)


A = [2, 3, 5]
B = [2, 3, 5]
C = [2, 3, 5]

solution = backtracking(A, B, C)
print("Solusi pertama yang memenuhi constraint: ", solution)

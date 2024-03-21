def is_valid_assignment(assignment):
    a, b, c = assignment
    if None in assignment:
        return False
    return a > b and b != c and a != c

def backtrack(assignment, domain, index):
    if index == len(assignment):
        return assignment

    for value in domain:
        assignment[index] = value
        if is_valid_assignment(assignment):
            result = backtrack(assignment.copy(), domain, index + 1)
            if result is not None:
                return result
    return None

def find_solution():
    domain = [2, 3, 5]
    assignment = [None, None, None]
    return backtrack(assignment, domain, 0)

solution = find_solution()
if solution is not None:
    print("Solusi pertama yang memenuhi constraint:")
    print("A =", solution[0])
    print("B =", solution[1])
    print("C =", solution[2])
else:
    print("Tidak ada solusi yang memenuhi constraint.")

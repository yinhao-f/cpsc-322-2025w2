variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
domain = [1, 2, 3, 4]

fail_count = 0
solutions = []

def is_consistent(assignment):
    """
    Checks all constraints that can be evaluated
    with the current partial assignment.
    Returns True if consistent, False otherwise.
    """
    global fail_count

    def assigned(x):
        return x in assignment

    def val(x):
        return assignment[x]

    # Constraints

    # A > G
    if assigned('A') and assigned('G'):
        if not (val('A') > val('G')):
            fail_count += 1
            return False

    # A ≤ H
    if assigned('A') and assigned('H'):
        if not (val('A') <= val('H')):
            fail_count += 1
            return False

    # |F-B| = 1
    if assigned('F') and assigned('B'):
        if not (abs(val('F') - val('B')) == 1):
            fail_count += 1
            return False

    # G < H
    if assigned('G') and assigned('H'):
        if not (val('G') < val('H')):
            fail_count += 1
            return False

    # |G-C| = 1
    if assigned('G') and assigned('C'):
        if not (abs(val('G') - val('C')) == 1):
            fail_count += 1
            return False

    # |H-C| is even
    if assigned('H') and assigned('C'):
        if not (abs(val('H') - val('C')) % 2 == 0):
            fail_count += 1
            return False

    # H != D
    if assigned('H') and assigned('D'):
        if not (val('H') != val('D')):
            fail_count += 1
            return False

    # D ≥ G
    if assigned('D') and assigned('G'):
        if not (val('D') >= val('G')):
            fail_count += 1
            return False

    # D != C
    if assigned('D') and assigned('C'):
        if not (val('D') != val('C')):
            fail_count += 1
            return False

    # E != C
    if assigned('E') and assigned('C'):
        if not (val('E') != val('C')):
            fail_count += 1
            return False

    # E < D-1
    if assigned('E') and assigned('D'):
        if not (val('E') < val('D') - 1):
            fail_count += 1
            return False

    # E != H-2
    if assigned('E') and assigned('H'):
        if not (val('E') != val('H') - 2):
            fail_count += 1
            return False

    # G != F
    if assigned('G') and assigned('F'):
        if not (val('G') != val('F')):
            fail_count += 1
            return False

    # H != F
    if assigned('H') and assigned('F'):
        if not (val('H') != val('F')):
            fail_count += 1
            return False

    # C != F
    if assigned('C') and assigned('F'):
        if not (val('C') != val('F')):
            fail_count += 1
            return False

    # D != F-1
    if assigned('D') and assigned('F'):
        if not (val('D') != val('F') - 1):
            fail_count += 1
            return False

    # |E-F| is odd
    if assigned('E') and assigned('F'):
        if not (abs(val('E') - val('F')) % 2 == 1):
            fail_count += 1
            return False

    return True


def dfs(assignment, depth=0):
    """
    Depth-First Search with pruning.
    Prints the search tree and records solutions.
    """
    if len(assignment) == len(variables):
        print("    " * depth + "solution:", assignment)
        solutions.append(assignment.copy())
        return

    var = variables[len(assignment)]

    for value in domain:
        assignment[var] = value

        print("    " * depth + f"{var}={value}", end=" ")

        if is_consistent(assignment):
            print()
            dfs(assignment, depth + 1)
        else:
            print("failure")

        del assignment[var]


# Run DFS
dfs({})

print("\nTotal solutions found:", len(solutions))
print("Failing consistency checks:", fail_count)

print("\nSolutions:")
for sol in solutions:
    print(sol)

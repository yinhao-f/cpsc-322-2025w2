import cspExamples
from collections import deque

def bfs_solver(csp):

    solutions = []
    frontier = [{}]

    while frontier:
        assignment = frontier.pop(0) 

        if len(assignment) == len(csp.variables):
            solutions.append(assignment.copy())
            continue

        var = None
        for v in csp.variables:
            if v not in assignment:
                var = v
                break

        if var is None:
            continue

        for value in var.domain:
            new_assignment = assignment.copy()
            new_assignment[var] = value

            if all(constraint.holds(new_assignment) for constraint in csp.constraints
                   if all(variable in new_assignment for variable in csp.variables)):  
                frontier.append(new_assignment)

    return solutions

if __name__ == "__main__":
    solutions = bfs_solver(cspExamples.csp2)
    print(solutions)

solutions = bfs_solver(cspExamples.csp2)

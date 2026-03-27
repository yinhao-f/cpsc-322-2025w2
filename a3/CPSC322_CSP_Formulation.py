from cspProblem import Variable, CSP, Constraint   
from cspConsistencyGUI import ConsistencyGUI

def meet_at(p1, p2):
    def meets(w1, w2):
        return w1[p1] == w2[p2]
    meets.__name__ = f"meet_at({p1}, {p2})"
    return meets

words = {'card', 'wood', 'herd', 'salt', 'look', 'slow', 'live'}

cell1 = Variable('one_down', words)
cell2 = Variable('two_down', words)
cell3 = Variable('three_accross', words)
cell4 = Variable('four_across', words)

crossword_puzzle = CSP(
    "word_puzzle",
    {cell1, cell2, cell3, cell4},
    [
        Constraint([cell1, cell3], meet_at(1,0),"1d[1]==3a[0]"),
        Constraint([cell1, cell4], meet_at(3,0),"1d[3]==4a[0]"),
        Constraint([cell2, cell3], meet_at(1,3),"2d[1]==3a[3]"),
        Constraint([cell2, cell4], meet_at(3,3),"2d[3]==4a[3]")
    ]
)

ConsistencyGUI(crossword_puzzle, fontsize=10).go()

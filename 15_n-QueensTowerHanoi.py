# n-Queens & Tower of Hanoi problem using python
def tower_of_hanoi(n, from_peg, to_peg, aux_peg):
    if n > 0:
        tower_of_hanoi(n-1, from_peg, aux_peg, to_peg)
        print("Move disk", n, "from peg", from_peg, "to peg", to_peg)
        tower_of_hanoi(n-1, aux_peg, to_peg, from_peg)

n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
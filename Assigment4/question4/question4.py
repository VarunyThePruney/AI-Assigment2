from itertools import permutations

def solve():
    letters = ('T', 'W', 'O', 'F', 'U', 'R')
    digits = range(10)

    for perm in permutations(digits, 6):
        T, W, O, F, U, R = perm

        if T == 0 or F == 0:
            continue

        two = 100*T + 10*W + O
        four = 1000*F + 100*O + 10*U + R

        if two + two == four:
            print("Solution Found")
            print("T =", T)
            print("W =", W)
            print("O =", O)
            print("F =", F)
            print("U =", U)
            print("R =", R)
            print()
            print(two, "+", two, "=", four)
            return
solve()
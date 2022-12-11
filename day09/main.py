with open('input.txt') as f:
    data = [(d, int(m)) for d, m in [line.strip().split() for line in f]]


def plot_rope(knots):
    h, w = 21, 26
    m = []
    for row in range(h):
        line = ""
        for col in range(w):
            line += str(knots.index(
                (col, row))) if (col, row) in knots else '.'
        m.append(line)
    for l in m[::-1]:
        print(l)
    print()


def move_rope(knots):
    for i in range(len(knots) - 1):
        kx, ky = knots[i + 1]
        kix, kiy = knots[i]
        if abs(kix - kx) > 1 or abs(kiy - ky) > 1:
            if kix > kx:
                # Move Right
                kx += 1
            elif kix < kx:
                # Move Left
                kx -= 1
            if kiy > ky:
                # Move Up
                ky += 1
            elif kiy < ky:
                # Move Down
                ky -= 1
            knots[i + 1] = (kx, ky)
    return knots


def solve(data, l):
    MOVES = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}
    knots = [(0, 0)] * l
    visited = {}

    for dir, moves in data:
        dx, dy = MOVES[dir]
        for _ in range(moves):
            # Move Head
            knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
            # Move Knot
            knots = move_rope(knots)
            visited.add(knots[-1])
        # plot_rope(knots)
    return len(visited)


print(solve(data, 2))
print(solve(data, 10))

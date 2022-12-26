import re


def main():
    m, path = parse_input('input.txt')
    print(solve(m, path, True))
    print(solve(m, path, False))


def parse_input(file):
    with open(file) as f:
        m, path = f.read().split('\n\n')
        m = m.split('\n')
        grid = []
        for line in m:
            if len(line) < 150:
                line += ' ' * (150 - len(line))
            grid.append([c for c in line])
        path = re.findall(r"\d+|L|R", path)
    return grid, path


def solve(grid, path, part1):
    path_list = list()
    row, col = 0, grid[0].index('.')
    dr, dc = 0, 1

    for op in path:
        if op.isdigit():
            for s in range(int(op)):
                row, col, dr, dc = move(grid, dr, dc, row, col, part1)
        else:
            if op == 'R':
                dr, dc = dc, -dr
            elif op == 'L':
                dr, dc = -dc, dr

    d_pointer = [(0, 1), (1, 0), (0, -1), (-1, 0)].index((dr, dc))
    return (row + 1) * 1000 + (col + 1) * 4 + d_pointer


def move(grid, dr, dc, row, col, part1):
    if part1:
        nr = (row + dr) % len(grid)
        nc = (col + dc) % len(grid[0])
        ndr, ndc = dr, dc
        while grid[nr][nc] == ' ':
            nr = (nr + dr) % len(grid)
            nc = (nc + dc) % len(grid[0])
    else:
        nr, nc = row + dr, col + dc
        ndr, ndc = dr, dc
        if len(grid[0]) <= nc or nc < 0 or len(grid) <= nr or nr < 0 or grid[nr][nc] == ' ':
            nr, nc, ndr, ndc = find_next_face(row, col, dr, dc)

    if grid[nr][nc] == '#':
        return row, col, dr, dc
    return nr, nc, ndr, ndc


def find_next_face(row, col, dr, dc):
    face_transition = {
        (1, 0, -1): (0, 1, lambda r, c: (149 - r, 0)),
        (1, -1, 0): (0, 1, lambda r, c: (c - 50 + 150, 0)),
        (2, 0, 1): (0, -1, lambda r, c: (149 - r, 99)),
        (2, -1, 0): (-1, 0, lambda r, c: (199, c - 100)),
        (2, 1, 0): (0, -1, lambda r, c: (c - 100 + 50, 99)),
        (4, 0, 1): (-1, 0, lambda r, c: (49, r - 50 + 100)),
        (4, 0, -1): (1, 0, lambda r, c: (100, r - 50)),
        (6, 0, -1): (0, 1, lambda r, c: (49 - (r - 100), 50)),
        (6, -1, 0): (0, 1, lambda r, c: (c + 50, 50)),
        (7, 0, 1): (0, -1, lambda r, c: (49 - (r - 100), 149)),
        (7, 1, 0): (0, -1, lambda r, c: (150 + (c - 50), 49)),
        (9, 0, 1): (-1, 0, lambda r, c: (149, (r - 150) + 50)),
        (9, 0, -1): (1, 0, lambda r, c: (0, r - 150 + 50)),
        (9, 1, 0): (1, 0, lambda r, c: (0, c + 100))
    }
    face = row // 50 * 3 + col // 50
    dr, dc, f = face_transition[(face, dr, dc)]
    nr, nc = f(row, col)
    return nr, nc, dr, dc


# transition table for the example input
def find_next_face2(row, col, dr, dc):
    face_transition = {
        (2, 0, 1): (0, -1, lambda r, c: (11 - r, 15)),
        (2, 0, -1): (1, 0, lambda r, c: (5, 4 + r)),
        (2, -1, 0): (-1, 0, lambda r, c: (5, 3 - (8 - c))),
        (4, -1, 0): (1, 0, lambda r, c: (0, 8 + (3 - c))),
        (4, 0, -1): (-1, 0, lambda r, c: (11, 15 - (4 - r))),
        (4, 1, 0): (-1, 0, lambda r, c: (11, 8 + (3 - c))),
        (5, -1, 0): (0, 1, lambda r, c: ((c - 4), 8)),
        (5, 1, 0): (0, 1, lambda r, c: (8 + (7 - c), 8)),
        (6, 0, 1): (1, 0, lambda r, c: (8, 15 - (r - 4))),
        (10, 0, -1): (-1, 0, lambda r, c: (7, 8 - (r - 8))),
        (10, 1, 0): (-1, 0, lambda r, c: (7, (11 - c))),
        (11, -1, 0): (0, -1, lambda r, c: (4 + (15 - c), 11)),
        (11, 0, 1): (0, -1, lambda r, c: (11 - r, 11)),
        (11, 1, 0): (0, 1, lambda r, c: (4 + (15 - r), 0)),
    }
    face = ((row // 4) * 4) + (col // 4)
    dr, dc, f = face_transition[(face, dr, dc)]
    nr, nc = f(row, col)
    return nr, nc, dr, dc


if __name__ == '__main__':
    main()

    # Map for the real input
    #       1 2
    #       4
    #     6 7
    #     9
    #    1 > 2(>)    2 > 7(<)    4 > 2(^)    6 > 7(>)    7 > 2(<)    9 > 7(^)
    #    1 < 6(>)    2 < 1(<)    4 < 6(v)    6 < 1(>)    7 < 6(<)    9 < 1(v)
    #    1 v 4(v)    2 v 4(<)    4 v 7(v)    6 v 9(v)    7 v 9(<)    9 v 2(v)
    #    1 ^ 9(>)    2 ^ 9(^)    4 ^ 1(^)    6 ^ 4(>)    7 ^ 4(^)    9 ^ 6(^)

    # Map for the example input
    #         2
    #     4 5 6
    #         10 11
    #
    #    2 > 11(<)   4 ^ 2(v)    5 ^ 2(>)    6 > 11(v)    10 < 5(^)    11 ^ 6(<)
    #    2 < 5(v)    4 < 11(^)   5 v 10(>)                10 v 4(^)    11 > 2(<)
    #   ?2 ^ 4(v)    4 v 10(^)                                         11 v 4(>)

#!/usr/local/bin/python

def main():
    print(solve(parse_input('input.txt'), 10, True))
    print(solve(parse_input('input.txt'), 1000, False))


def parse_input(file):
    grid = set()
    with open(file) as f:
        for i, line in enumerate(f):
            for j, x in enumerate(line.strip()):
                if x == '#':
                    grid.add((j, i))
    return grid


def solve(grid, rounds, part1):
    d_order = 'NSWE'
    possible_moves = dict()
    for r in range(rounds):
        # first half
        for (x, y) in grid:
            nx, ny = possible_move(x, y, grid, d_order)
            if (nx, ny) != (x, y):
                possible_moves[(x, y)] = (nx, ny)
        # part 2
        if len(possible_moves) == 0 and not part1:
            return r + 1
        # second half
        for (cx, cy), (px, py) in possible_moves.items():
            if list(possible_moves.values()).count((px, py)) == 1:
                grid.remove((cx, cy))
                grid.add((px, py))

        d_order = d_order[1:] + d_order[0]
        possible_moves.clear()

    # count empty tiles
    x_ = [x for x, _ in grid]
    y_ = [y for _, y in grid]
    minx, maxx = min(x_), max(x_)
    miny, maxy = min(y_), max(y_)
    empty_tiles = ((maxx - minx + 1) * (maxy - miny + 1)) - len(grid)

    if part1:
        return empty_tiles


def possible_move(x, y, grid, d_order):
    adj_dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    check_dirs = {'N': [(0, -1), (-1, -1), (1, -1)],
                  'S': [(0, 1), (-1, 1), (1, 1)],
                  'W': [(-1, 0), (-1, -1), (-1, 1)],
                  'E': [(1, 0), (1, -1), (1, 1)],
                  }
    if not any((x + dx, y + dy) in grid for dx, dy in adj_dirs):
        return x, y
    for d in d_order:
        if not any((x + dx, y + dy) in grid for dx, dy in check_dirs[d]):
            return x + check_dirs[d][0][0], y + check_dirs[d][0][1]
    return x, y


if __name__ == '__main__':
    main()

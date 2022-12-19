#!/usr/local/bin/python


def main():
    with open('input.txt') as f:
        gas = [c for c in f.read().strip()]
    print(solve(gas))


def solve(gas):
    grid = {(x, 0) for x in range(7)}
    shapes = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (0, 1), (1, 1)]
    ]

    pointer = 0
    rocks = 1_000_000_000_000
    counter = 0
    added = 0
    maxy = 0
    part1 = 0
    seen = {}
    while counter < rocks:
        shape = shapes[counter % len(shapes)]
        grid, pointer = rock_move(shape, grid, gas, pointer)
        if counter <= 2022:
            part1 = maxy
        if counter > 2021:
            sr = (counter % len(shapes), pointer, top_grid(grid))
            if sr in seen:
                old_rock, old_y = seen[sr]
                dy = maxy - old_y
                dt = counter - old_rock
                amt = (rocks - counter) // dt
                added += amt*dy
                counter += amt*dt

            seen[sr] = counter, maxy
        counter += 1
        maxy = max_y(grid)
    part2 = maxy + added
    return part1, part2


def top_grid(grid):
    maxy = max_y(grid)
    return frozenset((x, maxy - y) for (x, y) in grid if maxy - y <= 30)


def plot_grid(grid):
    for r in range(max_y(grid) + 7, -2, -1):
        line = ""
        for c in range(7):
            line += '#' if (c, r) in grid else '.'
        print(line)


def max_y(grid):
    return max([y for (_, y) in grid])


def rock_move(shape, grid, gas, pointer):
    rest = False
    start_y = max_y(grid) + 4
    start_x = 2
    shape = [(sx + start_x, sy + start_y) for (sx, sy) in shape]

    while not rest:
        d = gas[pointer]
        lx = min([x for (x, _) in shape])
        rx = max([x for (x, _) in shape])

        if d == '<' and lx > 0 and all((x - 1, y) not in grid for (x, y) in shape):
            shape = [(nsx - 1, nsy) for (nsx, nsy) in shape]
        elif d == '>' and rx < 6 and all((x + 1, y) not in grid for (x, y) in shape):
            shape = [(nsx + 1, nsy) for (nsx, nsy) in shape]
        pointer = (pointer + 1) % len(gas)
        if any((x, y - 1) in grid for (x, y) in shape):
            rest = True
        else:
            shape = [(nsx, nsy - 1) for (nsx, nsy) in shape]

    for (sx, sy) in shape:
        grid.add((sx, sy))
    return grid, pointer


if __name__ == '__main__':
    main()

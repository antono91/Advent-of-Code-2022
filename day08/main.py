def main():
    with open('input.txt') as f:
        m = {}
        trees = [[int(i) for i in line.strip()] for line in f]
        for i, r in enumerate(trees):
            for j, c in enumerate(r):
                m[(i, j)] = c
                
    print(solve(m))


def is_visible(m, pos):
    DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for xi, yi in DIR:
        dir = []
        new_pos = (pos[0] + xi, pos[1] + yi)
        while new_pos in m:
            dir.append(new_pos)
            new_pos = (new_pos[0] + xi, new_pos[1] + yi)
        if all(m[p] < m[pos] for p in dir):
            return True
    return False


def scenic_score(m, pos):
    DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ss = 1
    for xi, yi in DIR:
        score = 0
        new_pos = (pos[0] + xi, pos[1] + yi)
        found_block = False
        while new_pos in m and not found_block:
            score += 1
            if m[new_pos] < m[pos]:
                new_pos = (new_pos[0] + xi, new_pos[1] + yi)
            else:
                found_block = True

        ss *= score
    return ss


def solve(m):
    return sum(is_visible(m, p) for p in m), max(scenic_score(m, p) for p in m)


if __name__ == '__main__':
    main()

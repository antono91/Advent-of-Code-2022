import os


def main():
    with open('input.txt') as f:
        tree = {}
        for line in f:
            line = line.strip()
            if line.startswith("$"):
                _, cmd, *dir = line.split()
                if cmd == "cd":
                    path = dir[0]
                    if path == "/":
                        cur_dir = path
                    else:
                        cur_dir = os.path.normpath(os.path.join(cur_dir, path))
                    if cur_dir not in tree:
                        tree[cur_dir] = []
            else:
                size, name = line.split()
                if size != 'dir':
                    tree[cur_dir].append((name, int(size)))
                else:
                    tree[cur_dir].append(
                        os.path.normpath(os.path.join(cur_dir, name)))
                    
    print(solve(tree))


def calc_size(tree, dir):
    size = 0
    for d in tree[dir]:
        if d in tree:
            size += calc_size(tree, d)
        else:
            size += d[1]
    return size


def solve(tree):
    dir_sizes = {}
    for dir in tree:
        dir_sizes[dir] = calc_size(tree, dir)

    # Part 1
    p1 = sum([s for s in dir_sizes.values() if s < 100_000])

    # Part 2
    disk_size = 70_000_000
    upadte_size = 30_000_000
    needed_space = upadte_size - (disk_size - dir_sizes['/'])
    p2 = sorted(s for s in dir_sizes.values() if s > needed_space)[0]

    return p1, p2


if __name__ == '__main__':
    main()

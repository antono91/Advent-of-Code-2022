with open('input.txt') as f:
    data = [line.strip().split() for line in f]


def solve(data):
    x = 1
    cycle = [1, 1]
    line = ''
    for inst in data:
        if inst[0] == "noop":
            cycle.append(x)
        else:
            cycle.append(x)
            x += int(inst[1])
            cycle.append(x)

    for c in range(241):
        if c % 40 == 0:
            print(line)
            line = ''
        line += u'\u2588' if c % 40 - cycle[c + 1] in {-1, 0, 1} else ' '

    return sum(cycle[i] * i for i in range(20, 241, 40))


print(solve(data))

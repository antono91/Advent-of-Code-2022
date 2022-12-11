with open('input.txt') as f:
    data = f.read().strip()


def solve(data, lm):
    for i in range(len(data) - lm - 1):
        if len(set(data[i:i + lm])) == lm:
            return i + lm


print(solve(data, 4), solve(data, 14))

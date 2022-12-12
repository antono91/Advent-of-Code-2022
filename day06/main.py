def main():
    with open('input.txt') as f:
        data = f.read().strip()
       
    print(solve(data, 4), solve(data, 14))


def solve(data, lm):
    for i in range(len(data) - lm - 1):
        if len(set(data[i:i + lm])) == lm:
            return i + lm


if __name__ == '__main__':
    main()

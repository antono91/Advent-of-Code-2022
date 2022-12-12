def main():
    with open('input.txt') as f:
        data = []
        for line in f:
            r1, r2 = line.strip().split(',')
            r1s, r1e = (int(x) for x in r1.split('-'))
            r2s, r2e = (int(x) for x in r2.split('-'))
            data.append([set(range(r1s, r1e + 1)), set(range(r2s, r2e + 1))])
    
    print(solve(data))


def solve(data):
    count1 = count2 = 0
    for r1, r2 in data:
        overlap = len(r1.intersection(r2))
        if len(r1) == overlap or len(r2) == overlap:
            count1 += 1
        if overlap:
            count2 += 1
    return count1, count2


if __name__ == '__main__':
    main()

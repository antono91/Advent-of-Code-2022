with open('input.txt') as f:
    data = [line.strip() for line in f]


def solve(data):
    s = s2 = 0
    for rucksack in data:
        comp1, comp2 = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
        item = set(comp1).intersection(comp2).pop()
        s += ord(item) - 96 if item.islower() else ord(item) - 38

    for i in range(0, len(data), 3):
        r1, r2, r3 = data[i:i + 3]
        badge = set(r1).intersection(r2, r3).pop()
        s2 += ord(badge) - 96 if badge.islower() else ord(badge) - 38

    return s, s2


print(solve(data))

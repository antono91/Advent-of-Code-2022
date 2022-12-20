import copy
import re


def main():
    with open('input.txt') as f:
        stacks, inst = f.read().split("\n\n")
        inst = [list(map(int, re.findall(r'\d+', line))) for line in inst.split('\n')]

        stacks = [line[1::4] for line in stacks.split('\n')][::-1]
        stacks = {
            int(stacks[0][i]): [s[i] for s in stacks[1:] if s[i] != ' ']
            for i in range(len(stacks[0]))
        }

    print(solve(stacks, inst))


def solve(stacks, inst):
    stacks2 = copy.deepcopy(stacks)

    for c, f, t in inst:
        for _ in range(c):
            stacks[t].append(stacks[f].pop())

        stacks2[t] = stacks2[t] + stacks2[f][-c:]
        del stacks2[f][-c:]

    ans1 = ''.join([s[-1] for s in stacks.values()])
    ans2 = ''.join([s[-1] for s in stacks2.values()])
    return ans1, ans2


if __name__ == '__main__':
    main()

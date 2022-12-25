#!/usr/local/bin/python3
import re


def main():
    data = []
    with open('input.txt') as f:
        for line in f:
            data.append(list(map(int, re.findall(r'\d+', line.strip()))))
    print(solve(data))


def solve(data):
    for id_, ore, clay, obsidian1, obsidian2, geode1, geode2 in data:
        return simulate_blueprint(ore, clay, (obsidian1, obsidian2), (geode1, geode2))


def simulate_blueprint(ore, clay, obsidian, geode):
    robots = dict(ore=1, clay=0, obsidian=0, geode=0)
    minerals = dict(ore=0, clay=0, obsidian=0, geode=0)
    costs = dict(ore=ore, clay=clay, obsidian=obsidian, geode=geode)
    for time in range(1, 25):
        # buy new robots
        new_robots = []

        # collect minerals
        for ore, amount in robots.items():
            minerals[ore] += amount
        print(minerals)
    return robots, minerals, costs


if __name__ == '__main__':
    main()

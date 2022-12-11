with open('input.txt', 'r') as f:
    data = [line.strip().split(' ') for line in f]


def solve(data):
    win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    scores = {'X': 1, 'Y': 2, 'Z': 3}
    final_score = final_score2 = 0

    for opponent, me in data:
        if win[opponent] == me:
            final_score += scores[me] + 6
        elif draw[opponent] == me:
            final_score += scores[me] + 3
        elif lose[opponent] == me:
            final_score += scores[me]

        if me == 'X':
            final_score2 += scores[lose[opponent]]
        elif me == 'Y':
            final_score2 += scores[draw[opponent]] + 3
        elif me == 'Z':
            final_score2 += scores[win[opponent]] + 6

    return final_score, final_score2


print(solve(data))
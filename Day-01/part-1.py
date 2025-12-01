from pathlib import Path


def part1(steps):

    zeros = 0
    dial_pos = 50

    directions = {'L': -1, 'R': 1}

    for line in steps:

        if not line:
            continue

        direction = directions[line[0]]
        distance = int(line[1:]) * direction

        dial_pos = (dial_pos + distance) % 100

        if dial_pos == 0:
            zeros += 1

    print(zeros)


if __name__ == '__main__':

    sample_input = Path('./input')
    problem_input = Path('./input')

    #with open(sample_input) as f:
    with open(problem_input) as f:
        puzzle_input = [l.strip() for l in f.readlines()]
    
    part1(puzzle_input)

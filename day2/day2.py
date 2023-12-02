#!/usr/bin/env python3

def main():
    # red, green, blue
    r, g, b = (12, 13, 14)
    possible = []
    powers = []
    with open("../input", "r") as f:
        for i, line in enumerate(f.readlines()):
            games = line.split(';')
            possibility = []
            maxg = 0
            maxr = 0
            maxb = 0
            for game in games:
                if 'green' in game:
                    green = int(game.split(' green')[0].split(' ')[-1])
                else:
                    green = 0
                if 'red' in game:
                    red = int(game.split(' red')[0].split(' ')[-1])
                else:
                    red = 0
                if 'blue' in game:
                    blue = int(game.split(' blue')[0].split(' ')[-1])
                else:
                    blue = 0
                if red <= r and green <= g and blue <= b:
                    possibility.append(True)
                else:
                    possibility.append(False)
                maxg = max(green, maxg)
                maxb = max(blue, maxb)
                maxr = max(red, maxr)
            if all(possibility):
                possible.append(i+1)
            powers.append(maxg*maxb*maxr)
    print(f"Part 1: {sum(possible)}")
    print(f"Part 2: {sum(powers)}")


if __name__ == '__main__':
    main()

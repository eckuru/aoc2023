#!/usr/bin/env python3
import numpy as np


def main():
    inputlist = []
    specials = []
    with open('../input', 'r') as f:
        for i, line in enumerate(f.readlines()):
            inputlist.append(list(line))
            for c in list(line):
                if not c.isdigit() and c not in ('\n', '.'):
                    specials.append(c)

    specialset = set(specials)
    inputarr = np.array(inputlist)
    parts = []
    gearnumbers = {}
    for i in range(inputarr.shape[0]):
        inNumber = False
        number = ''
        numberidx = []
        for j in range(inputarr.shape[1]):
            if inputarr[i, j].isdigit() and inNumber:
                number += inputarr[i, j]
                continue
            if inputarr[i, j].isdigit() and not inNumber:
                number += inputarr[i, j]
                numberidx.append(j)
                inNumber = True
                continue
            if not inputarr[i, j].isdigit() and inNumber:
                numberidx.append(j-1)
                inNumber = False

                neighbors = inputarr[
                    max(0, i-1):min(inputarr.shape[0], i+2),
                    max(0, numberidx[-2]-1):min(inputarr.shape[1], numberidx[-1]+2)
                ]
                neighborsSet = set(np.unique(neighbors))
                specialNeighbors = neighborsSet.intersection(specialset)
                if len(specialNeighbors) > 0:
                    parts.append(int(number))

                    if '*' in specialNeighbors:
                        gearidxrel = np.where(neighbors == '*')
                        idx = gearidxrel
                        gearidx = (
                            idx[0] + max(0, i - 1),
                            idx[1] + max(0, numberidx[-2] - 1)
                        )
                        assert inputarr[gearidx] == '*'
                        if str(gearidx) not in gearnumbers:
                            gearnumbers[str(gearidx)] = [int(number)]
                        else:
                            gearnumbers[str(gearidx)].append(int(number))

                number = ''
    print(f"p1 {sum(parts)}")

    power = []
    for gear, numbers in gearnumbers.items():
        if len(numbers) == 2:
            power.append(numbers[0] * numbers[1])

    print(f"p2 {sum(power)}")


if __name__ == '__main__':
    main()

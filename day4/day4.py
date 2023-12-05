#!/usr/bin/env python3
import numpy as np


def main():
    nwins = []
    wincard = []
    with open('input', 'r') as f:
        cards = 0
        for line_i in f.readlines():
            line = line_i.replace('  ', ' ')
            lefttmp, right = line.split('|')
            _, left = lefttmp.split(':')
            winning = [int(s) for s in left.lstrip().rstrip().split(' ')]
            winset = set(winning)
            handset = set([int(s) for s in right.lstrip().rstrip().split(' ')])

            wins = handset.intersection(winset)
            if len(wins) > 0:
                nwins.append(len(wins))
                wincard.append(cards)
            cards += 1
    points = [2**(i - 1) for i in nwins]
    print(f"p1 {sum(points)}")

    ncards = np.ones(cards, dtype=int)
    for n, card in zip(nwins, wincard):
        print(ncards)
        copies_now = ncards[card]
        ncards[card+1:card+n+1] += copies_now
    print(f'p2: {sum(ncards)}')


if __name__ == '__main__':
    main()

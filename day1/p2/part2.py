#!/usr/bin/env python3
import re


def main():
    translate_forward = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    translate_backward = {
        "orez": 0,
        "eno": 1,
        "owt": 2,
        "eerht": 3,
        "ruof": 4,
        "evif": 5,
        "xis": 6,
        "neves": 7,
        "thgie": 8,
        "enin": 9,
    }
    forward = re.compile(r'zero|one|two|three|four|five|six|seven|eight|nine|[0-9]')
    backward = re.compile(r'orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|[0-9]')
    numbers = []
    with open("../input", "r") as f:
        for line in f.readlines():
            first = forward.findall(line)[0]
            try:
                firstdigit = int(first)
            except ValueError:
                firstdigit = translate_forward[first]
            second = backward.findall(line[-1::-1])[0]
            try:
                seconddigit = int(second)
            except ValueError:
                seconddigit = translate_backward[second]
            number = firstdigit * 10 + seconddigit
            numbers.append(number)
    print(sum(numbers))


if __name__ == '__main__':
    main()

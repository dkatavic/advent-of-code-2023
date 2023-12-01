import pathlib

word_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

fn = pathlib.Path(__file__).parent / 'input.txt'

with open(fn) as f:
    lines = f.readlines()
    codes = []
    for row in lines:
        if not row:
            continue
        first, last = None, None
        for i, char in enumerate(row):
            if char.isdigit():
                if not first:
                    first = int(char)
                last = int(char)
            for j, word in enumerate(word_numbers):
                lenght = len(word)
                if row[i:i+lenght] == word:
                    numer = j + 1
                    if not first:
                        first = numer
                    last = numer

        codes.append(first * 10 + last)
    print(f'sum: {sum(codes)}')

import pathlib
from dataclasses import dataclass

word_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
fn = pathlib.Path(__file__).parent / 'input.txt'


@dataclass
class Reveal:
    red: int = 0
    green: int = 0
    blue: int = 0

@dataclass
class Row:
    game_id: int
    reveals: list[Reveal]


limit = Reveal(red=12, green=13, blue=14)

def parse_reveal(reveal: str):
    number_str, color = reveal.strip().split(' ')
    return int(number_str), color


def parse_reveals(reveal_sets: str) -> list[Reveal]:
    results = []
    reveal_sets_splitted = reveal_sets.split(';')
    for reveal_set in reveal_sets_splitted:
        reveal_obj = Reveal()
        reveals = reveal_set.split(',')
        for reveal in reveals:
            num, color = parse_reveal(reveal)
            setattr(reveal_obj, color, num)
        results.append(reveal_obj)
    return results
        


def parse_row(row: str) -> Row:
    splitted = row.split(':')
    game_id = int(splitted[0][5:])
    reveals = parse_reveals(splitted[1])
    return Row(game_id, reveals)


def breaching_limit(limit: Reveal, reveal: Reveal) -> bool:
    for field in fields(limit):
        if getattr(limit, field) < getattr(reveal, field):
            return True
    return False


with open(fn) as f:
    lines = f.readlines()
    game_sum = 0
    for row in lines:
        if not row:
            continue
        parsed_row = parse_row(row)
        for reveal in parsed_row.reveals:
            if breaching_limit(limit, reveal):
                game_sum += parsed_row.game_id
                break
    print(f'game_sum: {game_sum} ')

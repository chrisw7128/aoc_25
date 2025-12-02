import re
from dataclasses import dataclass

def get_data():
    turns = []
    with open("day_01_input.txt", "r") as f:
        data = [line.strip() for line in f]

    @dataclass
    class Turn:
        dir: str
        amount: int

    for item in data:
        m = re.match(r"(.)?(.*)", item)
        dir, amount = m.groups()
        turns.append(Turn(dir=dir, amount=int(amount)))

    return turns

data = get_data()

def get_zeros_and_next_position(cur, turn):
    zeros = 0
    if turn.dir=='R':
        for movement in range(turn.amount):
            if cur == 99:
                cur = 0
            else:
                cur += 1
            if cur == 0:
                zeros += 1
    elif turn.dir=='L':
        for movement in range(turn.amount):
            if cur == 0:
                cur = 99
            else:
                cur -= 1
            if cur == 0:
                zeros += 1
    return zeros, cur

def count_zeros(data):
    count_zeros = 0
    cur = 50

    for turn in data:
        prev_zeros, cur = get_zeros_and_next_position(cur, turn)
        count_zeros += prev_zeros

    return count_zeros

total = count_zeros(data)
print(f'Total zeros = {total}')

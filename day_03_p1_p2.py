from dataclasses import dataclass, field
from pprint import pprint

with open("day_03_input.txt", "r") as f:
    data = [line.strip() for line in f]
    print(type(data))
    print(data[0])
    print(type(data[0]))

@dataclass
class Battery:
    highest: int = 0
    highest_after_split: int = 0
    bank: str = '0'

def identify_highest_num(data):
    all_batteries = []
    for nums in data:
        highest = 0
        for num in nums[:-1]:
            if int(num) > highest:
                highest = int(num)
        all_batteries.append(Battery(bank=nums, highest=highest))

    return all_batteries

all_batteries = identify_highest_num(data)

def split_bank_by_highest_num(all_batteries):
    total = 0
    for battery in all_batteries:
        for index, num in enumerate(battery.bank):
            if int(num) == battery.highest:
                battery_split = battery.bank[(index+1):]
                # print(f'battery split type: {type(battery_split)}')
                # print(f'battery_split: {battery_split}')
                break
        highest_after_split = 0
        for num in battery_split:
            # print(f'num: {num}')
            if int(num) > highest_after_split:
                highest_after_split = int(num)
                # print(f'highest after split: {highest_after_split}')
        battery.highest_after_split = highest_after_split
        total += int(str(battery.highest)+str(highest_after_split))
        print(f'total after {index+1} rounds: {total}')

    return total

total = split_bank_by_highest_num(all_batteries)
print(f'p1 total: {total}')

# for battery_num, battery in enumerate(all_batteries):
#     print(f'Battery {battery_num} highest: {battery.highest}')
#     print(f'Battery {battery_num} highest after split: {battery.highest_after_split}')

# 3002 is too low
# 17321 is correct

###### Part 2 ######

@dataclass
class p2_Battery:
    highest_12_nums: int = 0
    count_of_each_num: dict = field(default_factory=dict)
    bank: str = '0'
    new_seq: str = ''

def identify_highest_12_nums(data):
    all_batteries = []
    for nums in data:
        count_of_each_num = {}
        nums_copy=sorted(nums, reverse=True)[:12]
        for num in nums_copy:
            count_of_each_num[num] = count_of_each_num.get(num, 0) + 1
        all_batteries.append(p2_Battery(bank=nums, count_of_each_num=count_of_each_num))

    return all_batteries

p2_all_batteries = identify_highest_12_nums(data)

pprint(p2_all_batteries)

def get_new_sequence(p2_all_batteries):
    for battery in p2_all_batteries:
        new_seq = ''
        for num in battery.bank:
            if num in battery.count_of_each_num:
                battery.count_of_each_num[num] -= 1
                if battery.count_of_each_num[num] == 0:
                    del battery.count_of_each_num[num]
                new_seq += str(num)
                print(f'new seq: {new_seq}')
        battery.new_seq = new_seq
        print(battery.new_seq)

get_new_sequence(p2_all_batteries)

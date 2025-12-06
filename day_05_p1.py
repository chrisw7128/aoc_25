from dataclasses import dataclass

with open("day_05_input.txt", "r") as f:
    first_section, second_section = f.read().split("\n\n", 1)
    fresh_ingredients = first_section.splitlines()
    available_ingredients = second_section.splitlines()

@dataclass
class Ranges:
    start: int
    end: int

def construct_fresh_ranges(fresh_ingredients):
    ranges = []
    for range in fresh_ingredients:
        start = int(range.split('-')[0])
        end = int(range.split('-')[1])
        ranges.append(Ranges(start=start, end=end))

    return ranges

fresh_ingredients_ranges = construct_fresh_ranges(fresh_ingredients)

def count_num_of_available_fresh_ingredients(available_ingredients, fresh_ingredients_ranges):
    fresh_total = 0
    for ingredient in available_ingredients:
        for range in fresh_ingredients_ranges:
            if int(ingredient) >= range.start and int(ingredient) <= range.end:
                fresh_total += 1
                break
    
    return fresh_total

fresh_total = count_num_of_available_fresh_ingredients(available_ingredients, fresh_ingredients_ranges)
print(f'p1 fresh total: {fresh_total}')

# p1 answer is 701

# ######## Part 2 ########

# from dataclasses import dataclass

# first_section = 0

# with open("day_05_sample_p2.txt", "r") as f:
#     try:
#         first_section, second_section = f.read().split("\n\n", 1)
#     except ValueError:
#         with open("day_05_sample_p2.txt", "r") as f:
#             ranges = f.readlines()

#     if first_section:
#         ranges = first_section.splitlines()


#     print(len(ranges))
#     print(type(ranges))
#     print(ranges[1])
#     print(type(ranges[0]))
#     print(repr(ranges[1]))


# @dataclass
# class Ranges:
#     start: int
#     end: int

# def construct_fresh_ranges(fresh_ingredients):
#     ranges = []
#     for range in fresh_ingredients:
#         start = int(range.split('-')[0])
#         end = int(range.split('-')[1])
#         ranges.append(Ranges(start=start, end=end))

#     return ranges

# old_ranges = construct_fresh_ranges(ranges)

# def combine_ranges(old_ranges):
#     new_range_list = []
#     for new_range in new_ranges:
#         for old_range in old_ranges:
#             # RIP
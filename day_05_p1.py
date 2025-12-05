from dataclasses import dataclass

with open("day_05_input.txt", "r") as f:
    first_section, second_section = f.read().split("\n\n", 1)

    fresh_ingredients = first_section.splitlines()
    available_ingredients = second_section.splitlines()

    print(len(fresh_ingredients))
    print(len(available_ingredients))
    print(type(fresh_ingredients))
    print(type(available_ingredients))
    print(fresh_ingredients[0])
    print(available_ingredients[0])
    print(type(fresh_ingredients[0]))
    print(type(available_ingredients[0]))


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

print(type(fresh_ingredients_ranges))
print(type(fresh_ingredients_ranges[0]))
print(fresh_ingredients_ranges[0])
print(type(fresh_ingredients_ranges[0].start))
print(fresh_ingredients_ranges[0].start)
print(type(available_ingredients[0]))

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

######## Part 2 ########


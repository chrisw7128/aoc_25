from dataclasses import dataclass
from pprint import pprint

with open("day_04_input.txt", "r") as f:
    data = [line.strip() for line in f]

def count_adjacent_connections(data):
    total = 0
    for index, row in enumerate(data):
        for i, char in enumerate(row):
            if char == '@':
                connections = 0
                # Use slicing instead of indexing because slicing avoids an IndexError
                prev_row = data[index- 1] if index > 0 else ''
                next_row = data[index + 1] if index + 1 < len(data) else ''

                left = row[i-1:i]
                if left == '@':
                    connections += 1           
                right = row[i+1:i+2]
                if right == '@':
                    connections += 1        

                if prev_row:
                    above_left = prev_row[i-1:i]
                    if above_left == '@':
                        connections += 1
                    above = prev_row[i:i+1]
                    if above == '@':
                        connections += 1
                    above_right = prev_row[i+1:i+2]
                    if above_right == '@':
                        connections += 1

                if next_row:           
                    below_left = next_row[i-1:i]
                    if below_left == '@':
                        connections += 1
                    below = next_row[i:i+1]
                    if below == '@':
                        connections += 1                
                    below_right = next_row[i+1:i+2]
                    if below_right == '@':
                        connections += 1               

                if connections < 4:
                    total += 1

    return total

total = count_adjacent_connections(data)
print(f'P1 total: {total}')

# P1 answer 1502

######## Part 2 ########

# def p2_count_adjacent_connections(data):
#     total = 0
#     initial_state = data
#     locations_to_remove = []
#     for index, row in enumerate(data):
#         for i, char in enumerate(row):
#             if char == '@':
#                 connections = 0
#                 # Use slicing instead of indexing because slicing avoids an IndexError
#                 prev_row = data[index- 1] if index > 0 else ''
#                 next_row = data[index + 1] if index + 1 < len(data) else ''

#                 left = row[i-1:i]
#                 if left == '@':
#                     connections += 1           
#                 right = row[i+1:i+2]
#                 if right == '@':
#                     connections += 1        

#                 if prev_row:
#                     above_left = prev_row[i-1:i]
#                     if above_left == '@':
#                         connections += 1
#                     above = prev_row[i:i+1]
#                     if above == '@':
#                         connections += 1
#                     above_right = prev_row[i+1:i+2]
#                     if above_right == '@':
#                         connections += 1
                
#                 if next_row:           
#                     below_left = next_row[i-1:i]
#                     if below_left == '@':
#                         connections += 1
#                     below = next_row[i:i+1]
#                     if below == '@':
#                         connections += 1                
#                     below_right = next_row[i+1:i+2]
#                     if below_right == '@':
#                         connections += 1               

#                 if connections < 4:
#                     locations_to_remove.append([index, i])
#                     total += 1

#     new_state = initial_state.copy()

#     print(f'initial state type: {type(initial_state)}')
#     print(f'new state type: {type(new_state)}')
#     print(f'len of locations to remove: {len(locations_to_remove)}')

#     for index, row in enumerate(new_state):
#         for i, char in enumerate(row):
#             # print(f'initial_state[row][char]: {initial_state[index][i]}')
#             if initial_state[index][i] in locations_to_remove:
#                 initial_state[index][i] == 'x'

#     return total, initial_state, new_state


# total, initial_state, new_state = p2_count_adjacent_connections(data)

# p2_total = 0
# while True:
#     total, initial_state, new_state = p2_count_adjacent_connections(data)
#     p2_total += total
#     if initial_state == new_state:
#         break


# print(f'P2 total: {p2_total}')


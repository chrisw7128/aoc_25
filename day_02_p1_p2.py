from dataclasses import dataclass

def get_data():
    with open("day_02_input.txt", "r") as f:
        data = f.read().split(",")

    @dataclass
    class NumRange:
        start: int
        end: int

    list_of_ranges = []
    for i in data:
        left, right = i.split("-")
        list_of_ranges.append(NumRange(start=int(left), end=int(right)))
    
    list_of_strs = []
    for i in list_of_ranges:
        for num in range(i.start, (i.end + 1)):
            list_of_strs.append(str(num))

    return list_of_strs

list_of_strs = get_data()

def check_invalid_strs(list_of_strs):
    invalid_strs = []
    for i in list_of_strs:
        if len(str(i)) % 2 != 0:
            continue
        else:
            mid = len(i) // 2
            first_half, second_half = i[:mid], i[mid:]
            if first_half == second_half:
                invalid_strs.append(i)

    return invalid_strs

list_of_invalid_strs = check_invalid_strs(list_of_strs)

def get_total(list_of_invalid_strs):
    total = 0
    for i in list_of_invalid_strs:
        total += int(i)

    return total

total = get_total(list_of_invalid_strs)

print(f'Part 1 total invalid strs: {total}')

### Part 2 ###
    # note - I checked - max len str is 10 digits
    # possible repeating combos: 
    # - 1 digit 2-10 times
    # - 2 digits 2-5 times
    # - 3 digits 2-3 times
    # - 4 digits 2 times
    # - 5 digits 2 times
    # that's all the possibilities
    
def filter_strs_to_two_or_more_digits(list_of_strs):
    two_or_more_digit_strs = []
    for item in list_of_strs:
        if len(item) >= 2:
            two_or_more_digit_strs.append(item)

    return two_or_more_digit_strs

two_or_more_digit_strs = filter_strs_to_two_or_more_digits(list_of_strs)


def filter_strs_to_three_or_more_digits(list_of_strs):
    three_or_more_digit_strs = []
    for item in list_of_strs:
        if len(item) >= 3:
            three_or_more_digit_strs.append(item)

    return three_or_more_digit_strs

three_or_more_digit_strs = filter_strs_to_three_or_more_digits(list_of_strs)


def check_single_repeating(two_or_more_digit_strs):
    invalid_ids = 0
    single_repeating_strs = []

    split_filtered_str_list = []
    for str in two_or_more_digit_strs:
        str_segments = [str[i:i+1] for i in range(0, len(str))]
        split_filtered_str_list.append(str_segments)

    invalid_segmented_strs = []
    for segmented_str in split_filtered_str_list:
        first = segmented_str[0]
        flag = 0
        for i in range(len(segmented_str)):
            if segmented_str[i] != first:
                flag = 1
                break
            else:
                continue
        if flag == 0:
            invalid_segmented_strs.append(segmented_str)

    joined_list = []
    for segmented_str in invalid_segmented_strs:
        joined = ''.join(segmented_str)
        joined_list.append(int(joined))

    return joined_list


def check_double_repeating(three_or_more_digit_strs):
    invalid_ids = 0
    double_repeating_strs = []
    filtered_str_list = []
    for str in three_or_more_digit_strs:
        if len(str) % 2 == 0 and len(str) != 2:
            filtered_str_list.append(str)

    split_filtered_str_list = []
    for str in filtered_str_list:
        str_segments = [str[i:i+2] for i in range(0, len(str), 2)]
        split_filtered_str_list.append(str_segments)

    invalid_segmented_strs = []
    for segmented_str in split_filtered_str_list:
        first = segmented_str[0]
        flag = 0
        for i in range(len(segmented_str)):
            if segmented_str[i] != first:
                flag = 1
                break
            else:
                continue
        if flag == 0:
            invalid_segmented_strs.append(segmented_str)

    joined_list = []
    for segmented_str in invalid_segmented_strs:
        joined = ''.join(segmented_str)
        joined_list.append(int(joined))

    return joined_list


def check_triple_repeating(three_or_more_digit_strs):
    invalid_ids = 0
    triple_repeating_strs = []
    filtered_str_list = []
    for str in three_or_more_digit_strs:
        if len(str) % 3 == 0 and len(str) != 3:
            filtered_str_list.append(str)

    split_filtered_str_list = []
    for str in filtered_str_list:
        str_segments = [str[i:i+3] for i in range(0, len(str), 3)]
        split_filtered_str_list.append(str_segments)   

    invalid_segmented_strs = []
    for segmented_str in split_filtered_str_list:
        first = segmented_str[0]
        flag = 0
        for i in range(len(segmented_str)):
            if segmented_str[i] != first:
                flag = 1
                break
            else:
                continue
        if flag == 0:
            invalid_segmented_strs.append(segmented_str)

    joined_list = []
    for segmented_str in invalid_segmented_strs:
        joined = ''.join(segmented_str)
        joined_list.append(int(joined))

    return joined_list

def check_quadruple_repeating(three_or_more_digit_strs):
    invalid_ids = 0
    quadruple_repeating_strs = []
    filtered_str_list = []
    for str in three_or_more_digit_strs:
        if len(str) % 8 == 0 and len(str) != 4:
            filtered_str_list.append(str)

    split_filtered_str_list = []
    for str in filtered_str_list:
        str_segments = [str[i:i+4] for i in range(0, len(str), 4)]
        split_filtered_str_list.append(str_segments)   

    invalid_segmented_strs = []
    for segmented_str in split_filtered_str_list:
        first = segmented_str[0]
        flag = 0
        for i in range(len(segmented_str)):
            if segmented_str[i] != first:
                flag = 1
                break
            else:
                continue
        if flag == 0:
            invalid_segmented_strs.append(segmented_str)

    joined_list = []
    for segmented_str in invalid_segmented_strs:
        joined = ''.join(segmented_str)
        joined_list.append(int(joined))

    return joined_list


def check_quintuple_repeating(three_or_more_digit_strs):
    invalid_ids = 0
    quadruple_repeating_strs = []
    filtered_str_list = []
    for str in three_or_more_digit_strs:
        if len(str) % 5 == 0 and len(str) != 5:
            filtered_str_list.append(str)

    split_filtered_str_list = []
    for str in filtered_str_list:
        str_segments = [str[i:i+5] for i in range(0, len(str), 5)]
        split_filtered_str_list.append(str_segments)   

    invalid_segmented_strs = []
    for segmented_str in split_filtered_str_list:
        first = segmented_str[0]
        flag = 0
        for i in range(len(segmented_str)):
            if segmented_str[i] != first:
                flag = 1
                break
            else:
                continue
        if flag == 0:
            invalid_segmented_strs.append(segmented_str)

    joined_list = []
    for segmented_str in invalid_segmented_strs:
        joined = ''.join(segmented_str)
        joined_list.append(int(joined))

    return joined_list


count_one = check_single_repeating(two_or_more_digit_strs)
count_two = check_double_repeating(three_or_more_digit_strs)
count_three = check_triple_repeating(three_or_more_digit_strs)
count_four = check_quadruple_repeating(three_or_more_digit_strs)
count_five = check_quintuple_repeating(three_or_more_digit_strs)

def combine_p2_all(l1, l2, l3, l4, l5):
    total_list = []
    total_list.extend(l1)
    total_list.extend(l2)
    total_list.extend(l3)
    total_list.extend(l4)
    total_list.extend(l5)

    int_list = []
    for num in total_list:
        num = int(num)
        int_list.append(num)

    deduped_int_list = sorted(list(set(int_list)))

    total = 0
    for num in deduped_int_list:
        total += num

    print(f'Part 2 total invalid strs: {total}')

    len_5 = [i for i in deduped_int_list if len(str(i)) == 5]


combine_p2_all(count_one, count_two, count_three, count_four, count_five)

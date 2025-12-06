with open("day_06_input.txt", "r") as f:
    input = f.read().splitlines()
    data = []
    for line in input:
        elements = line.split()
        parsed = []
        for element in elements:
            try:
                parsed.append(int(element))
            except ValueError:
                parsed.append(element)
        data.append(parsed)

print(data)

def transpose_data(data):
    transposed_all = []
    for i in range(len(data[0])):
        transposed_instance = []
        for row in data:
            transposed_instance.append(row[i])
        transposed_all.append(transposed_instance)

    return transposed_all

transposed_all = transpose_data(data)

print(transposed_all)

def perform_calculations(transposed_all):
    answers = []
    for problem in transposed_all:
        operator = problem[-1]
        answer = problem[0]
        for num in problem[1:-1]:
            if operator == '+':
                answer += num
            elif operator == '*':
                answer *= num
        answers.append(answer)

    return answers

answers = perform_calculations(transposed_all)

print(answers)

def get_total(answers):
    total = 0
    for answer in answers:
        total += answer
    
    return total

total = get_total(answers)

print(f'P1 total: {total}')

# p1 answer 4309240495780

######## P2 ########


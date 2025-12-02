cur = 5
zeros = 0
for movement in range(100):
    print(f'initial state: cur: {cur}, zeros: {zeros}')
    if cur == 9:
        zeros += 1
        cur -= 9
        print(f'moved right once to position {cur}')
        print(f'updated state: cur: {cur}, zeros: {zeros}')
    else:
        cur += 1
        print(f'moved right once to position {cur}')
        print(f'updated state: cur: {cur}, zeros: {zeros}')

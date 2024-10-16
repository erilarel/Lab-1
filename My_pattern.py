BLUE = '\u001b[44m'
END = '\u001b[0m'


def draw(m, k):
    for j in range(k):
        for i in range(4):
            if i == 0: print(f'{BLUE}{" " * 2}{END}{" " * 12}{END}' * m)
            if i == 1: print(f'{" " * 2}{BLUE}{" " * 2}{END}{" " * 8}{BLUE}{" " * 2}{END}' * m)
            if i == 2: print(f'{" " * 4}{BLUE}{" " * 2}{END}{" " * 4}{BLUE}{" " * 2}{END}{" " * 2}{END}' * m)
            if i == 3: print(f'{" " * 6}{BLUE}{" " * (2 * 2)}{END}{" " * 4}{END}' * m)

draw(20, 6)
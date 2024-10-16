RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

for i in range(7):
    if i == 0 or i == 6:
        print(f'{RED}{"  " * 16}{END}')
    elif i == 1 or i == 5:
        print(f'{WHITE}{"  " * 16}{END}')
    else: print(f'{BLUE}{"  " * 16}{END}')
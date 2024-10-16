GREEN = '\u001b[42m'
END = '\u001b[0m'

def draw(step):
    print(f'{" " * int(step*50)}{GREEN}{" " * 2}{END}')

def giperbola():
    h = 50
    step = 0.2
    for i in range(h, 0, -1):
        draw(step)
        step = 10/i

giperbola()

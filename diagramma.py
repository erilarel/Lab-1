YELLOW = '\u001b[43m'
PINK = '\u001b[45m'
END = '\u001b[0m'

f = open('sequence.txt')
numbers = [float(x) for x in f if float(x) >= 0]
bol_5 =[]
men_5 = []
for i in range(len(numbers)):
    if numbers[i] > 5: bol_5.append(numbers[i])
    else: men_5.append(numbers[i])
proc_bol_5 = len(bol_5) / len(numbers)
proc_men_5 = len(men_5) / len(numbers)

print(f'\033[33m{proc_bol_5:.1%}{END}{" составляют числа больше пяти"}')
print(f'\033[35m{proc_men_5:.1%}{END}{" составляют числа меньше пяти"}')
print(f'{YELLOW}{" " * (round(proc_bol_5*100))}{END}\n{PINK}{" " * (round(proc_men_5*100))}{END}')


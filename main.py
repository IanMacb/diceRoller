import random


# implement keep n highest/lowest
# implement explode
# implement adding different die types

def die(c, n):
    if c > 0:
        return random.randint(1, n) + die(c - 1, n)
    return 0


def roll(c):
    for i in c:
        term = i.split('d')
        if not term[0].isnumeric():
            term[0] = 1
        print(i + ':', die(int(term[0]), int(term[1])))

def main():
    cmd = input('>').split()
    if cmd[0] == '/r':
        print(roll(cmd[1:]))
    elif cmd[0].lower() == 'exit' or 'x':
        exit()
    main()

main()
import random

#TODO
# keep n highest/lowest
# explode
# -adding different die types
# reroll
# save favorite rolls as "" to txt

LAST_ROLL =[]

def die(c, n):
    if c > 0:
        return random.randint(1, n) + die(c - 1, n)
    return 0


def roll(c):
    for term in c:
        #print('term:', term)
        dice = term.split('+')
        total = 0
        result = []
        for i in dice:
            #print(i)
            if i == '':
                break
            d = i.split('d')
            if not d[0].isnumeric():
                d[0] = 1
            result.append(die(int(d[0]), int(d[1])))
            total += result[-1]
        print(term + ':', result, total)


def main():
    cmd = input('>').split()
    if cmd[0] == '/r' or '/roll':
        print(roll(cmd[1:]))
    elif cmd[0].lower() == '/x' or '/exit' or 'x':
        LAST_ROLL = cmd
        exit()
    elif cmd[0].lower() == '/rr' or '/reroll':
        print(roll(LAST_ROLL[1:]))
    LAST_ROLL = cmd
    main()


main()

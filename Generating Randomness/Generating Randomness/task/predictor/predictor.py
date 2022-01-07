import random


def cou_tem(string, substring):
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count


def statistic(stat):
    for x in ["000", "001", "010", "011", "100", "101", "110", "111"]:
        a = x + "0"
        b = x + "1"
        if cou_tem(fin_str, a) > cou_tem(fin_str, b):
            stat[x] = 0
        elif cou_tem(fin_str, a) < cou_tem(fin_str, b):
            stat[x] = 1
        else:
            stat[x] = random.choice('01')
    return stat


final = []
stat = dict()
bal = 1000
print("Please give AI some data to learn...\nThe current data length is 0, 100 symbols left")
while len(final) < 100:
    print("Print a random string containing 0 or 1:\n")
    number = input()
    for item in number:
        if item == "0" or item == "1":
            final.append(item)
    if len(final) < 100:
        print("Current data length is " + str(len(final)) + ", " + str(100 - len(final)) + " symbols left")
fin_str = "".join(final)

print("\nFinal data string:")
print(fin_str)
print("\nYou have $1000. Every time the system successfully predicts your next press, you lose $1.")
print('Otherwise, you earn $1. Print "enough" to leave the game.' + "Let's go!\n")

while True:
    print("\nPrint a random string containing 0 or 1:")
    str1 = input()
    if str1 == "enough":
        print("Game over!")
        break
    else:
        ok = 0
        for i in str1:
            if i == "0" or i == "1":
                ok += 1
        if ok == len(str1):
            statistic(stat)
            str2 = 3 * random.choice('01')
            s = 0
            total = len(str1) - 3
            while s < total:
                str2 += str(stat[str1[s:(s + 3)]])
                s += 1

            print("prediction:\n" + str2)
            cou = 0
            for x in range(3, len(str1)):
                if str1[x] == str2[x]:
                    cou += 1
                    bal -= 1
                else:
                    bal += 1
            print("\nComputer guessed right", cou, "out of", total, "symbols (" + str(round(100 * cou / total, 2)), "%)")
            print("Your balance is now $" + str(bal))
            fin_str += str1


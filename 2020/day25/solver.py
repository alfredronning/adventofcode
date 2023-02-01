SUB_NR = 7
REM = 20201227

if __name__ == "__main__":
    door_pub, card_pub = [int(i) for i in open("input.txt").read().strip().split("\n")]
    card_mod = 7
    print(card_pub, door_pub)
    loop = 1
    while True:
        card_mod = card_mod*SUB_NR%REM
        loop += 1
        if card_mod == card_pub:
            break
    print(loop)
    print(pow(door_pub, loop, REM))


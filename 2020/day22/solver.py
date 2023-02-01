if __name__ == "__main__":
    p1, p2 = open("input.txt").read().strip().split("\n\n")
    p1 = [int(i) for i in p1.split("\n")[1:]]
    p2 = [int(i) for i in p2.split("\n")[1:]]
    while p1 and p2:
        p1_card, p2_card = p1.pop(0), p2.pop(0)
        if p1_card > p2_card:
            p1 += [p1_card, p2_card]
        else:
            p2 += [p2_card, p1_card]
    if p1:
        res = sum((i+1)*card for i, card in enumerate(p1[::-1]))
    else:
        res = sum((i+1)*card for i, card in enumerate(p2[::-1]))
    print(res)


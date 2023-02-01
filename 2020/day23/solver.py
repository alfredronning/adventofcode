if __name__ == "__main__":
    cups = [int(i) for i in open("input.txt").read().strip()]
    for move in range(100):
        cup_id = move % len(cups)
        current_cup = cups[cup_id]
        three_other = (cups*2)[cup_id+1: cup_id+4]
        destination = (current_cup-2) % (len(cups)) + 1
        while destination in three_other:
            destination = (destination - 2) % (len(cups)) + 1
        destination_id = cups.index(destination)
        cups = [cup for cup in cups if cup not in three_other]
        destination_id_after = cups.index(destination)
        cups = cups[:destination_id_after+1]+three_other+cups[destination_id_after+1:]
        while cups[cup_id] != current_cup:
            cups = [cups[-1]] + cups[:-1]
    after_1 = (cups*2)[cups.index(1)+1:cups.index(1)+len(cups)]
    print("".join(str(i) for i in after_1))


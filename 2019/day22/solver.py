def shuffle(cards, technique):
    if technique == "deal into new stack":
        return cards[::-1]
    n = int(technique.split()[-1])
    if "cut" in technique:
        return cards[n:] + cards[:n]
    new_cards = [0]*len(cards)
    for i, c in enumerate(cards):
        new_cards[i*n%len(cards)] = c
    return new_cards

if __name__ == "__main__":
    techniques = open("input.txt").read().strip().split("\n")
    cards = [i for i in range(10007)]
    for technique in techniques:
        cards = shuffle(cards, technique)
    print(cards.index(2019))


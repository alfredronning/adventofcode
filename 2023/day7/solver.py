CARDMAP = {"2": "02", "3": "03", "4": "04", "5": "05", "6": "06", "7": "07", "8": "08", "9": "09", "T": "10", "J": "11", "Q": "12", "K": "13", "A": "14"}

def get_hand(cards):
    counts = [cards.count(card) for card in set(cards) if cards.count(card) > 1]
    if len(counts) == 2:
        return 5 if max(counts) == 3 else 3
    return counts[0]*2-2 if counts else 0

def get_strength(cards):
    strength = str(get_hand(cards))
    for card in cards:
        strength += CARDMAP[card]
    return strength

if __name__ == "__main__":
    cards_bets = [i.split() for i in open("input.txt").read().strip().split("\n")]
    strength_bets = sorted([(get_strength(cards), int(bet)) for cards, bet in cards_bets])
    res = 0
    for i in range(len(strength_bets)):
        res += strength_bets[i][1]*(i+1)
    print(res)


def play_out(id, cards, cache):
    if id in cache:
        return cache[id]
    winning, my = cards[id].split(" | ")
    winning = set(int(i) for i in winning.split(": ")[1].split())
    my = [int(i) for i in my.split()]
    right = sum(n in winning for n in my)
    if right == 0:
        cache[id] = 1
    else:
        res = 1
        for other_id in range(id+1, id+right+1):
            res += play_out(other_id, cards, cache)
        cache[id] = res
    return cache[id]

if __name__ == "__main__":
    cards = open("input.txt").read().strip().split("\n")
    res = 0
    cache = dict()
    for id in range(len(cards)):
        res += play_out(id, cards, cache)
    print(res)


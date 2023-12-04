def get_points(winning, my):
    right = sum(n in winning for n in my)
    if right == 0:
        return 0
    return 2**(right-1)

if __name__ == "__main__":
    cards = open("input.txt").read().strip().split("\n")
    points = 0
    for card in cards:
        winning, my = card.split(" | ")
        winning = set(int(i) for i in winning.split(": ")[1].split())
        my = [int(i) for i in my.split()]
        points += get_points(winning, my)
    print(points)


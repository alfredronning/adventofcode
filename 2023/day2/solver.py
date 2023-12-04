def possible(game, m):
    moves = game.split("; ")
    for s in moves:
        items = s.split(", ")
        for item in items:
            count, color = item.split()
            if int(count) > m[color]:
                return False
    return True

if __name__ == "__main__":
    games = open("input.txt").read().strip().split("\n")
    m = {"red": 12, "green": 13, "blue": 14}
    res = 0
    for row in games:
        id, game = row.split(": ")
        if possible(game, m):
            res += int(id.split()[1])
    print(res)


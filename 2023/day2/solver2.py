def cubepower(game):
    m = {"red": 0, "green": 0, "blue": 0}
    moves = game.split("; ")
    for s in moves:
        items = s.split(", ")
        for item in items:
            count, color = item.split()
            m[color] = max(m[color], int(count))
    return m["red"]*m["green"]*m["blue"]

if __name__ == "__main__":
    games = open("input.txt").read().strip().split("\n")
    res = 0
    for row in games:
        game = row.split(": ")[1]
        res += cubepower(game)
    print(res)


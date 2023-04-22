WEP_SHOP = {8: 4, 10: 5, 25: 6, 40: 7, 74: 8}
ARMOR_SHOP = {13: 1, 31: 2, 53: 3, 75: 4, 102: 5}
RING_SHOP = {20: [0, 1], 25: [1, 0], 40: [0, 2], 50: [2, 0], 80: [0, 3], 100: [3, 0]}

def wins(stats, boss_stats):
    player_turn = False
    players_stats = [boss_stats, stats]
    while True:
        players_stats[player_turn][0] -= max(1, players_stats[not player_turn][1] - players_stats[player_turn][2])
        if players_stats[player_turn][0] <= 0:
            return not player_turn
        player_turn = not player_turn

def calc_stats(weps, armor, rings):
    player = [100, 0, 0]
    for i in range(len(weps)):
        player[1] += WEP_SHOP[weps[i]]
    for i in range(len(armor)):
        player[2] += ARMOR_SHOP[armor[i]]
    for i in range(len(rings)):
        player[1] += RING_SHOP[rings[i]][0]
        player[2] += RING_SHOP[rings[i]][1]
    return player

def search_solution_space(weps, armor, rings, piece, price, boss, cache):
    if price >= cache["best"] or piece > 3:
        return float("inf")
    if piece > 0:
        player = calc_stats(weps, armor, rings)
        if wins(player, boss[:]):
            cache["best"] = price
            cache["best_setup"] = [weps, armor, rings]
            return price
    best = float("inf")
    if piece == 0:
        for wep in WEP_SHOP.keys():
            current = search_solution_space([wep], armor, rings, piece+1, price+wep, boss, cache)
            best = min(best, current)
    elif piece == 1:
        best = search_solution_space(weps, [], rings, piece+1, price, boss, cache)
        for arm in ARMOR_SHOP.keys():
            current = search_solution_space(weps, [arm], rings, piece+1, price+arm, boss, cache)
            best = min(best, current)
    else:
        for ring in [ring for ring in RING_SHOP.keys() if ring not in rings]:
            current = search_solution_space(weps, armor, rings+[ring], piece+1, price+ring, boss, cache)
            best = min(best, current)
    return best

if __name__ == "__main__":
    boss = open("input.txt").read().strip().split("\n")
    boss_stats = [int(l.split(": ")[1]) for l in boss]


    cache = {"best": float("inf"), "best_setup": [[], [], []]}
    best = search_solution_space([], [], [], 0, 0, boss_stats, cache)
    print(best)
    print(cache)


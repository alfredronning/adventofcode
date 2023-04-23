MANA = {0: 53, 1: 73, 2: 113, 3: 173, 4: 229}
SHIELD_BLOCK = 7
RECHARGE_MANA = 101
POISON_TICK = 3

def search_solution_space(shields, poisons, recharges, boss, player, player_turn, mana_spent, cache, path):
    if mana_spent >= cache["best"]:
        return float("inf")
    if player[1] < 0:
        return float("inf")

    if not player_turn:
        new_player_hp = player[0] - max(1, boss[1] - (SHIELD_BLOCK if len(shields) else 0)) - 1
        new_boss_hp = boss[0] - len(poisons) * POISON_TICK
        if new_boss_hp <= 0:
            cache["best"] = mana_spent
            cache["best_path"] = path
            return mana_spent
        if new_player_hp <= 0:
            return float("inf")
        new_player_mana = player[1] + len(recharges) * RECHARGE_MANA
        shields = [i - 1 for i in shields if i > 1]
        poisons = [i - 1 for i in poisons if i > 1]
        recharges = [i - 1 for i in recharges if i > 1]
        return search_solution_space(shields, poisons, recharges, (new_boss_hp, boss[1]), (new_player_hp, new_player_mana), True, mana_spent, cache, path)
    else:
        new_boss_hp = boss[0] - len(poisons) * POISON_TICK
        new_player_hp = player[0] - 1
        if new_player_hp == 0:
            return float("inf")
        if new_boss_hp <= 0:
            cache["best"] = mana_spent
            cache["best_path"] = path
            return mana_spent
        if new_boss_hp <= 4 and player[1] >= MANA[0]:
            if cache["best"] <= mana_spent + MANA[0]:
                return float("inf")
            cache["best"] = mana_spent + MANA[0]
            cache["best_path"] = path + [0]
            return cache["best"]
        new_player_mana = player[1] + len(recharges) * RECHARGE_MANA
        shields = [i - 1 for i in shields if i > 1]
        poisons = [i - 1 for i in poisons if i > 1]
        recharges = [i - 1 for i in recharges if i > 1]

        best = float("inf")
        # check shield path
        if not len(shields) and new_player_mana >= MANA[2]:
            shield_path = search_solution_space(shields + [6], poisons, recharges, (new_boss_hp, boss[1]), (new_player_hp, new_player_mana-MANA[2]), False, mana_spent + MANA[2], cache, path+[2])
            best = min(best, shield_path)
        # check poison path
        if not len(poisons) and new_player_mana >= MANA[3]:
            poison_path = search_solution_space(shields, poisons + [6], recharges, (new_boss_hp, boss[1]), (new_player_hp, new_player_mana-MANA[3]), False, mana_spent + MANA[3], cache, path+[3])
            best = min(best, poison_path)
        # check nuke path
        if new_player_mana >= MANA[0]:
            nuke_path = search_solution_space(shields, poisons, recharges, (new_boss_hp - 4, boss[1]), (new_player_hp, new_player_mana-MANA[0]), False, mana_spent + MANA[0], cache, path+[0])
            best = min(best, nuke_path)
        # check drain path
        if new_player_mana >= MANA[1]:
            drain_path = search_solution_space(shields, poisons, recharges, (new_boss_hp - 2, boss[1]), (new_player_hp + 2, new_player_mana-MANA[1]), False, mana_spent + MANA[1], cache, path+[1])
            best = min(best, drain_path)
        # recharge path
        if not len(recharges) and new_player_mana >= MANA[4]:
            shield_path = search_solution_space(shields, poisons, recharges+[5], (new_boss_hp, boss[1]), (new_player_hp, new_player_mana-MANA[4]), False, mana_spent + MANA[4], cache, path+[4])
            best = min(best, shield_path)
        return best


if __name__ == "__main__":
    cache = {"best": 2420, "best_path": []}
    best = search_solution_space([], [], [], (58, 9), (50, 500), True, 0, cache, [])
    print(best)
    print(cache)

winscore = 21
ROLLCOUNT = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

def dfs(pos1, pos2, score1, score2):
    if score2 >= winscore:
        return 0, 1
    wins1 = wins2 = 0
    for roll in ROLLCOUNT:
        newpos = (pos1 + roll) % 10
        new_wins2, new_wins1 = dfs(pos2, newpos, score2, score1+newpos+1)
        wins1 += ROLLCOUNT[roll] * new_wins1
        wins2 += ROLLCOUNT[roll] * new_wins2
    return wins1, wins2

if __name__ == "__main__":
    # player1, player2 = 4, 9
    player1, player2 = 9, 3
    player1, player2 = player1-1, player2-1

    print(dfs(player1, player2, 0, 0))

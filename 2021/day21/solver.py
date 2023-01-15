if __name__ == "__main__":
    # player1, player2, = 4, 9
    player1, player2 = 9, 3
    player1, player2 = player1-1, player2-1

    p1_points = p2_points = 0
    rolls = 0
    while p1_points < 1000 and p2_points < 1000:
        player1 = (player1 + rolls * 3 + 6) % 10
        p1_points += player1 + 1
        if p1_points >= 1000:
            rolls += 3
            break
        player2 = (player2 + rolls * 3 + 15) % 10
        p2_points += player2 + 1
        rolls += 6

    print(rolls * min(p1_points, p2_points))

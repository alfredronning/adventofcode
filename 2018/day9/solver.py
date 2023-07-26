from collections import defaultdict

if __name__ == "__main__":
    players = 419
    marbles = 72164

    current_pos = 0
    current_player = 0
    circle = [0]
    scores = defaultdict(int)
    for score in range(1, marbles+1):
        if score%23 == 0:
            scores[current_player] += score
            current_pos = (current_pos-7)%len(circle)
            scores[current_player] += circle.pop(current_pos)
        else:
            current_pos = (current_pos+2)%len(circle)
            circle.insert(current_pos, score)
        current_player = (current_player+1)%players
    print(max(scores.values()))


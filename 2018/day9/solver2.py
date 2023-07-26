from collections import defaultdict

class Marble:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


if __name__ == "__main__":
    players = 419
    marbles = 7216400


    current_marble = Marble(0, None, None)
    current_marble.prev = current_marble # type: ignore
    current_marble.next = current_marble # type: ignore
    start_marble = current_marble

    current_player = 0
    scores = defaultdict(int)

    for score in range(1, marbles+1):
        if score%23 == 0:
            scores[current_player] += score
            current_marble = current_marble.prev.prev.prev.prev.prev.prev # type: ignore
            scores[current_player] += current_marble.prev.val

            current_marble.prev = current_marble.prev.prev
            current_marble.prev.next = current_marble
        else:
            next_marble = current_marble.next
            next_next_marble = next_marble.next # type: ignore
            current_marble = Marble(score, next_marble, next_next_marble)
            next_marble.next = current_marble # type: ignore
            next_next_marble.prev = current_marble # type: ignore
        current_player = (current_player+1)%players
    print(max(scores.values()))


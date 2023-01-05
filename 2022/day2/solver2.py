chosen_score = {"A": 1, "B": 2, "C": 3}
decrypt = {
        "X": {"A":"C", "B": "A", "C": "B"},
        "Y": {"A":"A", "B": "B", "C": "C"},
        "Z": {"A":"B", "B": "C", "C": "A"}
        }


def calculate_score(opp, me):
    me = decrypt[me][opp]
    return chosen_score[me] + (ord(me)-ord(opp)+1)%3*3

def sum_scores(rounds):
    return sum(calculate_score(r.split()[0], r.split()[1]) for r in rounds)

if __name__ == "__main__":
    rounds = open("input.txt").read().strip().split("\n")
    print(sum_scores(rounds))


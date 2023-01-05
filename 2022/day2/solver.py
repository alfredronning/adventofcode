chosen_score = {"A": 1, "B": 2, "C": 3}
decrypt = {"X": "A", "Y": "B", "Z": "C"}


def calculate_score(opp, me):
    return chosen_score[decrypt[me]] + (ord(decrypt[me])-ord(opp)+1)%3*3

def sum_scores(rounds):
    return sum(calculate_score(r.split()[0], r.split()[1]) for r in rounds)

if __name__ == "__main__":
    rounds = open("input.txt").read().strip().split("\n")
    print(sum_scores(rounds))


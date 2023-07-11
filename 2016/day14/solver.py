from hashlib import md5
from collections import defaultdict

def five_times(digest):
    res = []
    for i in range(len(digest)-4):
        if len(set(digest[i:i+5])) == 1:
            res.append(digest[i])
    return res

def first_tripple(digest):
    for i in range(len(digest)-2):
        if len(set(digest[i:i+3])) == 1:
            return digest[i]

def find_otps(salt, count):
    tripples = defaultdict(set)
    otp_idx = []
    i = 0
    break_idx = float("inf")
    while i < break_idx:
        val = salt + str(i)
        digest = md5(val.encode()).hexdigest()
        fives = five_times(digest)
        for five in fives:
            for triplet_idx in tripples[five]:
                if i - triplet_idx <= 1000:
                    otp_idx.append(triplet_idx)
                    if len(otp_idx) == count:
                        break_idx = i + 1000
            tripples[five] = set()
        tripple = first_tripple(digest)
        if first_tripple is not None:
            tripples[tripple].add(i)
        i += 1
    return sorted(otp_idx)[count-1]


if __name__ == "__main__":
    salt = "zpqevtbw"
    print(find_otps(salt, 64))


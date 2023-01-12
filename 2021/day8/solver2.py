if __name__ == "__main__":
    entries = [entry.split(" | ") for entry in open("input.txt").read().strip().split("\n")]
    res = 0
    for pattern, digits in entries:
        pattern = sorted(("".join(sorted(s)) for s in pattern.split()), key=lambda x: len(x))
        translator = {}
        translator[pattern[0]] = 1
        translator[[p for p in pattern if len(p) == 5 and len([c for c in pattern[2] if c in p]) == 2][0]] = 2
        translator[[p for p in pattern if len(p) == 5 and len([c for c in pattern[0] if c in p]) == 2][0]] = 3
        translator[pattern[2]] = 4
        translator[[p for p in pattern if len(p) == 5 and p not in translator][0]] = 5
        translator[[p for p in pattern if len(p) == 6 and len([c for c in pattern[0] if c in p]) == 1][0]] = 6
        translator[pattern[1]] = 7
        translator[pattern[9]] = 8 
        translator[[p for p in pattern if len(p) == 6 and len([c for c in pattern[2] if c in p]) == 4][0]] = 9
        translator[[p for p in pattern if len(p) == 6 and p not in translator][0]] = 0
        for i, digit in enumerate("".join(sorted(s)) for s in digits.split()[::-1]):
            res += translator[digit]*10**i
    print(res)


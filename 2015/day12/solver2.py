import json

def calc_sum(j):
    if isinstance(j, int):
        return j
    elif isinstance(j, list):
        return sum(calc_sum(n) for n in j)
    elif isinstance(j, dict):
        if "red" in j.values():
            return 0
        else:
            return sum(calc_sum(n) for n in j.values())
    return 0

if __name__ == "__main__":
    j = json.loads(open("input.txt").read().strip())
    print(calc_sum(j))


def find_cellar_index(inp):
    floor = 0
    for i, c in enumerate(inp):
        floor += (1 if c == "(" else -1)
        if floor < 0:
            return i+1
    raise Exception("Never went to the cellar")


if __name__ == "__main__":
    inp = open("input.txt").read().strip()
    print(find_cellar_index(inp))


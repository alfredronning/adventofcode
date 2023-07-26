if __name__ == "__main__":
    polymer = open("input.txt").read().strip()
    shortest = float("inf")
    for c in "abcdefghijklmnopqrstuvwxyz":
        changed = True
        p = polymer
        p = p.replace(c, "")
        p = p.replace(c.upper(), "")
        while changed:
            changed = False
            for i in range(len(p)-1):
                if p[i].lower() == p[i+1].lower() and p[i] != p[i+1]:
                    changed = True
                    p = p[:i]+p[i+2:]
                    break
        shortest = min(shortest, len(p))
    print(shortest)


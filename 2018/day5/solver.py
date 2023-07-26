if __name__ == "__main__":
    polymer = open("input.txt").read().strip()
    changed = True
    while changed:
        changed = False
        for i in range(len(polymer)-1):
            if polymer[i].lower() == polymer[i+1].lower() and polymer[i] != polymer[i+1]:
                changed = True
                polymer = polymer[:i]+polymer[i+2:]
                break
    print(len(polymer))


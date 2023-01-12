def count_fishes(fishmap, days):
    newfish = [0, 0]
    for day in range(days):
        newfish.append(fishmap[day % 7])
        fishmap[day % 7] += newfish.pop(0)
    return sum(fishmap.values()) + sum(newfish)


if __name__ == "__main__":
    fishes = open("input.txt").read().strip().split(",")
    fishmap = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for fish in fishes:
        fishmap[int(fish)] += 1
    #print(count_fishes(fishmap, 80))
    print(count_fishes(fishmap, 256))


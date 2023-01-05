def find_rucksack_value(rucksacks):
    for item in rucksacks[0]:
        if item in rucksacks[1] and item in rucksacks[2]:
            return ord(item)-96 if ord(item)>96 else ord(item)-38
    raise Exception("No shared value")

if __name__ == "__main__":
    rucksacks = open("input.txt").read().strip().split("\n")
    print(sum(find_rucksack_value(rucksacks[i*3:i*3+3]) for i in range(len(rucksacks)//3)))


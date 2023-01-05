def find_rucksack_value(rucksack):
    for item in rucksack[:len(rucksack)//2]:
        if item in rucksack[len(rucksack)//2:]:
            return ord(item)-96 if ord(item)>96 else ord(item)-38
    raise Exception("No shared value")

if __name__ == "__main__":
    rucksacks = open("input.txt").read().strip().split("\n")
    print(sum(find_rucksack_value(rucksack) for rucksack in rucksacks))


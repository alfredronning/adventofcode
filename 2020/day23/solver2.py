if __name__ == "__main__":
    total_cups = 1000000
    cups = [int(i) for i in open("input.txt").read().strip()]
    next_dict = dict()
    for i in range(len(cups)-1):
        next_dict[cups[i]] = cups[i+1]
    next_dict[cups[-1]] = len(cups)+1
    for i in range(len(cups)+1, total_cups):
        next_dict[i] = i+1
    next_dict[total_cups] = cups[0]

    current_cup = cups[0]
    for _ in range(10000000):
        after_1 = next_dict[current_cup]
        after_2 = next_dict[after_1]
        after_3 = next_dict[after_2]
        three_other = [after_1, after_2, after_3]
        destination = (current_cup - 2) % total_cups + 1
        while destination in three_other:
            destination = (destination - 2) % total_cups + 1
        next_dict[current_cup] = next_dict[after_3]
        next_dict[after_3] = next_dict[destination]
        next_dict[destination] = after_1
        current_cup = next_dict[current_cup]
    first = next_dict[1]
    second = next_dict[first]
    print(first*second)


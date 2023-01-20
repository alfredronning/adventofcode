if __name__ == "__main__":
    numbers = [int(i) for i in open("input.txt").read().strip().split(",")]
    seen_dict = dict((n, i) for i, n in enumerate(numbers[:-1]))
    last_seen = numbers[-1]
    spoken = seen_dict[0]
    for i in range(len(numbers)-1, 30000000-1):
        if last_seen in seen_dict:
            spoken = i - seen_dict[last_seen]
        else:
            spoken = 0
        seen_dict[last_seen] = i
        last_seen = spoken
    print(spoken)

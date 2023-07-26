def first_repeating(frequencies):
    frequency_sum = 0
    seen = set()
    while True:
        for frequency in frequencies:
            frequency_sum += int(frequency)
            if frequency_sum in seen:
                return frequency_sum
            seen.add(frequency_sum)

if __name__ == "__main__":
    frequencies = open("input.txt").read().strip().split("\n")
    print(first_repeating(frequencies))


if __name__ == "__main__":
    passwords = open("input.txt").read().strip().split("\n")
    count = 0
    for pw in passwords:
        letter_range, letter, password = pw.split()
        letter_range = [int(i) for i in letter_range.split("-")]
        letter = letter[0]
        letter_count = password.count(letter)
        if letter_range[0] <= letter_count <= letter_range[1]:
            count += 1
    print(count)


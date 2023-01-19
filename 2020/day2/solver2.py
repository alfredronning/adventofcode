if __name__ == "__main__":
    passwords = open("input.txt").read().strip().split("\n")
    count = 0
    for pw in passwords:
        letter_range, letter, password = pw.split()
        letter_range = [int(i) for i in letter_range.split("-")]
        letter = letter[0]
        if sum(password[i-1] == letter for i in letter_range) == 1:
            count += 1
    print(count)


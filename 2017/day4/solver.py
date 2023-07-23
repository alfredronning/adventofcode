if __name__ == "__main__":
    passwords = open("input.txt").read().strip().split("\n")
    print(sum(len(set(pw.split())) == len(pw.split()) for pw in passwords))


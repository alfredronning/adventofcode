def valid(pw):
    words = pw.split()
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                return False
    return True

if __name__ == "__main__":
    passwords = open("input.txt").read().strip().split("\n")
    print(sum(valid(pw) for pw in passwords))


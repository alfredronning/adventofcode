def find_first_marker(message):
    for i in range(len(message)):
        if len(set(message[i:i+4])) == 4:
            return i+4


if __name__ == "__main__":
    inp = open("input.txt").read()
    print(find_first_marker(inp))


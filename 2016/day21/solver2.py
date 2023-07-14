if __name__ == "__main__":
    password = [c for c in "fbgdceah"]

    operations = open("input.txt").read().strip().split("\n")
    for operation in operations[::-1]:
        o_split = operation.split()
        if "swap position" in operation:
            x, y = int(o_split[2]), int(o_split[5])
            password[x], password[y] = password[y], password[x]
        elif "swap letter" in operation:
            x, y = password.index(o_split[2]), password.index(o_split[5])
            password[x], password[y] = password[y], password[x]
        elif "rotate right" in operation:
            x = int(o_split[2])
            for i in range(x):
                password = password[1:] + [password[0]]
        elif "rotate left" in operation:
            x = int(o_split[2])
            for i in range(x):
                password = [password[-1]] + password[:-1]
        elif "rotate based on position of letter" in operation:
            password = password[1:] + [password[0]]
            for i in range(10):
                x = password.index(o_split[6])
                if x + (2 if x >= 4 else 1) == i + 1:
                    break
                password = password[1:] + [password[0]]
        elif "reverse positions" in operation:
            x, y = int(o_split[2]), int(o_split[4])
            password = password[:x] + password[x:y + 1][::-1] + password[y + 1:]
        elif "move position" in operation:
            x, y = int(o_split[2]), int(o_split[5])
            password.insert(x, password.pop(y))
        else:
            raise Exception(operation + " not listed")
    print("".join(password))


if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    visited = set()
    ip = acc = 0
    while True:
        if ip in visited:
            break
        visited.add(ip)
        opcode, operand = instructions[ip].split()
        if opcode == "acc":
            acc += int(operand)
            ip += 1
        elif opcode == "nop":
            ip += 1
        else:
            ip += int(operand)
    print(acc)


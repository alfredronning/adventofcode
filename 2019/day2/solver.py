if __name__ == "__main__":
    opcodes = [int(i) for i in open("input.txt").read().strip().split(",")]
    opcodes[1] = 12
    opcodes[2] = 2
    ip = 0
    current_op = opcodes[ip]
    while current_op != 99:
        if current_op == 1:
            opcodes[opcodes[ip+3]] = opcodes[opcodes[ip+1]]+opcodes[opcodes[ip+2]]
        if current_op == 2:
            opcodes[opcodes[ip+3]] = opcodes[opcodes[ip+1]]*opcodes[opcodes[ip+2]]
        ip += 4
        current_op = opcodes[ip]
    print(opcodes[0])


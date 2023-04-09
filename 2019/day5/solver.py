def find_output(opcodes, inp):
    ip = 0
    current_operand = opcodes[ip]
    while current_operand != 99:
        current_operand = "{:05d}".format(current_operand)
        opcode1 = ip+1 if current_operand[-3] == "1" else opcodes[ip+1]
        opcode2 = ip+2 if current_operand[-4] == "1" else opcodes[ip+2]
        opcode3 = ip+3 if current_operand[-5] == "1" else opcodes[ip+3]
        if current_operand[-1] == "1":
            opcodes[opcode3] = opcodes[opcode1]+opcodes[opcode2]
            ip += 4
        elif current_operand[-1] == "2":
            opcodes[opcode3] = opcodes[opcode1]*opcodes[opcode2]
            ip += 4
        elif current_operand[-1] == "3":
            opcodes[opcode1] = inp
            ip += 2
        elif current_operand[-1] == "4":
            print(opcodes[opcode1])
            ip += 2
        elif current_operand[-1] == "5":
            ip = ip + 3 if opcodes[opcode1] == 0 else opcodes[opcode2]
        elif current_operand[-1] == "6":
            ip = ip + 3 if opcodes[opcode1] != 0 else opcodes[opcode2]
        elif current_operand[-1] == "7":
            opcodes[opcode3] = 1 if opcodes[opcode1] < opcodes[opcode2] else 0
            ip += 4
        elif current_operand[-1] == "8":
            opcodes[opcode3] = 1 if opcodes[opcode1] == opcodes[opcode2] else 0
            ip += 4
        current_operand = opcodes[ip]
    return 0


if __name__ == "__main__":
    opcodes = [int(i) for i in open("input.txt").read().strip().split(",")]
    print(find_output(opcodes, 5))


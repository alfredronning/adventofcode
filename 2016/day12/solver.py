if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}

    ip = 0
    while ip < len(instructions):
        operator, *operands = instructions[ip].split()
        if operator == "jnz":
            if (registers[operands[0]] if operands[0] in "abcd" else int(operands[0])) != 0:
                ip += int(operands[1]) - 1
        elif operator == "cpy":
            registers[operands[1]] = registers[operands[0]] if operands[0] in "abcd" else int(operands[0])
        elif operator == "inc":
             registers[operands[0]] += 1
        elif operator == "dec":
             registers[operands[0]] -= 1
        ip += 1
    print(registers)


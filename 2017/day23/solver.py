def getval(registers, val):
    if val.lstrip("-").isnumeric():
        return int(val)
    if val not in registers:
        registers[val] = 0
    return registers[val]

if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    registers = {}

    mul_count = 0
    ip = 0
    while ip < len(instructions):
        instruction = instructions[ip]
        operator = instruction.split()[0]
        operands = instruction.split()[1:]

        if operator == "set":
            getval(registers, operands[0])
            registers[operands[0]] = getval(registers, operands[1])
        elif operator == "sub":
            registers[operands[0]] = getval(registers, operands[0]) - getval(registers, operands[1])
        elif operator == "mul":
            registers[operands[0]] = getval(registers, operands[0]) * getval(registers, operands[1])
            mul_count += 1
        elif operator == "jnz":
            if getval(registers, operands[0]) != 0:
                ip += getval(registers, operands[1]) - 1
        ip += 1

    print(mul_count)


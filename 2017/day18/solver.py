def getval(registers, val):
    if val.lstrip("-").isnumeric():
        return int(val)
    if val not in registers:
        registers[val] = 0
    return registers[val]

if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    registers = {}

    sounds = []

    ip = 0
    while ip < len(instructions):
        instruction = instructions[ip]
        operator = instruction.split()[0]
        operands = instruction.split()[1:]

        if operator == "snd":
            sounds.append(getval(registers, operands[0]))
        elif operator == "rcv":
            if getval(registers, operands[0]) != 0:
                sounds.append(sounds[-1])
                break
        elif operator == "set":
            getval(registers, operands[0])
            registers[operands[0]] = getval(registers, operands[1])
        elif operator == "add":
            registers[operands[0]] = getval(registers, operands[0]) + getval(registers, operands[1])
        elif operator == "mul":
            registers[operands[0]] = getval(registers, operands[0]) * getval(registers, operands[1])
        elif operator == "mod":
            registers[operands[0]] = getval(registers, operands[0]) % getval(registers, operands[1])
        elif operator == "jgz":
            if getval(registers, operands[0]) > 0:
                ip += getval(registers, operands[1]) - 1
        ip += 1
    print(sounds[-1])


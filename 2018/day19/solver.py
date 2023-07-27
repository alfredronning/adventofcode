def apply_instruction(registers, instruction):
    operator, operands = instruction[0], instruction[1:]
    if operator == "addr":
        registers[operands[2]] = registers[operands[0]]+registers[operands[1]]
    if operator == "addi":
        registers[operands[2]] = registers[operands[0]]+operands[1]
    if operator == "mulr":
        registers[operands[2]] = registers[operands[0]]*registers[operands[1]]
    if operator == "muli":
        registers[operands[2]] = registers[operands[0]]*operands[1]
    if operator == "banr":
        registers[operands[2]] = registers[operands[0]]&registers[operands[1]]
    if operator == "bani":
        registers[operands[2]] = registers[operands[0]]&operands[1]
    if operator == "borr":
        registers[operands[2]] = registers[operands[0]]|registers[operands[1]]
    if operator == "bori":
        registers[operands[2]] = registers[operands[0]]|operands[1]
    if operator == "setr":
        registers[operands[2]] = registers[operands[0]]
    if operator == "seti":
        registers[operands[2]] = operands[0]
    if operator == "gtir":
        registers[operands[2]] = 1 if operands[0]>registers[operands[1]] else 0
    if operator == "gtri":
        registers[operands[2]] = 1 if registers[operands[0]]>operands[1] else 0
    if operator == "gtrr":
        registers[operands[2]] = 1 if registers[operands[0]]>registers[operands[1]] else 0
    if operator == "eqir":
        registers[operands[2]] = 1 if operands[0]==registers[operands[1]] else 0
    if operator == "eqri":
        registers[operands[2]] = 1 if registers[operands[0]]==operands[1] else 0
    if operator == "eqrr":
        registers[operands[2]] = 1 if registers[operands[0]]==registers[operands[1]] else 0

if __name__ == "__main__":
    f = open("input.txt").read().strip().split("\n")
    ip_instruction, instructions = f[0], f[1:]
    instructions = [i.split("//")[0] for i in instructions]
    registers = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    ip_register = int(ip_instruction.split()[1])
    while registers[ip_register] < len(instructions):
        ip = registers[ip_register] + 2
        instruction = instructions[registers[ip_register]]
        s = instruction.split()
        if ip == 4:
            pass
        if ip == 5:
            pass
        if ip == 6:
            pass
        if ip == 7:
            pass
        if ip == 8:
            pass
        if ip == 9:
            pass
        if ip == 10:
            pass
        if ip == 11:
            pass
        if ip == 12:
            pass
        if ip == 13:
            pass
        if ip == 14:
            pass
        if ip == 15:
            pass
        if ip == 16:
            pass
        if ip == 17:
            pass
        if ip == 18:
            pass
        if ip == 19:
            pass
        if ip == 20:
            pass
        if ip == 21:
            pass
        if ip == 22:
            pass
        if ip == 23:
            pass
        if ip == 24:
            pass
        if ip == 25:
            pass
        if ip == 26:
            pass
        if ip == 27:
            pass
        if ip == 28:
            pass
        if ip == 29:
            pass
        if ip == 30:
            pass
        if ip == 31:
            pass
        if ip == 32:
            pass
        if ip == 33:
            pass
        if ip == 34:
            pass
        if ip == 35:
            pass
        operator, operands = s[0], s[1:]
        apply_instruction(registers, [operator]+[int(i) for i in operands])
        registers[ip_register] += 1
    print(registers[0])


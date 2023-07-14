def toggled_instruction(instructions, idx):
    operator, *operands = instructions[idx].split("//")[0].strip().split()
    if len(operands) == 1:
        if operator == "inc":
            return "dec "+operands[0]
        else:
            return "inc "+operands[0]
    if operator == "jnz":
        return "cpy " + operands[0] + " " + operands[1]
    else:
        return "jnz " + operands[0] + " " + operands[1]


if __name__ == "__main__":
    instructions = [l for l in open("input.txt").read().strip().split("\n") if len(l) and l[0] not in "/ "]
    # instructions = [l for l in open("orig.txt").read().strip().split("\n") if len(l) and l[0] not in "/ "]
    registers = {"a": 12, "b": 0, "c": 0, "d": 0}

    ip = 0
    i = 0
    while ip < len(instructions):
        operator, *operands = instructions[ip].split("//")[0].strip().split()
        if ip == 18:
            x = 1
        if ip == 23:
            x = 1
        if ip == 25:
            x = 1
        if operator == "mul":
            o1 = registers[operands[0]] if operands[0] in registers else int(operands[0])
            o2 = registers[operands[1]] if operands[1] in registers else int(operands[1])
            registers[operands[2]] = o1*o2
        if operator == "add":
            o1 = registers[operands[0]] if operands[0] in registers else int(operands[0])
            o2 = registers[operands[1]] if operands[1] in registers else int(operands[1])
            registers[operands[2]] = o1+o2
        if operator == "jnz":
            if (registers[operands[0]] if operands[0] in "abcd" else int(operands[0])) != 0:
                ip += (registers[operands[1]] if operands[1] in "abcd" else int(operands[1])) - 1
        elif operator == "cpy":
            if operands[1] not in registers:
                continue
            registers[operands[1]] = registers[operands[0]] if operands[0] in "abcd" else int(operands[0])
        elif operator == "inc":
            registers[operands[0]] += 1
        elif operator == "dec":
            registers[operands[0]] -= 1
        elif operator == "tgl":
            idx = ip + registers[operands[0]] if operands[0] in "abcd" else int(operands[0])
            if idx > 0 and idx < len(instructions):
                instructions[idx] = toggled_instruction(instructions, idx)
        ip += 1
        i += 1
    print(registers)


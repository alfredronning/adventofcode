def toggled_instruction(instructions, idx):
    operator, *operands = instructions[idx].split("//")[0].strip().split()
    if len(operands) == 1:
        if operator == "inc":
            return "dec " + operands[0]
        else:
            return "inc " + operands[0]
    if operator == "jnz":
        return "cpy " + operands[0] + " " + operands[1]
    else:
        return "jnz " + operands[0] + " " + operands[1]


def valid_signal(instructions, a):
    registers = {"a": a, "b": 0, "c": 0, "d": 0}

    ip = 0
    signal = 1
    signal_count = 0
    time_since_last_signal = 0
    while ip < len(instructions):
        time_since_last_signal += 1
        operator, *operands = instructions[ip].split("//")[0].strip().split()
        if operator == "add":
            o1 = registers[operands[0]] if operands[0] in "abcd" else int(operands[0])
            o2 = registers[operands[1]] if operands[1] in "abcd" else int(operands[1])
            registers[operands[2]] = o1 + o2
        if operator == "mul":
            o1 = registers[operands[1]] if operands[1] in "abcd" else int(operands[1])
            o2 = registers[operands[2]] if operands[2] in "abcd" else int(operands[2])
            registers[operands[0]] = o1 * o2
        if operator == "jnz":
            if (registers[operands[0]] if operands[0] in "abcd" else int(operands[0])) != 0:
                ip += registers[operands[1]] if operands[1] in "abcd" else int(operands[1]) - 1
        elif operator == "cpy":
            if operands[1] not in registers:
                continue
            registers[operands[1]] = registers[operands[0]] if operands[0] in "abcd" else int(operands[0])
        elif operator == "inc":
            registers[operands[0]] += 1
        elif operator == "dec":
            registers[operands[0]] -= 1

        # enhanced instruction set
        elif operator == "cp2":
            registers[operands[1]] = (registers[operands[0]] if operands[0] in "abcd" else int(operands[0])) // 2
        elif operator == "md2":
            registers[operands[0]] = registers[operands[0]] % 2
        elif operator == "out":
            output = registers[operands[0]] if operands[0] in "abcd" else int(operands[0])
            if signal == 0 and output != 1:
                return False
            if signal == 1 and output != 0:
                return False
            signal = output
            signal_count += 1
            time_since_last_signal = 0
        if signal_count == 20:
            return True
        ip += 1


if __name__ == "__main__":
    # instructions = open("orig.txt").read().strip().split("\n")
    instructions = [i for i in open("input.txt").read().strip().split("\n") if len(i) and i[0] not in "/ "]
    # for i in range(200):
    for i in range(1000000):
        if valid_signal(instructions, i):
            print(i)
            break

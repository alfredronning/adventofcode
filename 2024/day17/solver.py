registers, program = open("input.txt").read().strip().split("\n\n")

a, b, c = [int(r.split(": ")[1]) for r in registers.split("\n")]
program = [int(i) for i in program.split(": ")[1].split(",")]

ip = 0
outputs = []

def combo(a, b, c, operand):
    if operand >= 0 and operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    raise Exception("Invalid combo operand: " + str(operand))

while ip != len(program):
    opcode, operand = program[ip:ip+2]
    if opcode == 0:
        a //= 2**combo(a, b, c, operand)
    elif opcode == 1:
        b ^= operand
    elif opcode == 2:
        b = combo(a, b, c, operand) % 8
    elif opcode == 3:
        if a != 0:
            ip = operand
            continue
    elif opcode == 4:
        b ^= c
    elif opcode == 5:
        outputs.append(str(combo(a, b, c, operand) % 8))
    elif opcode == 6:
        b = a // 2**combo(a, b, c, operand)
    elif opcode == 7:
        c = a // 2**combo(a, b, c, operand)
    else:
        raise Exception("Invalid opcode: " + str(opcode))
    ip += 2

print(",".join(outputs))


from collections import defaultdict

def apply_operation(registers, register, op, value):
    if op == "inc":
        registers[register] += int(value)
        registers["max"] = max(registers["max"], registers[register])
    elif op == "dec":
        registers[register] -= int(value)
        registers["max"] = max(registers["max"], registers[register])


def condition_true(registers, register, op, value):
    if op == "<" and registers[register] < int(value):
        return True
    elif op == ">" and registers[register] > int(value):
        return True
    elif op == "<=" and registers[register] <= int(value):
        return True
    elif op == ">=" and registers[register] >= int(value):
        return True
    elif op == "!=" and registers[register] != int(value):
        return True
    elif op == "==" and registers[register] == int(value):
        return True
    return False


if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    registers = defaultdict(int)
    registers["max"] = 0

    for instruction in instructions:
        operation, condition = instruction.split(" if ")

        if condition_true(registers, *condition.split()):
            apply_operation(registers, *operation.split())

    print(registers["max"])


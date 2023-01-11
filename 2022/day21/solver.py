MONKEYS = dict(m.split(": ") for m in open("input.txt").read().strip().split("\n"))

def calculate(monkey):
    yell = MONKEYS[monkey]
    if yell.isdigit():
        return int(yell)
    operand1, opcode, operand2 = yell.split()
    if opcode == "+":
        return calculate(operand1) + calculate(operand2)
    if opcode == "-":
        return calculate(operand1) - calculate(operand2)
    if opcode == "*":
        return calculate(operand1) * calculate(operand2)
    if opcode == "/":
        return calculate(operand1) / calculate(operand2)

if __name__ == "__main__":
    print(int(calculate("root")))


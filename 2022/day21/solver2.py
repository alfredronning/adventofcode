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

def find_you_path(monkey, path):
    yell = MONKEYS[monkey]
    if monkey == "humn":
        return path
    if yell.isdigit():
        return False
    operand1, opcode, operand2 = yell.split()
    path1 = find_you_path(operand1, path+[1])
    path2 = find_you_path(operand2, path+[2])
    if path1:
        return path1
    return path2
    
def find_yell(monkey, you_path, eq):
    if monkey == "humn":
        return eq
    yell = MONKEYS[monkey]
    operand1, opcode, operand2 = yell.split()
    next_you_path = you_path.pop(0)
    should_eq = calculate(operand1 if next_you_path == 2 else operand2)
    next_monkey = operand2 if next_you_path == 2 else operand1
    if opcode == "+":
        return find_yell(next_monkey, you_path, eq-should_eq)
    if opcode == "-":
        return find_yell(next_monkey, you_path, eq+should_eq)
    if opcode == "*":
        return find_yell(next_monkey, you_path, eq/should_eq)
    if opcode == "/":
        return find_yell(next_monkey, you_path, eq*should_eq)

if __name__ == "__main__":
    you_path = find_you_path("root", [])
    print(int(find_yell("root", you_path, 0)))

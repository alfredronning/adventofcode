def getval(registers, val):
    if val.lstrip("-").isdigit():
        return int(val)
    if val not in registers:
        registers[val] = 0
    return registers[val]

class Program:
    def __init__(self, id):
        self.registers = {"rcv": [], "p": id}
        self.ip = 0
        self.locked = False
        self.gen = self.generator()

    def generator(self):
        while self.ip < len(instructions):
            instruction = instructions[self.ip]
            operator = instruction.split()[0]
            operands = instruction.split()[1:]

            if operator == "snd":
                yield getval(self.registers, operands[0])
            elif operator == "rcv":
                if len(self.registers["rcv"]) == 0:
                    self.locked = True
                    self.ip -= 1
                    yield None
                else:
                    self.locked = False
                    getval(self.registers, operands[0])
                    self.registers[operands[0]] = self.registers["rcv"].pop(0)
            elif operator == "set":
                getval(self.registers, operands[0])
                self.registers[operands[0]] = getval(self.registers, operands[1])
            elif operator == "add":
                self.registers[operands[0]] = getval(self.registers, operands[0]) + getval(self.registers, operands[1])
            elif operator == "mul":
                self.registers[operands[0]] = getval(self.registers, operands[0]) * getval(self.registers, operands[1])
            elif operator == "mod":
                self.registers[operands[0]] = getval(self.registers, operands[0]) % getval(self.registers, operands[1])
            elif operator == "jgz":
                if getval(self.registers, operands[0]) > 0:
                    self.ip += getval(self.registers, operands[1]) - 1
            self.ip += 1

    def recv(self, val):
        self.registers["rcv"].append(val)

if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    p_0 = Program(0)
    p_1 = Program(1)

    count = 0

    while not p_0.locked or not p_1.locked:
        p_0_out = next(p_0.gen)
        p_1_out = next(p_1.gen)

        if p_0_out is not None:
            p_1.recv(p_0_out)
        if p_1_out is not None:
            count += 1
            p_0.recv(p_1_out)
    print(count)


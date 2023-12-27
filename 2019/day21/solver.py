from collections import defaultdict

class Program:
    def __init__(self, opcodes):
        self.opcodes = opcodes
        self.ip = 0
        self.inputs = []
        self.outputs = []

    def continue_program(self):
        current_operand = self.opcodes[self.ip]
        relative_base = 0
        while current_operand != 99:
            current_operand = "{:05d}".format(current_operand)
            opcode1 = self.opcodes[self.ip+1]+relative_base if current_operand[-3] == "2" else self.ip+1 if current_operand[-3] == "1" else self.opcodes[self.ip+1]
            opcode2 = self.opcodes[self.ip+2]+relative_base if current_operand[-4] == "2" else self.ip+2 if current_operand[-4] == "1" else self.opcodes[self.ip+2]
            opcode3 = self.opcodes[self.ip+3]+relative_base if current_operand[-5] == "2" else self.ip+3 if current_operand[-5] == "1" else self.opcodes[self.ip+3]
            if current_operand[-1] == "1":
                self.opcodes[opcode3] = self.opcodes[opcode1]+self.opcodes[opcode2]
                self.ip += 4
            elif current_operand[-1] == "2":
                self.opcodes[opcode3] = self.opcodes[opcode1]*self.opcodes[opcode2]
                self.ip += 4
            elif current_operand[-1] == "3":
                if self.inputs:
                    self.opcodes[opcode1] = self.inputs.pop(0)
                    self.ip += 2
                else:
                    return
            elif current_operand[-1] == "4":
                self.outputs.append(self.opcodes[opcode1])
                self.ip += 2
            elif current_operand[-1] == "5":
                self.ip = self.ip + 3 if self.opcodes[opcode1] == 0 else self.opcodes[opcode2]
            elif current_operand[-1] == "6":
                self.ip = self.ip + 3 if self.opcodes[opcode1] != 0 else self.opcodes[opcode2]
            elif current_operand[-1] == "7":
                self.opcodes[opcode3] = 1 if self.opcodes[opcode1] < self.opcodes[opcode2] else 0
                self.ip += 4
            elif current_operand[-1] == "8":
                self.opcodes[opcode3] = 1 if self.opcodes[opcode1] == self.opcodes[opcode2] else 0
                self.ip += 4
            elif current_operand[-1] == "9":
                relative_base += self.opcodes[opcode1]
                self.ip += 2
            current_operand = opcodes[self.ip]

    def add_input(self, i):
        self.inputs.append(i)

    def add_inputs(self, i):
        self.inputs +=i


    def get_outputs(self):
        return self.outputs

    def clear_outputs(self):
        self.outputs = []


if __name__ == "__main__":
    opcodes = defaultdict(int)
    for i, v in enumerate(open("input.txt").read().strip().split(",")):
        opcodes[i] = int(v)

    program = Program(opcodes)
    program.add_inputs([ord(c) for c in 
        "NOT C J\n" +
        "AND D J\n" +
        "NOT A T\n"
        "OR T J\n"
        "WALK\n"
    ])
    program.continue_program()
    outputs = program.get_outputs()
    print("".join(chr(c) if c < 0xff else str(c) for c in outputs))

    

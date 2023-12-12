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

def is_in_beam(x, y, opcodes):
    program = Program(opcodes.copy())
    program.add_input(x)
    program.add_input(y)
    program.continue_program()
    return program.get_outputs()[0]

if __name__ == "__main__":
    opcodes = defaultdict(int)
    for i, v in enumerate(open("input.txt").read().strip().split(",")):
        opcodes[i] = int(v)
    leftedge = rightedge = 3
    row = 4
    leftedges = {}
    rightedges = {}
    square_size = 99
    while True:
        row += 1
        if not is_in_beam(row, leftedge, opcodes):
            leftedge += 1
        if is_in_beam(row, rightedge+1, opcodes):
            rightedge += 1
        leftedges[row] = leftedge
        rightedges[row] = rightedge
        if row < square_size*2:
            continue
        if rightedges[row-square_size] - leftedges[row] == square_size:
            print(10000*(row-square_size)+leftedges[row])
            break


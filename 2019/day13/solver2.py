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
            if len(self.outputs) == 2270:
                print("break")
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
        raise Exception("done")

    def add_input(self, i):
        self.inputs.append(i)

    def get_outputs(self):
        return self.outputs

def print_board(board):
    minx = miny = 50
    maxx = maxy = -50
    for x, y in board:
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
    for y in range(miny, maxy+1): #type: ignore
        row = ""
        for x in range(minx, maxx+1): #type: ignore
            if (x, y) in board:
                row += board[(x, y)]
            else:
                row += "."
        print(row)

if __name__ == "__main__":
    opcodes = defaultdict(int)
    for i, v in enumerate(open("input.txt").read().strip().split(",")):
        opcodes[i] = int(v)
    opcodes[0] = 2
    program = Program(opcodes)
    program.continue_program()
    output = program.get_outputs()
    res = 0
    board = dict()
    ballpos = pos = 0
    score = 0
    finnished = False
    while not finnished:
        if ballpos > pos:
            inp = 1
        elif ballpos < pos:
            inp = -1
        else:
            inp = 0
        program.add_input(inp)
        try:
            program.continue_program()
        except Exception:
            #finnished = True
            pass
        for i in range(len(output)//3):
            x, y, t = output[i*3:i*3+3]
            if x == -1 and y == 0:
                score = t
            elif t == 3:
                board[(x, y)] = "_"
                pos = x
            elif t == 4:
                board[(x, y)] = "o"
                ballpos = x
            elif t == 0:
                board[(x, y)] = " "
            elif t == 1:
                board[(x, y)] = "|"
            elif t == 2:
                board[(x, y)] = "#"
        print_board(board)
        print(score)


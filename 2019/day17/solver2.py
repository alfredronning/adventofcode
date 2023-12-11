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

def parse_output(output):
    output = "".join(chr(c) for c in output).split("\n")
    intersections = set()
    scaffolds = set()
    robot_pos = None
    for i in range(1, len(output)-1):
        for j in range(1, len(output[i])-1):
            if output[i][j] in "<>^v":
                robot_pos = (i, j)
            if output[i][j] != "#":
                continue
            scaffolds.add((i, j))
            scaffold_count = 0
            for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if output[i+d[0]][j+d[1]] == "#":
                    scaffold_count += 1
                else:
                    break
            if scaffold_count == 4:
                intersections.add((i, j))
    return robot_pos, scaffolds, intersections

if __name__ == "__main__":
    opcodes = defaultdict(int)
    for i, v in enumerate(open("input.txt").read().strip().split(",")):
        opcodes[i] = int(v)
    opcodes[0] = 2
    program = Program(opcodes)
    program.continue_program()
    output = program.get_outputs()
    print("".join(chr(c) for c in output))
    print(len("".join(chr(c) for c in output).split("\n")[0]))
    """
    R,6,L,8,R,8,R,6,L,8,R,8,R,4,R,6,R,6,R,4,R,4,L,8,R,6,L,10,L,10,R,4,R,6,R,6,R,4,R,4,L,8,R,6,L,10,L,10,R,4,R,6,R,6,R,4,R,4,L,8,R,6,L,10,L,10,R,6,L,8,R,8,L,8,R,6,L,10,L,10
    C,C,B,A,B,A,B,A,C,A
    A = L,8,R,6,L,10,L,10
    B = R,4,R,6,R,6,R,4,R,4
    C = R,6,L,8,R,8
    """
    inputs = "C,C,B,A,B,A,B,A,C,A\nL,8,R,6,L,10,L,10\nR,4,R,6,R,6,R,4,R,4\nR,6,L,8,R,8\ny\n"
    program.add_inputs([ord(c) for c in inputs])
    while output:
        print(output[-1])
        program.clear_outputs()
        output = program.get_outputs()
        program.continue_program()


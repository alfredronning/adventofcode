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
                    return self.outputs.pop(0) if self.outputs else None
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

def print_board(discovered, position):
    minx = miny = 100000000
    maxx = maxy = -minx
    for x, y in discovered:
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
    for x in range(minx, maxx+1):
        row = ""
        for y in range(miny, maxy+1):
            if (x, y) == position:
                row += "D"
            elif (x, y) in discovered:
                row += "# O"[discovered[(x, y)]]
            else:
                row += "."
        print(row)
    print("----------------------------------------------------------")

def add_undiscovered_neighbours(undiscovered, discovered, position):
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        neighbour = (position[0]+d[0], position[1]+d[1])
        if neighbour not in discovered:
            undiscovered.add(neighbour)

def get_closest(undiscovered, position):
    shortest = float("inf")
    best = None
    for u in undiscovered:
        dist = (position[0]-u[0])**2+(position[1]-u[1])**2
        if dist < shortest:
            shortest = dist
            best = u
    return best

def generate_path(came_from, current):
    path = []
    while current in came_from:
        prev = came_from[current]
        if current[0]-prev[0] == 1:
            path.append(2)
        if current[0]-prev[0] == -1:
            path.append(1)
        if current[1]-prev[1] == 1:
            path.append(4)
        if current[1]-prev[1] == -1:
            path.append(3)
        current = prev
    return path[::-1]

def shortest_path(discovered, position, goal):
    graph = set(n for n in discovered if discovered[n] == 1)
    visited = set()
    dists = dict()
    came_from = dict()
    dists[position] = 0
    queue = [position]
    while queue:
        queue.sort(key=lambda x: -dists[x])
        position = queue.pop()
        visited.add(position)
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbour = (position[0]+d[0], position[1]+d[1])
            if neighbour == goal:
                came_from[neighbour] = position
                return generate_path(came_from, neighbour)
            if neighbour not in graph:
                continue
            if neighbour not in visited:
                came_from[neighbour] = position
                dists[neighbour] = dists[position] + 1
                queue.append(neighbour)
            elif dists[neighbour] > dists[position] + 1:
                dists[neighbour] = dists[position] + 1
                came_from[neighbour] = position
    raise Exception("no path!")

def longest_path(discovered, position):
    graph = set(n for n in discovered if discovered[n] == 1)
    visited = set()
    dists = dict()
    came_from = dict()
    dists[position] = 0
    queue = [position]
    while queue:
        queue.sort(key=lambda x: -dists[x])
        position = queue.pop()
        visited.add(position)
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbour = (position[0]+d[0], position[1]+d[1])
            if neighbour not in graph:
                continue
            if neighbour not in visited:
                came_from[neighbour] = position
                dists[neighbour] = dists[position] + 1
                queue.append(neighbour)
            elif dists[neighbour] > dists[position] + 1:
                dists[neighbour] = dists[position] + 1
                came_from[neighbour] = position
    return max(dists.values())

def discover_all(program, discovered):
    position = (0, 0)
    discovered[position] = 1
    undiscovered = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    while undiscovered:
        current = get_closest(undiscovered, position)
        undiscovered.remove(current)
        path = shortest_path(discovered, position, current)
        while path:
            inp = path.pop(0)
            program.add_input(inp)
            output = program.continue_program()
            if output is None:
                continue
            direction = [(-1, 0), (1, 0), (0, -1), (0, 1)][inp-1]
            new_position = (position[0]+direction[0], position[1]+direction[1])
            if new_position in undiscovered:
                undiscovered.remove(new_position)
            if output == 0:
                discovered[new_position] = 0
                break
            elif output == 1:
                position = new_position
                discovered[position] = 1
                add_undiscovered_neighbours(undiscovered, discovered, position)
            elif output == 2:
                position = new_position
                discovered[position] = 2
                add_undiscovered_neighbours(undiscovered, discovered, position)

if __name__ == "__main__":
    opcodes = defaultdict(int)
    for i, v in enumerate(open("input.txt").read().strip().split(",")):
        opcodes[i] = int(v)
    program = Program(opcodes)
    program.continue_program()
    output = program.continue_program()
    discovered = dict()
    discover_all(program, discovered)
    print_board(discovered, (0, 0))
    oxygenpos = [k for k in discovered if discovered[k] == 2][0]
    print(len(shortest_path(discovered, (0, 0), oxygenpos)))
    print(longest_path(discovered, oxygenpos))



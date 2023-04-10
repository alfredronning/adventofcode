def get_val(memory, val):
    if val.isnumeric():
        return int(val)
    if val in memory:
        return memory[val]

def execute_instruction(memory, instruction):
    inp, out = instruction.split(" -> ")
    if inp.isnumeric():
        memory[out] = int(inp)
        return True
    inp = inp.split()
    if "NOT" in inp:
        op1 = get_val(memory, inp[1])
        if op1 is None:
            return False
        memory[out] = 65535 ^ op1
        return True
    elif "OR" in inp:
        op1 = get_val(memory, inp[0])
        op2 = get_val(memory, inp[2])
        if op1 is None or op2 is None:
            return False
        memory[out] = op1 | op2
        return True
    elif "AND" in inp:
        op1 = get_val(memory, inp[0])
        op2 = get_val(memory, inp[2])
        if op1 is None or op2 is None:
            return False
        memory[out] = op1 & op2
        return True
    elif "LSHIFT" in inp:
        op1 = get_val(memory, inp[0])
        if op1 is None:
            return False
        memory[out] = op1 << int(inp[2])
        return True
    elif "RSHIFT" in inp:
        op1 = get_val(memory, inp[0])
        if op1 is None:
            return False
        memory[out] = op1 >> int(inp[2])
        return True
    elif len(inp) == 1:
        op1 = get_val(memory, inp[0])
        if op1 is None:
            return False
        memory[out] = op1
        return True
    raise Exception("unknown gate " + instruction)

def execute_queue(memory, queued):
    changed = True
    while changed and len(queued):
        changed = False
        for instruction in queued:
            if execute_instruction(memory, instruction):
                queued.remove(instruction)
                changed = True
                break

if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    queued = []
    memory = dict()
    for instruction in instructions:
        if execute_instruction(memory, instruction):
            execute_queue(memory, queued)
        else:
            queued.append(instruction)
    memory["b"] = memory["a"]
    for instruction in instructions:
        if execute_instruction(memory, instruction):
            execute_queue(memory, queued)
        else:
            queued.append(instruction)
    print(memory["a"])

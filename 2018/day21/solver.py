def apply_instruction(registers, instruction):
    operator, operands = instruction[0], instruction[1:]
    if operator == "addr":
        registers[operands[2]] = registers[operands[0]]+registers[operands[1]]
    if operator == "addi":
        registers[operands[2]] = registers[operands[0]]+operands[1]
    if operator == "mulr":
        registers[operands[2]] = registers[operands[0]]*registers[operands[1]]
    if operator == "muli":
        registers[operands[2]] = registers[operands[0]]*operands[1]
    if operator == "banr":
        registers[operands[2]] = registers[operands[0]]&registers[operands[1]]
    if operator == "bani":
        registers[operands[2]] = registers[operands[0]]&operands[1]
    if operator == "borr":
        registers[operands[2]] = registers[operands[0]]|registers[operands[1]]
    if operator == "bori":
        registers[operands[2]] = registers[operands[0]]|operands[1]
    if operator == "setr":
        registers[operands[2]] = registers[operands[0]]
    if operator == "seti":
        registers[operands[2]] = operands[0]
    if operator == "gtir":
        registers[operands[2]] = 1 if operands[0]>registers[operands[1]] else 0
    if operator == "gtri":
        registers[operands[2]] = 1 if registers[operands[0]]>operands[1] else 0
    if operator == "gtrr":
        registers[operands[2]] = 1 if registers[operands[0]]>registers[operands[1]] else 0
    if operator == "eqir":
        registers[operands[2]] = 1 if operands[0]==registers[operands[1]] else 0
    if operator == "eqri":
        registers[operands[2]] = 1 if registers[operands[0]]==operands[1] else 0
    if operator == "eqrr":
        registers[operands[2]] = 1 if registers[operands[0]]==registers[operands[1]] else 0


if __name__ == "__main__":
    f = open("orig.txt").read().strip().split("\n")
    ip_instruction, instructions = f[0], f[1:]
    instructions = [i.split("//")[0] for i in instructions]
    ip_register = int(ip_instruction.split()[1])
    
    #registers = {0: 13522479, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    registers = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    instructions_executed = 0
    visited = set()
    prevoius = 0
    while registers[ip_register] < len(instructions):
        ip = registers[ip_register] + 2
        # a må være like register 2 når ip = 28, eller 30 i input
        # finner siste verdi før den repeterer 13min :S
        if ip == 30:
            if registers[2] in visited:
                print(prevoius)
                break
            prevoius = registers[2]
            visited.add(registers[2])
        if instructions_executed == 1806:
           pass
        instruction = instructions[registers[ip_register]]
        s = instruction.split()
        operator, operands = s[0], s[1:]
        apply_instruction(registers, [operator]+[int(i) for i in operands])
        registers[ip_register] += 1
        instructions_executed += 1
        


from collections import defaultdict

def apply_instruction(registers, instruction):
    operator, *operands = instruction
    if operator == "addr":
        registers[operands[2]] = registers[operands[0]]+registers[operands[1]]
    if operator == "addi":
        registers[operands[2]] = registers[operands[0]]+int(operands[1])
    if operator == "mulr":
        registers[operands[2]] = registers[operands[0]]*registers[operands[1]]
    if operator == "muli":
        registers[operands[2]] = registers[operands[0]]*int(operands[1])
    if operator == "banr":
        registers[operands[2]] = registers[operands[0]]&registers[operands[1]]
    if operator == "bani":
        registers[operands[2]] = registers[operands[0]]&int(operands[1])
    if operator == "borr":
        registers[operands[2]] = registers[operands[0]]|registers[operands[1]]
    if operator == "bori":
        registers[operands[2]] = registers[operands[0]]|int(operands[1])
    if operator == "setr":
        registers[operands[2]] = registers[operands[0]]
    if operator == "seti":
        registers[operands[2]] = int(operands[0])
    if operator == "gtir":
        registers[operands[2]] = 1 if int(operands[0])>registers[operands[1]] else 0
    if operator == "gtri":
        registers[operands[2]] = 1 if registers[operands[0]]>int(operands[1]) else 0
    if operator == "gtrr":
        registers[operands[2]] = 1 if registers[operands[0]]>registers[operands[1]] else 0
    if operator == "eqir":
        registers[operands[2]] = 1 if int(operands[0])==registers[operands[1]] else 0
    if operator == "eqri":
        registers[operands[2]] = 1 if registers[operands[0]]==int(operands[1]) else 0
    if operator == "eqrr":
        registers[operands[2]] = 1 if registers[operands[0]]==registers[operands[1]] else 0

def find_three_or_more_count(samples):
    operators = ["addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]
    res = 0
    for sample in samples:
        before, instruction, after = sample.split("\n")
        operator, *_ = instruction.split()

        before = [int(i) for i in before.split("[")[1][:-1].split(", ")]
        instruction = instruction.split()[1:]
        after = [int(i) for i in after.split("[")[1][:-1].split(", ")]

        valid = 0
        for candidate in operators[:]:
            after_map = {"0": before[0], "1": before[1], "2": before[2], "3": before[3]}
            apply_instruction(after_map, [candidate]+instruction)
            if all(after_map[str(i)] == after[i] for i in range(len(after))):
                valid += 1
        if valid >= 3:
            res += 1
    return res

def execute_instructions(instructions, instruction_map):
    registers = defaultdict(int)
    for instruction in instructions:
        mapped_instruction = instruction.split()
        mapped_instruction[0] = instruction_map[mapped_instruction[0]]
        apply_instruction(registers, mapped_instruction)
    return registers

if __name__ == "__main__":
    samples, instructions = open("input.txt").read().strip().split("\n\n\n")
    three_or_more_candidates = find_three_or_more_count(samples.split("\n\n"))
    print(three_or_more_candidates)


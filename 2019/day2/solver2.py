def calc_output(opcodes, noun, verb):
    opcodes = opcodes[:]
    opcodes[1] = noun
    opcodes[2] = verb
    ip = 0
    current_op = opcodes[ip]
    while current_op != 99:
        if current_op == 1:
            opcodes[opcodes[ip+3]] = opcodes[opcodes[ip+1]]+opcodes[opcodes[ip+2]]
        if current_op == 2:
            opcodes[opcodes[ip+3]] = opcodes[opcodes[ip+1]]*opcodes[opcodes[ip+2]]
        ip += 4
        current_op = opcodes[ip]
    return opcodes[0]

if __name__ == "__main__":
    opcodes = [int(i) for i in open("input.txt").read().strip().split(",")]
    for noun in range(99):
        for verb in range(99):
            if calc_output(opcodes, noun, verb) == 19690720:
                print(noun*100+verb)


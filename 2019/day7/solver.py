def find_output(opcodes, phase_setting, inp):
    ip = 0
    current_operand = opcodes[ip]
    phase_set = False
    while current_operand != 99:
        current_operand = "{:05d}".format(current_operand)
        opcode1 = opcodes[ip+1] if current_operand[-3] == "1" or current_operand[-1] in "3456" else opcodes[opcodes[ip+1]]
        opcode2 = opcodes[ip+2] if current_operand[-4] == "1" or current_operand[-1] in "34" else opcodes[opcodes[ip+2]]
        opcode3 = ip+3 if current_operand[-5] == "1" or current_operand[-1] in "34" else opcodes[ip+3]
        if current_operand[-1] == "1":
            opcodes[opcode3] = opcode1+opcode2
            ip += 4
        elif current_operand[-1] == "2":
            opcodes[opcode3] = opcode1*opcode2
            ip += 4
        elif current_operand[-1] == "3":
            opcodes[opcode1] = inp if phase_set else phase_setting
            phase_set = True
            ip += 2
        elif current_operand[-1] == "4":
            return opcodes[opcode1]
        elif current_operand[-1] == "5":
            ip = ip + 3 if opcode1 == 0 else opcode2
        elif current_operand[-1] == "6":
            ip = ip + 3 if opcode1 != 0 else opcode2
        elif current_operand[-1] == "7":
            opcodes[opcode3] = 1 if opcode1 < opcode2 else 0
            ip += 4
        elif current_operand[-1] == "8":
            opcodes[opcode3] = 1 if opcode1 == opcode2 else 0
            ip += 4
        current_operand = opcodes[ip]
    return 0

def find_thruster_signal(opcodes, phase_setting):
    output = 0
    for i in range(5):
        output = find_output(opcodes[:], phase_setting[i], output)
    return output

def find_max_thruster_signal(opcodes):
    max_thruster_signal = 0
    for s1 in range(5):
        for s2 in [i for i in range(5) if i not in [s1]]:
            for s3 in [i for i in range(5) if i not in [s1, s2]]:
                for s4 in [i for i in range(5) if i not in [s1, s2, s3]]:
                    for s5 in [i for i in range(5) if i not in [s1, s2, s3, s4]]:
                        thruster_signal = find_thruster_signal(opcodes, [s1, s2, s3, s4, s5])
                        max_thruster_signal = max(max_thruster_signal, thruster_signal)
    return max_thruster_signal


if __name__ == "__main__":
    opcodes = [int(i) for i in open("input.txt").read().strip().split(",")]
    print(find_max_thruster_signal(opcodes))


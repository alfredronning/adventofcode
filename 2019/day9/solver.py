def get_or_default(defaultdict, i):
    if i in defaultdict:
        return defaultdict[i]
    if i < 0:
        raise Exception("get negative index")
    return 0

def set_or_default(defaultdict, i, val):
    if i < 0:
        raise Exception("set negative index")
    defaultdict[i] = val

def find_output(opcodes, inp):
    ip = 0
    current_operand = opcodes[ip]
    relative_base = 0
    while current_operand != 99:
        current_operand = "{:05d}".format(current_operand)
        opcode1 = get_or_default(opcodes, ip+1)+relative_base if current_operand[-3] == "2" else ip+1 if current_operand[-3] == "1" else get_or_default(opcodes, ip+1)
        opcode2 = get_or_default(opcodes, ip+2)+relative_base if current_operand[-4] == "2" else ip+2 if current_operand[-4] == "1" else get_or_default(opcodes, ip+2)
        opcode3 = get_or_default(opcodes, ip+3)+relative_base if current_operand[-5] == "2" else ip+3 if current_operand[-5] == "1" else get_or_default(opcodes, ip+3)
        if current_operand[-1] == "1":
            set_or_default(opcodes, opcode3, get_or_default(opcodes, opcode1)+get_or_default(opcodes, opcode2))
            ip += 4
        elif current_operand[-1] == "2":
            set_or_default(opcodes, opcode3, get_or_default(opcodes, opcode1)*get_or_default(opcodes, opcode2))
            ip += 4
        elif current_operand[-1] == "3":
            set_or_default(opcodes, opcode1, inp)
            ip += 2
        elif current_operand[-1] == "4":
            print(get_or_default(opcodes, opcode1))
            ip += 2
        elif current_operand[-1] == "5":
            ip = ip + 3 if get_or_default(opcodes, opcode1) == 0 else get_or_default(opcodes, opcode2)
        elif current_operand[-1] == "6":
            ip = ip + 3 if get_or_default(opcodes, opcode1) != 0 else get_or_default(opcodes, opcode2)
        elif current_operand[-1] == "7":
            set_or_default(opcodes, opcode3, 1 if get_or_default(opcodes, opcode1) < get_or_default(opcodes, opcode2) else 0)
            ip += 4
        elif current_operand[-1] == "8":
            set_or_default(opcodes, opcode3, 1 if get_or_default(opcodes, opcode1) == get_or_default(opcodes, opcode2) else 0)
            ip += 4
        elif current_operand[-1] == "9":
            relative_base += get_or_default(opcodes, opcode1)
            ip += 2
        current_operand = get_or_default(opcodes, ip)
    return 0


if __name__ == "__main__":
    opcodes = {}
    for i, v in enumerate(open("input.txt").read().strip().split(",")):
        opcodes[i] = int(v)
    print(find_output(opcodes, 2))


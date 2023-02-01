def search_terminate(ip, acc, instructions, swapped, visited, endip):
    if ip in visited:
        return 1, acc
    if ip == endip:
        return 0, acc
    opcode, operand = instructions[ip].split()
    if opcode == "acc":
        return search_terminate(ip+1, acc+int(operand), instructions, swapped, visited+[ip], endip)
    elif opcode == "nop":
        if not swapped:
            status_code, acc_tmp = search_terminate(ip+int(operand), acc, instructions, True, visited+[ip], endip)
            if status_code == 0:
                print(ip)
                return 0, acc_tmp
        return search_terminate(ip+1, acc, instructions, swapped, visited+[ip], endip)
    else:
        if not swapped:
            status_code, acc_tmp = search_terminate(ip+1, acc, instructions, True, visited+[ip], endip)
            if status_code == 0:
                return 0, acc_tmp
        return search_terminate(ip+int(operand), acc, instructions, swapped, visited+[ip], endip)
    return 2, "Should never get to the bottom"

if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    visited = []
    ip = acc = 0
    status_code, acc = search_terminate(ip, acc, instructions, False, visited, len(instructions))
    print(acc)


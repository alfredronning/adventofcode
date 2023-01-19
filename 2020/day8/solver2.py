def search_terminate(ip, acc, instructions, swapped, visited, endip):
    if ip in visited:
        return 1, acc
    if ip == endip:
        return 0, acc
    opcode, operand = instructions[ip].split()
    if ip == 79 and search_terminate(ip+1, acc+int(operand), instructions, swapped, visited+[ip], endip)[0] == 0:
        print("break")
    if ip == 249 and search_terminate(ip+int(operand), acc, instructions, swapped, visited+[ip], endip)[0] == 0:
        print("break2")
    if opcode == "acc":
        return search_terminate(ip+1, acc+int(operand), instructions, swapped, visited+[ip], endip)
    elif opcode == "nop":
        if not swapped:
            status_code, acc = search_terminate(ip+int(operand), acc, instructions, True, visited+[ip], endip)
            if status_code == 0:
                print(ip)
                return 0, acc
        return search_terminate(ip+1, acc, instructions, swapped, visited+[ip], endip)
    else:
        if not swapped:
            status_code, acc = search_terminate(ip+1, acc, instructions, True, visited+[ip], endip)
            if status_code == 0:
                print(ip)
                return 0, acc
        return search_terminate(ip+int(operand), acc, instructions, swapped, visited+[ip], endip)
    return 2, "Should never get to the bottom"

if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    visited = []
    ip = acc = 0
    status_code, acc = search_terminate(ip, acc, instructions, False, visited, len(instructions))
    print(status_code, acc)


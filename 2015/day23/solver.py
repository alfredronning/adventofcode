if __name__ == "__main__":
    instructions = [row.replace(",", "").split() for row in open("input.txt").read().strip().split("\n")]
    memory = {"a": 1, "b": 0}
    ip = 0
    while ip < len(instructions):
        current_instruction = instructions[ip]
        ip += 1
        if current_instruction[0] == "hlf":
            memory[current_instruction[1]] //= 2
        elif current_instruction[0] == "tpl":
            memory[current_instruction[1]] *= 3
        elif current_instruction[0] == "inc":
            memory[current_instruction[1]] += 1
        elif current_instruction[0] == "jmp":
            ip += int(current_instruction[1]) - 1
        elif current_instruction[0] == "jie":
            if memory[current_instruction[1]] % 2 == 0:
                ip += int(current_instruction[2]) - 1
        elif current_instruction[0] == "jio":
            if memory[current_instruction[1]] == 1:
                ip += int(current_instruction[2]) - 1
    print(memory["b"])

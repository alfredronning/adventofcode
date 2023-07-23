if __name__ == "__main__":
    instructions = [int(i) for i in open("input.txt").read().strip().split("\n")]
    ip = 0
    steps = 0
    while ip >= 0 and ip < len(instructions):
        steps += 1

        next_ip = ip + instructions[ip]
        instructions[ip] += (1 if instructions[ip] < 3 else -1)
        ip = next_ip
    print(steps)


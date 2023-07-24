if __name__ == "__main__":
    program_list = open("input.txt").read().strip().split("\n")

    tree = {}
    non_root = set()

    for program_line in program_list:
        program = program_line.split(" -> ")[0]
        hold_up = program_line.split(" -> ")[1] if " -> " in program_line else ""
        program_name, program_weight = program.replace("()", "").split()
        tree[program_name] = (int(program_weight[1:-1]), [p for p in hold_up.split(", ")])
        for p in hold_up.split(", "):
            non_root.add(p)

    for p in tree:
        if p not in non_root:
            print(p)
            break
    

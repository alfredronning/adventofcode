def find_max(ports, current, visited, strenght):
    non_visited = [p for p in ports if p not in visited]
    compatible_ports = [p for p in non_visited if p[0] == current or p[1] == current]
    if not compatible_ports:
        return strenght
    max_strength = 0
    for compatible_port in compatible_ports:
        next_val = compatible_port[0] if compatible_port[1] == current else compatible_port[1]
        next_strength = strenght + sum(compatible_port)
        current_strength = find_max(ports, next_val, visited+[compatible_port], next_strength)
        max_strength = max(max_strength, current_strength)
    return max_strength


if __name__ == "__main__":
    ports = [tuple(int(i) for i in p.split("/")) for p in open("input.txt").read().strip().split("\n")]

    print(find_max(ports, 0, [], 0))


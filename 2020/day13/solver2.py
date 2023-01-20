if __name__ == "__main__":
    busses = open("input.txt").read().strip().split("\n")[1]
    current_num = 0
    current_gcd = 1
    for i, bus in enumerate(busses.split(",")):
        if bus == "x":
            continue
        while (current_num+i) % int(bus) != 0:
            current_num += current_gcd
        current_gcd *= int(bus)

    print(current_num)

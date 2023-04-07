if __name__ == "__main__":
    modules = [int(i) for i in open("input.txt").read().strip().split("\n")]
    total_fuel = 0
    for module in modules:
        while module > 0:
            module = module//3-2
            if module > 0:
                total_fuel += module
    print(total_fuel)


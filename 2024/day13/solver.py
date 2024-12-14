machines = open("input.txt").read().strip().split("\n\n")

DECIMAL_CHECK = 2

def solve_machine(a, b, price):
    # x1 * a[0] + x2 * b[0] = price[0]
    # x1 * a[1] + x2 * b[1] = price[1]
    # x1 = (price[0] - x2 * b[0]) / a[0]
    # (price[0] - x2 * b[0]) / a[0] * a[1] + x2*b[1] = price[1]
    # price[0] * a[1] / a[0] - x2 * b[0] * a[1] / a[0] + x2 * b[1] = price[1]
    # x2 * b[1] - x2 * b[0] * a[1] / a[0] = price[1] - price[0] * a[1] / a[0]
    x2 = (price[1] * a[0] - price[0] * a[1]) / (b[1] * a[0] - b[0] * a[1])
    x1 = (price[0] - x2 * b[0]) / a[0]
    if int(x2*(10**DECIMAL_CHECK))-int(x2)*(10**DECIMAL_CHECK) == 0 and int(x1*(10**DECIMAL_CHECK))-int(x1)*(10**DECIMAL_CHECK) == 0:
        return 3*x1 + x2
    return 0

res = 0

def carve_coords(line):
    line = line.split("X")[1][1:]
    x, rest = line.split(", Y")
    return (int(x), int(rest[1:]))


for machine in machines:
    a, b, price = machine.split("\n")
    res += solve_machine(carve_coords(a), carve_coords(b), carve_coords(price))
print(int(res))
    

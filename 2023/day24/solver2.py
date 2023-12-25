from sympy import symbols, solve

def find_all_intersects(hails):
    # x + t1 * dx = x1 + t1 * dx1
    # x + t2 * dx = x2 + t2 * dx2
    # x + t3 * dx = x3 + t3 * dx3
    # y + t1 * dy = y1 + t1 * dy1
    # y + t2 * dy = y2 + t2 * dy2
    # y + t3 * dy = y3 + t3 * dy3
    # z + t1 * dz = z1 + t1 * dz1
    # z + t2 * dz = z2 + t2 * dz2
    # z + t3 * dz = z3 + t3 * dz3
    # 9 equations 9 variables
    # too much to solve by hand
    x, y, z, dx, dy, dz, t1, t2, t3 = symbols("x, y, z, dx, dy, dz, t1, t2, t3") #type: ignore
    t = [t1, t2, t3]
    eqs = []
    for i in range(3):
        pos, vel = hails[i]
        x0 = pos[0]+t[i]*vel[0]-x-t[i]*dx
        y0 = pos[1]+t[i]*vel[1]-y-t[i]*dy
        z0 = pos[2]+t[i]*vel[2]-z-t[i]*dz
        eqs.append(x0)
        eqs.append(y0)
        eqs.append(z0)
    res = solve(eqs, x, y, z, dx, dy, dz, t1, t2, t3)[0]
    return res[0]+res[1]+res[2]


if __name__ == "__main__":
    hails = [([int(i) for i in h.split(" @ ")[0].split(", ")], [int(i) for i in h.split(" @ ")[1].split(", ")])
              for h in open("input.txt").read().strip().split("\n")]
    print(find_all_intersects(hails))

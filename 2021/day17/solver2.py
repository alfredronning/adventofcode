if __name__ == "__main__":
    _, x, y = open("input.txt").read().strip().split("=")
    xmin, xmax = (int(i) for i in x.split(", ")[0].split(".."))
    ymin, ymax = (int(i) for i in y.split(".."))

    x_closest = xmin if abs(xmin) < abs(xmax) else xmax
    y_closest = ymin if abs(ymin) < abs(ymax) else ymax
    x_furthest = xmax if abs(xmin) < abs(xmax) else xmin
    y_furthest = ymax if abs(ymin) < abs(ymax) else ymin


    if 0 in range(ymin, ymax+1):
        raise Exception("Infinite amount of configurations")

    # starts with 1 more speed on the way down than up.
    y_max_velocity = max(abs(ymin + (1 if ymin < 0 else 0)), abs(ymax))
    x_max_velocity = max(abs(xmin + (1 if ymax < 0 else 0)), abs(xmax))

    # solve sum 1..n == xmin, n(n+1)/2 = xmin
    # if sum 1..n < xmin, the velocity will become 0 before it reaches
    x_min_velocity = int(-((1 - (1 + 8*abs(x_closest))**0.5)//2)) * (1 if x_closest >=0 else -1)

    # the entire trench is either over or under y = 0, or the exception is raised
    if ymin < 0:
        y_min_velocity = -y_max_velocity-1
    else:
        y_min_velocity = int(-(1 - (1 + 8*abs(y_closest))**0.5)//2)

    # couldn't think of constant way to solve the count
    count = 0
    for x_velocity in range(x_min_velocity, x_max_velocity+1):
        for y_velocity in range(y_min_velocity, y_max_velocity+1):
            dx, dy = x_velocity, y_velocity
            x_current = 0
            y_current = 0
            while x_current <= x_furthest and y_current >= y_furthest:
                x_current += dx
                y_current += dy
                dx -= (1 if dx else 0)
                dy -= 1
                if x_current>=xmin and x_current<=xmax and y_current>=ymin and y_current<=ymax:
                    count += 1
                    break
    print(count)


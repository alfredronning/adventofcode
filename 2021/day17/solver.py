if __name__ == "__main__":
    _, _, y = open("input.txt").read().strip().split("=")
    ymin, ymax = (int(i) for i in y.split(".."))

    # starts with 1 more speed on the way down than up.
    ymin += 1 if ymin < 0 else 0
    ymax += 1 if ymax < 0 else 0

    # max y_velocity is inf if 0 is in the y range.
    # it will always pass 0, no mather how hard you shoot it.
    if 0 in range(ymin, ymax+1):
        raise Exception("Infinite y_height")

    # max y_velocity when it reaches the end of the area 1
    # timestep after starting or passing 0.
    y_max_velocity = max(abs(ymin), abs(ymax))
    y_height = (y_max_velocity+1)/2*y_max_velocity
    print(int(y_height))


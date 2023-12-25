def trace_intersects(hail1, hail2, mi, ma):
    pos1, vel1 = hail1
    pos2, vel2 = hail2
    x1, y1, _ = pos1
    x2, y2, _ = pos2
    dx1, dy1, _ = vel1
    dx2, dy2, _ = vel2
    # x1+t1*dx1 = x2+t2*dx2
    # y1+t1*dy1 = y2+t2*dy2
    # t1 = (y2-y1+t2*dy2)/dy1
    # x1+(y2-y1+t2*dy2)/dy1*dx1 = x2+t2*dx2
    # (y2-y1+t2*dy2)/dy1*dx1 = x2-x1+t2*dx2
    # (y2-y1)*dx1/dy1+t2*dy2*dx1/dy1 = x2-x1+t2*dx2
    # t2*dy2*dx1/dy1-t2*dx2 = x2-x1-(y2-y1)*dx1/dy1
    # t2*(dy2*dx1/dy1-dx2) = x2-x1-(y2-y1)*dx1/dy1
    # t2 = (x2-x1-(y2-y1)*dx1/dy1)/(dy2*dx1/dy1-dx2)
    if (dy2*dx1/dy1-dx2) == 0:
        return False
    t2 = (x2-x1-(y2-y1)*dx1/dy1)/(dy2*dx1/dy1-dx2)
    t1 = (x2-x1+t2*dx2)/dx1
    intersect_x = x2+t2*dx2
    intersect_y = y2+t2*dy2
    if intersect_x < mi or intersect_x > ma:
        return False
    if intersect_y < mi or intersect_y > ma:
        return False
    if t1 < 0 or t2 < 0:
        return False
    return True


if __name__ == "__main__":
    hails = [([int(i) for i in h.split(" @ ")[0].split(", ")], [int(i) for i in h.split(" @ ")[1].split(", ")])
              for h in open("input.txt").read().strip().split("\n")]
    intersections = 0
    mi, ma = 7, 27
    mi, ma = 200000000000000, 400000000000000
    for i, hail in enumerate(hails):
        for other in hails[i+1:]:
            if trace_intersects(hail, other, mi, ma):
                intersections += 1
    print(intersections)


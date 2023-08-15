def manhattan_distance(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2])+abs(p1[3]-p2[3])

if __name__ == "__main__":
    points = [tuple(int(i) for i in row.split(",")) for row in open("input.txt").read().strip().split("\n")]
    constallations = []
    for point in points:
        point_constallation = None
        for constallation in constallations:
            if point in constallation:
                point_constallation = constallation
                break
        for other_point in points:
            if point == other_point or manhattan_distance(point, other_point) > 3:
                continue
            if point_constallation is not None and other_point in point_constallation:
                continue
            other_point_constallation = None
            for constallation in constallations:
                if other_point in constallation:
                    other_point_constallation = constallation
                    break
            if point_constallation is None and other_point_constallation is None:
                point_constallation = {point, other_point}
                constallations.append(point_constallation)
            elif point_constallation is None and other_point_constallation is not None:
                point_constallation = other_point_constallation
                other_point_constallation.add(point)
            elif point_constallation is not None and other_point_constallation is None:
                point_constallation.add(other_point)
            else:
                point_constallation.update(other_point_constallation)
                constallations.remove(other_point_constallation)
    res = len(constallations)
    for point in points:
        if not any(point in constallation for constallation in constallations):
            res += 1
    print(res)


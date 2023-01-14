from collections import defaultdict, Counter

Z_ORIENTATIONS = [
    lambda point: point,
    lambda point: (point[0], -point[1], -point[2]),
    lambda point: (-point[2], point[1], point[0]),
    lambda point: (point[2], point[1], -point[0]),
    lambda point: (point[0], -point[2], point[1]),
    lambda point: (point[0], point[2], -point[1]),
]

XY_ORIENTATIONS = [
    lambda point: point,
    lambda point: (-point[0], -point[1], point[2]),
    lambda point: (point[1], -point[0], point[2]),
    lambda point: (-point[1], point[0], point[2]),
]

def find_relative_position(scanner1, scanner2):
    for z_orientation in Z_ORIENTATIONS:
        z_diff_beacons = defaultdict(lambda: ([], []))
        for beacon1 in scanner1:
            for beacon2 in scanner2:
                beacon2 = z_orientation(beacon2)
                z_diff = beacon1[2] - beacon2[2]
                z_diff_beacons[z_diff][0].append(beacon1)
                z_diff_beacons[z_diff][1].append(beacon2)
        beacons_over_12z = [(z_diff, z_diff_beacons[z_diff][0], z_diff_beacons[z_diff][1]) for z_diff in z_diff_beacons
                            if len(z_diff_beacons[z_diff][0]) >= 12]
        # continue if < 12 points with same relative z_diff
        if not beacons_over_12z:
            continue
        for z_diff, beacons1, beacons2 in beacons_over_12z:
            for xy_orientation in XY_ORIENTATIONS:
                y_diff_beacons = defaultdict(lambda: ([], []))
                for beacon1 in beacons1:
                    for beacon2 in beacons2:
                        beacon2 = xy_orientation(beacon2)
                        y_diff = beacon1[1] - beacon2[1]
                        y_diff_beacons[y_diff][0].append(beacon1)
                        y_diff_beacons[y_diff][1].append(beacon2)
                beacons_over_12y = [(y_diff, y_diff_beacons[y_diff][0], y_diff_beacons[y_diff][1]) for z_diff in
                                    y_diff_beacons if len(y_diff_beacons[z_diff][0]) >= 12]
                # continue if < 12 points with same relative z_diff and y diff
                if not beacons_over_12y:
                    continue
                for y_diff, beacons1, beacons2 in beacons_over_12y:
                    x_diff_beacons = Counter()
                    for beacon1 in beacons1:
                        for beacon2 in beacons2:
                            x_diff = beacon1[0] - beacon2[0]
                            if x_diff_beacons[x_diff] == 11:
                                scanner2pos = x_diff, y_diff, z_diff
                                return True, scanner2pos, correct_points(scanner2, scanner2pos, z_orientation, xy_orientation)
                            x_diff_beacons[x_diff] += 1
    return False, None, None

def correct_points(scanner, position, z_orientation, xy_orentation):
    res = []
    for point in scanner:
        point = xy_orentation(z_orientation(point))
        res.append((point[0]+position[0], point[1]+position[1], point[2]+position[2]))
    return res

if __name__ == "__main__":
    scanners = open("input.txt").read().strip().split("\n\n")
    scanners = [[tuple(int(coord) for coord in beacon.split(",")) for beacon in scanner.split("\n")[1:]] for scanner in scanners]
    found_locations = [0]
    check_pointer = 0
    positions = [None]*len(scanners)
    positions[0] = (0, 0, 0)
    while len(scanners) > len(found_locations) > check_pointer:
        id1 = found_locations[check_pointer]
        check_pointer += 1
        for id2 in range(len(scanners)):
            if id2 in found_locations:
                continue
            found, position, new_points = find_relative_position(scanners[id1], scanners[id2])
            if found:
                found_locations.append(id2)
                scanners[id2] = new_points
                positions[id2] = position
    #part1
    beacons = set(point for scanner in scanners for point in scanner)
    print("Total beacons: " + str(len(beacons)))
    #part2
    maxdist = 0
    for i in range(len(scanners)):
        for j in range(i+1, len(scanners)):
            scanner1 = positions[i]
            scanner2 = positions[j]
            dist = abs(scanner1[0]-scanner2[0]) + abs(scanner1[1]-scanner2[1]) + abs(scanner1[2]-scanner2[2])
            maxdist = max(maxdist, dist)
    print("Max manhattan distance: " + str(maxdist))

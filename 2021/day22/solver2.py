import re

def updated_segment(new, old):
    xr_new, yr_new, zr_new = [r[:] for r in new]
    xr_old, yr_old, zr_old = [r[:] for r in old]
    # if no overlap return old segment
    if xr_new[0] > xr_old[1] or xr_new[1] < xr_old[0] or yr_new[0] > yr_old[1] or yr_new[1] < yr_old[0] \
            or zr_new[0] > zr_old[1] or zr_new[1] < zr_old[0]:
        return [old]

    # if old complete overlapped
    if xr_new[0] <= xr_old[0] and xr_new[1] >= xr_old[1] \
        and yr_new[0] <= yr_old[0] and yr_new[1] >= yr_old[1] \
            and zr_new[0] <= zr_old[0] and zr_new[1] >= zr_old[1]:
        return []

    old_segment_split = []
    # crop x
    if xr_old[0] <= xr_new[1] <= xr_old[1]:
        old_segment_split.append([[xr_new[1]+1, xr_old[1]], yr_old[:], zr_old])
        xr_old[1] = xr_new[1]
    if xr_old[0] <= xr_new[0] <= xr_old[1]:
        old_segment_split.append([[xr_old[0], xr_new[0]-1], yr_old[:], zr_old])
        xr_old[0] = xr_new[0]
    # crop y
    if yr_old[0] <= yr_new[1] <= yr_old[1]:
        old_segment_split.append([xr_old, [yr_new[1]+1, yr_old[1]], zr_old])
        yr_old[1] = yr_new[1]
    if yr_old[0] <= yr_new[0] <= yr_old[1]:
        old_segment_split.append([xr_old, [yr_old[0], yr_new[0]-1], zr_old])
        yr_old[0] = yr_new[0]
    # crop z
    if zr_old[0] <= zr_new[1] <= zr_old[1]:
        old_segment_split.append([xr_old, yr_old, [zr_new[1]+1, zr_old[1]]])
    if zr_old[0] <= zr_new[0] <= zr_old[1]:
        old_segment_split.append([xr_old, yr_old, [zr_old[0], zr_new[0]-1]])
    return old_segment_split

def update_set_with_new_segment(covered_segments, new_segment, on):
    new_covered_segments = []
    for old_segment in covered_segments:
        new_segments = updated_segment(new_segment, old_segment)
        for seg in new_segments:
            new_covered_segments.append(seg)
    if on:
        new_covered_segments.append(new_segment)
    return new_covered_segments

def find_on_switches(steps):
    covered_segments = []
    res = 0
    for on, new_segment in steps:
        covered_segments = update_set_with_new_segment(covered_segments, new_segment, on)
    for xr, yr, zr in covered_segments:
        res += (xr[1]-xr[0]+1)*(yr[1]-yr[0]+1)*(zr[1]-zr[0]+1)
    return res

if __name__ == "__main__":
    inp = open("input.txt").read().strip().split("\n")
    steps = []
    on_set = []
    for step in inp:
        match = re.findall(r"^(.*)\sx=(.*),y=(.*),z=(.*)", step)[0]
        on = True if match[0] == "on" else False
        coords = [[int(c) for c in point.split("..")] for point in match[1:]]
        steps.append((on, coords))
    print(find_on_switches(steps))

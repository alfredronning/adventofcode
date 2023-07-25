import re

if __name__ == "__main__":
    particles_input = open("input.txt").read().strip().split("\n")
    particles = []

    for i in range(len(particles_input)):
        particles.append([tuple(int(i) for i in j[1:-1].split(",")) for j in re.findall(r"<[^<]*>", particles_input[i])])


    lowest_a = float("inf")
    lowest_v = float("inf")
    lowest_i = 0

    for i, (p, v, a) in enumerate(particles):
        current_a = (a[0]**2+a[1]**2+a[2]**2)**0.5
        current_v = (v[0]**2+v[1]**2+v[2]**2)**0.5
        if current_a <= lowest_a:
            if current_a == lowest_a:
                if current_v < lowest_v:
                    lowest_a = current_a
                    lowest_v = current_v
                    lowest_i = i
            else:
                lowest_a = current_a
                lowest_v = current_v
                lowest_i = i

    print(lowest_i)


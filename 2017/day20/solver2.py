from re import findall
from collections import defaultdict

if __name__ == "__main__":
    particles_input = open("input.txt").read().strip().split("\n")
    particles = []

    for i in range(len(particles_input)):
        particles.append([tuple(int(k) for k in j[1:-1].split(",")) for j in findall(r"<[^<]*>", particles_input[i])])

    dead_particles = set()

    for _ in range(100):
        pos_dict = defaultdict(list)
        for i, (p, v, a) in enumerate(particles):
            if i in dead_particles:
                continue
            next_v = (v[0]+a[0], v[1]+a[1], v[2]+a[2])
            next_p = (p[0]+next_v[0], p[1]+next_v[1], p[2]+next_v[2])
            particles[i] = (next_p, next_v, a)
            pos_dict[next_p].append(i)
            if len(pos_dict[next_p]) > 1:
                dead_particles.update(pos_dict[next_p])
    print(len(particles)-len(dead_particles))


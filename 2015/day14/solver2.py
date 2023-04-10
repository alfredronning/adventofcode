import re

if __name__ == "__main__":
    reindeer_specs = open("input.txt").read().strip().split("\n")
    reindeers = {}
    for reindeer in reindeer_specs:
        groups = re.search("(.*) can fly (.*) km/s for (.*) sec.*for (.*) sec.*", reindeer)
        reindeers[groups.group(1)] = (int(groups.group(2)), int(groups.group(3)), int(groups.group(4)))
    scores = dict((reindeer, 0) for reindeer in reindeers)
    distances = dict((reindeer, 0) for reindeer in reindeers)
    resting = dict((reindeer, False) for reindeer in reindeers)

    for s in range(1, 2504):
        for reindeer in reindeers:
            speed, fly_time, rest_time = reindeers[reindeer]
            if resting[reindeer]:
                if s%(fly_time+rest_time) == 0:
                    resting[reindeer] = False
            else:
                distances[reindeer] += speed
                if (s-fly_time)%(fly_time+rest_time) == 0:
                    resting[reindeer] = True
        leader = max(distances.values())
        for reindeer in reindeers:
            if distances[reindeer] == leader:
                scores[reindeer] += 1
    print(max(scores.values()))


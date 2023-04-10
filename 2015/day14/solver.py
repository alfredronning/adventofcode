import re

if __name__ == "__main__":
    reindeer_specs = open("input.txt").read().strip().split("\n")
    reindeers = {}
    for reindeer in reindeer_specs:
        groups = re.search("(.*) can fly (.*) km/s for (.*) sec.*for (.*) sec.*", reindeer)
        reindeers[groups.group(1)] = (int(groups.group(2)), int(groups.group(3)), int(groups.group(4)))
    res = 0
    for reindeer in reindeers:
        speed, fly_time, rest_time = reindeers[reindeer]
        time_remainding = 2503
        distance_traveled = 0
        while time_remainding > 0:
            if fly_time <= time_remainding:
                distance_traveled += speed * fly_time
                time_remainding -= fly_time + rest_time
            else:
                distance_traveled += speed * time_remainding
                time_remainding = 0
        res = max(res, distance_traveled)
    print(res)


class Valve:
    def __init__(self, valve):
        self.name = valve[6:8]
        self.bit = 0
        self.flow_rate = int(valve.split("=")[1].split(";")[0])
        self.neighbours = "".join(valve.split("to valv")[1].split()[1:]).split(",")
        self.distances = {}

    def calc_distances(self, valve_map):
        valve_queue = [(self, 0)]
        visited = [self.name]
        while valve_queue:
            current, current_time = valve_queue[0]
            valve_queue = valve_queue[1:]
            if current.name not in self.distances:
                self.distances[current.name] = current_time
            for neighbour in current.neighbours:
                if neighbour not in visited:
                    valve_queue.append((valve_map[neighbour], current_time+1))
                    visited.append(neighbour)

def dfs(current, valves, visited, time, res, pressure):
    if visited in res:
        res[visited] = max(res[visited], pressure)
    else:
        res[visited] = pressure
    for valve_next in valves:
        valve_next_time = time - current.distances[valve_next.name] - 1
        if valve_next_time > 0 and not valve_next.bit & visited:
            dfs(valve_next, valves, visited | valve_next.bit, valve_next_time, res, valve_next.flow_rate*valve_next_time + pressure)


if __name__ == "__main__":
    total_time = 26
    scan = open("input.txt").read().strip().split("\n")
    valves = [Valve(valve) for valve in scan]
    valve_map = dict((v.name, v) for v in valves)
    current = valve_map["AA"]
    for i, valve in enumerate(valves):
        valve.calc_distances(valve_map)
    res = {}
    valves = [v for v in valves if v.flow_rate]
    for i, v in enumerate(valves):
        v.bit = 1 << i
    dfs(current, valves, 0, total_time, res, 0)
    print(max(res[b1] + res[b2] for b1 in res for b2 in res if not b1 & b2))

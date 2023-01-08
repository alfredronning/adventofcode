class Valve:
    def __init__(self, valve):
        self.name = valve[6:8]
        self.flow_rate = int(valve.split("=")[1].split(";")[0])
        self.neighbours = "".join(valve.split("to valv")[1].split()[1:]).split(",")
        self.distances = {}

    def calc_distances(self, valvemap):
        valve_queue = [(self, 0)]
        visited = [self.name]
        while valve_queue:
            current, current_time = valve_queue[0]
            valve_queue = valve_queue[1:]
            visited.append(current.name)
            if current.name not in self.distances:
                self.distances[current.name] = current_time
            for neighbour in current.neighbours:
                if neighbour not in visited:
                    valve_queue.append((valvemap[neighbour], current_time+1))

def dfs(current, valvemap, visited, time):
    best_path = 0
    for valve in [v for v in valvemap.values() if v.name not in visited and current.distances[v.name] + 1 < time]:
        opening_path = dfs(valve, valvemap, visited+[valve.name], time-current.distances[valve.name]-1)
        if opening_path > best_path:
            best_path = opening_path
    return current.flow_rate*(time-1) + best_path


if __name__ == "__main__":
    total_time = 30
    scan = open("input.txt").read().strip().split("\n")
    valves = [Valve(valve) for valve in scan]
    valvemap = dict((v.name, v) for v in valves)
    for valve in valves:
        valve.calc_distances(valvemap)
    current = valvemap["AA"]
    if current.flow_rate == 0:
        total_time += 1
    print(dfs(current, valvemap, [valve.name for valve in valves if valve.flow_rate==0], total_time))


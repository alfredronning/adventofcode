if __name__ == "__main__":
    depart_time, busses = open("input.txt").read().strip().split("\n")
    depart_time = int(depart_time)
    busses = [int(bus) for bus in busses.split(",") if bus != "x"]
    shortest_wait = float("inf")
    shortest_bus = -1
    for bus in busses:
        waittime = -depart_time % bus
        if waittime < shortest_wait:
            shortest_wait = waittime
            shortest_bus = bus
    print(shortest_bus*shortest_wait)


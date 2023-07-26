def add_sleep_minutes(guard, sleep_minutes, sleep_start, sleep_end):
    if guard not in sleep_minutes:
        sleep = [0 for _ in range(100)]
    else:
        sleep = sleep_minutes[guard]
    for i in range(sleep_start, sleep_end):
        sleep[i] += 1
    sleep_minutes[guard] = sleep


if __name__ == "__main__":
    observations = sorted(open("input.txt").read().strip().split("\n"))
    sleep_minutes = {}
    current_guard = None
    sleep_start = None
    for observation in observations:
        timestamp, action = observation[1:].split("]")
        action = action.split()
        if action[0] == "Guard":
            current_guard = int(action[1][1:])
        elif action[1] == "asleep":
            sleep_start = int(timestamp.split()[1].split(":")[1])
        elif action[1] == "up":
            sleep_end = int(timestamp.split()[1].split(":")[1])
            add_sleep_minutes(current_guard, sleep_minutes, sleep_start, sleep_end)

    most_sleep = 0
    most_sleep_guard = None
    for guard in sleep_minutes:
        sleep = max(sleep_minutes[guard])
        if sleep > most_sleep:
            most_sleep = sleep
            most_sleep_guard = guard

    most_sleep_minute = sleep_minutes[most_sleep_guard].index(max(sleep_minutes[most_sleep_guard]))
    print(most_sleep_minute*most_sleep_guard)


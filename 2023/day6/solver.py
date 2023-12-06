if __name__ == "__main__":
    time, dist = [[int(i) for i in j.split(":")[1].split()] for j in open("input.txt").read().strip().split("\n")]
    res = 1
    for i in range(len(time)):
        ways = 0
        t, d = time[i], dist[i]
        for press in range(t):
            if press * (t-press) > d:
                ways += 1
        res *= ways
    print(res)
    

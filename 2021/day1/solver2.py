if __name__ == "__main__":
    measurements = [int(m) for m in open("input.txt").read().strip().split("\n")]
    print(sum((measurements[i] > measurements[i-3]) for i in range(3, len(measurements))))


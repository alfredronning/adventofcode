if __name__ == "__main__":
    adapters = [0]+sorted([int(i) for i in open("input.txt").read().strip().split("\n")])
    diff1 = 0
    diff3 = 1
    for i in range(len(adapters)-1):
        current_diff = adapters[i+1]-adapters[i]
        if current_diff == 1:
            diff1 += 1
        elif current_diff == 3:
            diff3 += 1
    print(diff1*diff3)
    

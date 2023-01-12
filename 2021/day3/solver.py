if __name__ == "__main__":
    report = open("input.txt").read().strip().split("\n")
    number = sum(2**i for i in range(len(report[0])) if sum(int(report[j][-i-1]) for j in range(len(report)))>len(report)//2)
    print(number * (number^2**(len(report[0]))-1))


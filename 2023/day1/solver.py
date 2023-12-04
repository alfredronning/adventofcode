if __name__ == "__main__":
    inp = open("input.txt").read().strip().split("\n")
    res = 0
    for line in inp:
        nums = "".join(c for c in line if c in "0123456789")
        res += int(nums[0] + nums[-1])
    print(res)


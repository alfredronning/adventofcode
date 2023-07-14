import re

if __name__ == "__main__":
    discs = open("input.txt").read().strip().split("\n")
    discs = [list((int(i) for i in re.search(r".* (\d*) .*n (\d*)", disc).groups())) for disc in discs]
    for i in range(len(discs)):
        discs[i][1] = (discs[i][1] + i + 1) % discs[i][0]
    
    i = 0
    while True:
        if all((disc[1]+i)%disc[0] == 0 for disc in discs):
            print(i)
            break
        i += 1


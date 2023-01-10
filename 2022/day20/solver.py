class N:
    def __init__(self, val):
        self.value = val

if __name__ == "__main__":
    f = [N(int(n)) for n in open("testinput.txt").read().strip().split("\n")]
    refs = f[:]
    l = len(f)
    for ref in refs:
        index = f.index(ref)
        n = f.pop(index)
        new_index = (n.value+index)%(l-1)
        if new_index == 0:
            new_index = l-1
        f.insert(new_index, n)
    f = [n.value for n in f]
    f_0 = f.index(0)
    print(f[(f_0+1000)%l] + f[(f_0+2000)%l] + f[(f_0+3000)%l])

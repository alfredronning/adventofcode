inp = open("input.txt").read().strip().split("\n")

res = 0

def can_produce(test, values, acc):
    if not len(values):
        return acc == test
    mult = can_produce(test, values[1:], acc*values[0])
    if mult:
        return True
    add = can_produce(test, values[1:], acc+values[0])
    if add:
        return True
    return can_produce(test, values[1:], int(str(acc)+str(values[0])))
    
for line in inp:
    test, values = line.split(": ")
    test = int(test)
    values = [int(v) for v in values.split()]
    if can_produce(test, values[1:], values[0]):
        res += test
print(res)



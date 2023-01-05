import ast
from functools import cmp_to_key

def cmp(left, right):
    if isinstance(left, int):
        if isinstance(right, int):
            return -1 if left < right else 1 if right < left else 0
        return cmp([left], right)
    if isinstance(right, int):
        return cmp(left, [right])
    for i in range(min(len(left), len(right))):
        current_cmp = cmp(left[i], right[i])
        if current_cmp != 0:
            return current_cmp
    if len(right) > len(left):
        return -1
    if len(left) > len(right):
        return 1
    return 0

if __name__ == "__main__":
    packets = open("input.txt").read().strip().replace("\n\n", "\n").split("\n")
    first, second = [[2]], [[6]]
    packets = [ast.literal_eval(packet) for packet in packets] + [first, second]
    packets.sort(key=cmp_to_key(cmp))

    print((packets.index(first)+1)*(packets.index(second)+1))


import ast

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

def right_order(packet_pair):
    left, right = packet_pair.split("\n")
    left, right = ast.literal_eval(left), ast.literal_eval(right)
    return cmp(left, right) <= 0

if __name__ == "__main__":
    packet_pairs = open("input.txt").read().strip().split("\n\n")
    print(sum(i+1 for i, packet_pair in enumerate(packet_pairs) if right_order(packet_pair)))


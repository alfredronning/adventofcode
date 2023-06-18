def group_ip(right):
    inner = []
    outer = []
    while "]" in right:
        left, right = right.split("[")[0], "[".join(right.split("[")[1:])
        mid, right = right.split("]")[0], "]".join(right.split("]")[1:])
        inner.append(mid)
        if len(left):
            outer.append(left)
    if len(right):
        outer.append(right)
    return inner, outer

def find_abas(group):
    abas = []
    for part in group:
        for i in range(len(part)-2):
            if part[i] == part[i+2] and part[i] != part[i+1]:
                abas.append(part[i:i+3])
    return abas

if __name__ == "__main__":
    ips = open("input.txt").read().strip().split("\n")
    ssl_count = 0
    for ip in ips:
        inner, outer = group_ip(ip)
        abas = find_abas(outer)
        for part in inner:
            if any(aba[1]+aba[0]+aba[1] in part for aba in abas):
                ssl_count += 1
                break
    print(ssl_count)


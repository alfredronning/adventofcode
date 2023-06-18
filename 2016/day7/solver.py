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

def supports_tls(ip):
    for i in range(len(ip)-3):
        if ip[i:i+2] == ip[i+2:i+4][::-1] and ip[i] != ip[i+1]:
            return True
    return False

if __name__ == "__main__":
    ips = open("input.txt").read().strip().split("\n")
    tls_count = 0
    for ip in ips:
        inner, outer = group_ip(ip)
        if any(supports_tls(o) for o in outer) and not any(supports_tls(i) for i in inner):
            tls_count += 1
    print(tls_count)


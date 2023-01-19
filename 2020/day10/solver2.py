from collections import defaultdict

if __name__ == "__main__":
    adapters = [0]+sorted([int(i) for i in open("input.txt").read().strip().split("\n")])
    adapter_count = defaultdict(int)
    adapter_count[0] = 1
    for i, adapter in enumerate(adapters):
        current_count = adapter_count[adapter]
        for j in range(1, 4):
            if adapter+j in adapters:
                adapter_count[adapter+j] += current_count
    print(max(adapter_count.values()))




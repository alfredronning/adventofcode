from collections import deque
from math import lcm

class Module:
    def __init__(self, module):
        name, out = module.split(" -> ")
        self.name = name[1:]
        self.type = name[0]
        self.prev = 0
        self.outputs = out.split(", ")
        self.inputs = dict()

    def recieve_input(self, inp_module, inp):
        if self.type == "%":
            if inp:
                return []
            self.prev = 0 if self.prev else 1
            return [(o, self.prev, self.name) for o in self.outputs]
        elif self.type == "&":
            self.inputs[inp_module] = inp
            signal = 0 if all(i == 1 for i in self.inputs.values()) else 1
            return [(o, signal, self.name) for o in self.outputs]
        else:
            return [(o, inp, self.name) for o in self.outputs]

def print_states(modules_map):
    for module in modules_map:
        if module in modules_map and modules_map[module].type == "&":
            k = " ".join(str(i) for i in modules_map[module].inputs.values())
            print(module, k)
    print()


def calc_lcm(modules_map):
    signals = deque()
    detected_cycle = [0, 0, 0, 0]
    for i in range(1000000):
        signals.append(("roadcaster", 0, None))
        while signals:
            module, signal, came_from = signals.popleft()
            if module == "dn":
                for j in range(len(detected_cycle)):
                    if detected_cycle[j]:
                        continue
                    if list(modules_map["dn"].inputs.values())[j] == 1:
                        detected_cycle[j] = i+1
                        print(detected_cycle)
                        if all(d != 0 for d in detected_cycle):
                            return lcm(*detected_cycle)
            if module not in modules_map:
                continue
            for o in modules_map[module].recieve_input(came_from, signal):
                signals.append(o)

if __name__ == "__main__":
    modules = open("input.txt").read().strip().split("\n")
    modules_map = dict()
    for module in modules:
        name, outputs = module.split(" -> ")
        modules_map[name[1:]] = Module(module)
    for module in modules:
        name, outputs = module.split(" -> ")
        for output in outputs.split(", "):
            if output in modules_map and modules_map[output].type == "&":
                modules_map[output].inputs[name[1:]] = 0
    print(calc_lcm(modules_map))




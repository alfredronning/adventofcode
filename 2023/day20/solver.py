from collections import deque

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

    signals = deque()
    signal_hight = 0
    signal_low = 0
    for _ in range(1000):
        signals.append(("roadcaster", 0, None))
        while signals:
            module, signal, came_from = signals.popleft()
            if signal == 0:
                signal_low += 1
            else:
                signal_hight += 1
            if module not in modules_map:
                continue
            for o in modules_map[module].recieve_input(came_from, signal):
                signals.append(o)
    print(signal_hight*signal_low)


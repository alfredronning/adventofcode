class Monkey:
    def __init__(self, monkeyid, items, operation, test, trueid, falseid):
        self.monkeyid = monkeyid
        self.items = [int(item) for item in items.split(": ")[1].split(", ")]
        self.operation = operation
        self.test = int(test.split()[-1])
        self.trueid = int(trueid.split()[-1])
        self.falseid = int(falseid.split()[-1])
        self.monkeybusiness = 0

    def apply_operation(self, old):
        operand = self.operation.split()[-1]
        if "*" in self.operation:
            return old*old if operand == "old" else old*int(operand)
        return old+old if operand == "old" else old+int(operand)

    def add_throwmonkeys(self, allmonkeys):
        self.truemonkey = allmonkeys[self.trueid]
        self.falsemonkey = allmonkeys[self.falseid]

    def inspect_items(self):
        for item in self.items:
            item = self.apply_operation(item)//3
            if item%self.test == 0:
                self.truemonkey.items.append(item)
            else:
                self.falsemonkey.items.append(item)
        self.monkeybusiness += len(self.items)
        self.items = []

    def __repr__(self):
        return "Monkey {}: {}".format(self.monkeyid, ", ".join(str(i) for i in self.items))

if __name__ == "__main__":
    monkeys = open("input.txt").read().strip().split("\n\n")
    monkey_obj = []
    for i, monkey in enumerate(monkeys):
        monkeyid, items, op, test, trueid, falseid = monkey.split("\n")
        monkey_obj.append(Monkey(i, items, op, test, trueid, falseid))
    for monkey in monkey_obj:
        monkey.add_throwmonkeys(monkey_obj)
    for r in range(20):
        for monkey in monkey_obj:
            monkey.inspect_items()
    res = 1
    for monkey in sorted(monkey_obj, key=lambda monkey: monkey.monkeybusiness)[-2:]:
        res *= monkey.monkeybusiness
    print(res)


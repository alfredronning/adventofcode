class Pair:
    def __init__(self, parent=None, is_left_ch=None):
        self.parent = parent
        self.is_left_ch = is_left_ch
        self.left = None
        self.right = None

    def depth(self):
        if self.parent is None:
            return 0
        return 1+self.parent.depth()

def explode(snailfish_node):
    left = snailfish_node.left
    right = snailfish_node.right
    is_left_ch = snailfish_node.is_left_ch
    snailfish_node = snailfish_node.parent
    if is_left_ch:
        snailfish_node.left = 0
        # add to right
        if type(snailfish_node.right) == int:
            snailfish_node.right += right
        else:
            right_node = snailfish_node.right
            while type(snailfish_node.left) != int:
                right_node = right_node.left
            right_node.left += right
        # add to left
        left_node = snailfish_node
        while left_node.is_left_ch:
            left_node = left_node.parent
            if left_node.parent is None:
                return
        if type(left_node.parent.left) == int:
            left_node.parent.left += left
            return
        left_node = left_node.parent.left
        while type(left_node.right) != int:
            left_node = left_node.right
        left_node.right += left
    else:
        snailfish_node.right = 0
        # add to left
        if type(snailfish_node.left) == int:
            snailfish_node.left += left
        else:
            left_node = snailfish_node.left
            while type(snailfish_node.right) != int:
                left_node = left_node.right
            left_node.right += left
        # add to right
        right_node = snailfish_node
        while not right_node.is_left_ch:
            right_node = right_node.parent
            if right_node.parent is None:
                return
        if type(right_node.parent.right) == int:
            right_node.parent.right += right
            return
        right_node = right_node.parent.right
        while type(right_node.left) != int:
            right_node = right_node.left
        right_node.left += right


def traverse_explode(snailfish_node):
    if type(snailfish_node.left) == int and type(snailfish_node.right) == int:
        if snailfish_node.depth() >= 4:
            explode(snailfish_node)
            return True
    if type(snailfish_node.left) != int:
        changed = traverse_explode(snailfish_node.left)
        if changed:
            return True
    if type(snailfish_node.right) != int:
        return traverse_explode(snailfish_node.right)
    return False

def traverse_split(snailfish_node):
    if type(snailfish_node.left) == int:
        if snailfish_node.left >= 10:
            new_left = Pair(snailfish_node)
            new_left.is_left_ch = True
            new_left.left = snailfish_node.left//2
            new_left.right = snailfish_node.left-new_left.left
            snailfish_node.left = new_left
            return True
    else:
        changed = traverse_split(snailfish_node.left)
        if changed:
            return True
    if type(snailfish_node.right) == int:
        if snailfish_node.right >= 10:
            new_right = Pair(snailfish_node)
            new_right.is_left_ch = False
            new_right.left = snailfish_node.right//2
            new_right.right = snailfish_node.right-new_right.left
            snailfish_node.right = new_right
            return True
        return False
    return traverse_split(snailfish_node.right)

def reduce_snailfish(snailfish_root):
    changed = True
    while changed:
        changed = traverse_explode(snailfish_root)
        if not changed:
            changed = traverse_split(snailfish_root)

def magnitude(snailfish_node):
    res = 0
    if type(snailfish_node.left) == int:
        res += 3*snailfish_node.left
    else:
        res += 3*magnitude(snailfish_node.left)
    if type(snailfish_node.right) == int:
        res += 2*snailfish_node.right
    else:
        res += 2*magnitude(snailfish_node.right)
    return res

def calc_snailfish(snailfish):
    while len(snailfish) > 1:
        first = snailfish.pop(0)
        second = snailfish.pop(0)
        new_root = Pair()
        first.is_left_ch = True
        first.parent = new_root
        new_root.left = first
        second.is_left_ch = False
        second.parent = new_root
        new_root.right = second
        reduce_snailfish(new_root)
        snailfish.insert(0, new_root)
    return magnitude(snailfish[0])

def parse_snailfish_pairs(snailfish_row):
    current = Pair()
    for c in snailfish_row:
        if c == "[":
            new_left = Pair(current, True)
            current.left = new_left
            current = new_left
        elif c == "]":
            if current.parent is not None:
                current = current.parent
        elif c == ",":
            new_right = Pair(current, False)
            current.right = new_right
            current = new_right
        elif c.isdigit():
            if current.is_left_ch:
                current = current.parent
                current.left = int(c)
            else:
                current = current.parent
                current.right = int(c)
    return current

if __name__ == "__main__":
    snailfish = open("input.txt").read().strip().split("\n")
    snailfish = [parse_snailfish_pairs(row) for row in snailfish]
    print(calc_snailfish(snailfish))


def find_closing_index(eq):
    opencount = 0
    for i, c in enumerate(eq):
        if c == ")":
            if opencount == 1:
                return i
            opencount -= 1
        elif c == "(":
            opencount += 1

def evaluate(eq):
    res = 0
    opmul = False
    i = 0
    while i < len(eq):
        if eq[i] == "*":
            opmul = True
        elif eq[i] == "+":
            opmul = False
        elif eq[i].isdigit():
            if opmul:
                res *= int(eq[i])
            else:
                res += int(eq[i])
        elif eq[i] == "(":
            indexof_close = find_closing_index(eq[i:])
            nextnum = evaluate(eq[i+1:i+indexof_close])
            if opmul:
                res *= nextnum
            else:
                res += nextnum
            i += indexof_close
        else:
            raise Exception(eq[i] + "is not handled")
        i += 1
    return res
            
if __name__ == "__main__":
    equations = [eq.replace(" ", "") for eq in open("input.txt").read().strip().split("\n")]
    print(sum(evaluate(eq) for eq in equations))


def execute_instructions(instructions, store, inp):
    for i, instruction in enumerate(instructions):
        if not i % 18:
            print("break")
        opcode, operand1, operand2 = instruction[0], instruction[1], instruction[-1]
        if opcode == "inp":
            store[operand1] = int(inp.pop(0))
        elif opcode == "add":
            if operand2.replace("-", "").isnumeric():
                store[operand1] += int(operand2)
            else:
                store[operand1] += store[operand2]
        elif opcode == "mul":
            if operand2.replace("-", "").isnumeric():
                store[operand1] *= int(operand2)
            else:
                store[operand1] *= store[operand2]
        elif opcode == "div":
            if operand2.replace("-", "").isnumeric():
                store[operand1] //= int(operand2)
            else:
                store[operand1] //= store[operand2]
        elif opcode == "mod":
            if operand2.replace("-", "").isnumeric():
                store[operand1] %= int(operand2)
            else:
                store[operand1] %= store[operand2]
        elif opcode == "eql":
            if operand2.replace("-", "").isnumeric():
                store[operand1] = 1 if store[operand1] == int(operand2) else 0
            else:
                store[operand1] = 1 if store[operand1] == store[operand2] else 0
        else:
            raise Exception("opcode {} not recognized".format(opcode))


SHORT = True


def instructions_summed(inp):
    inp = [int(n) for n in inp]

    # 9979 digit 1,2,3,4
    # Must go down to 5 to reach the first div
    # 9969 digit 5,6,7,8


    z = ((inp[0] + 7) * 26 + inp[1] + 4) * 26 + inp[2] + 8 # inp2 must be 7 to get in the first mod
    if z % 26 - 4 != inp[3]:
        z = z // 26 * 26 + inp[3] + 1
    else:
        z //= 26
    z = ((z * 26 + inp[4] + 5) * 26 + inp[5] + 14) * 26 + inp[6] + 12
    if z % 26 - 9 != inp[7]:
        z = z // 26 * 26 + inp[7] + 10
    else:
        z //= 26
    if z % 26 - 9 != inp[8]:
        z = z // 26 * 26 + inp[8] + 5
    else:
        z //= 26
    z = z * 26 + inp[9] + 7
    if z % 26 - 15 != inp[10]:
        z = z // 26 * 26 + inp[10] + 6
    else:
        z //= 26
    if z % 26 - 7 != inp[11]:
        z = z // 26 * 26 + inp[11] + 8
    else:
        z //= 26
    if z % 26 - 10 != inp[12]:
        z = z // 26 * 26 + inp[12] + 4
    else:
        z //= 26
    if z % 26 != inp[13]:
        z = z // 26 * 26 + inp[13] + 6
    else:
        z //= 26
    if SHORT:
        return z
    #
    #
    # # 0 digit
    # # w = inp[0]
    # # x = 1
    # # y = inp[0] + 7
    # z = inp[0] + 7 # 16
    #
    # # 1 digit
    # # w = inp[1]
    # # x = 1
    # # y = inp[1]+4
    # z = z*26 + inp[1] + 4 # 429
    #
    # # 2 digit
    # # w = inp[2]
    # # x = 1
    # # y = inp[2] + 8
    # z = 26*z+inp[2] + 8 # 11171
    #
    # # 3 digit
    # # w = inp[3]
    # z, x = divmod(z, 26)
    # x = (x-4) != inp[3]
    # z = 26*z if x else z
    # y = (inp[3] + 1)*x
    # z += y
    #
    # # 4 digit
    # # w = inp[4]
    # # x = 1
    # # y = inp[4] + 5
    # z = 26*z + inp[4] + 5
    #
    # # 5 digit
    # # w = inp[5]
    # # x = 1
    # # y = inp[5] + 14
    # z = 26*z + inp[5] + 14
    #
    # # 6 digit
    # # w = inp[6]
    # # x = 1
    # # y = inp[6] + 12
    # z = 26*z + inp[6] + 12
    #
    # # 7 digit
    # w = inp[7]
    # z, x = divmod(z, 26)
    # x = (x-9) != inp[7]
    # z = 26*z if x else z
    # y = (inp[7]+10)*x
    # z += y
    #
    # # 8 digit
    # w = inp[8]
    # z, x = divmod(z, 26)
    # x = (x-9) != inp[8]
    # z = 26*z if x else z
    # y = (inp[8]+5)*x
    # z += y
    #
    # # 9 digit
    # # w = inp[9]
    # # x = 1
    # # y = inp[9] + 12
    # z = 26*z + inp[9]+7
    #
    # # 10 digit
    # # w = inp[10]
    # z, x = divmod(z, 26)
    # x = (x-15) != inp[10]
    # z = 26*z if x else z
    # y = (inp[10]+6)*x
    # z += y
    #
    # # 11 digit
    # # w = inp[11]
    # z, x = divmod(z, 26)
    # x = (x-7) != inp[11]
    # z = 26*z if x else z
    # y = (inp[11]+8)*x
    # z += y
    #
    # # 12 digit
    # # w = inp[12]
    # z, x = divmod(z, 26)
    # x = (x-10) != inp[12]
    # z = 26*z if x else z
    # y = (inp[12]+4)*x
    # z += y
    #
    # # 13 digit
    # # w = inp[13]
    # z, x = divmod(z, 26)
    # x = x != inp[13]
    # z = 26*z if x else z
    # y = (inp[12]+6)*x
    # z += y
    #
    # return z

def valid_state(inp):
    if len(inp) < 4:
        return True
    z = ((inp[0] + 7) * 26 + inp[1] + 4) * 26 + inp[2] + 8 # inp2 must be 7 to get in the first mod
    if z % 26 - 4 != inp[3]:
        z = z // 26 * 26 + inp[3] + 1
        return False
    else:
        if len(inp) == 4:
            return True
        z //= 26
    if len(inp) < 8:
        return True
    z = ((z * 26 + inp[4] + 5) * 26 + inp[5] + 14) * 26 + inp[6] + 12
    if z % 26 - 9 != inp[7]:
        z = z // 26 * 26 + inp[7] + 10
        return False
    else:
        if len(inp) == 8:
            return True
        z //= 26
    if z % 26 - 9 != inp[8]:
        z = z // 26 * 26 + inp[8] + 5
        return False
    else:
        if len(inp) == 9:
            return True
        z //= 26
    if len(inp) == 10:
        return True
    z = z * 26 + inp[9] + 7
    if z % 26 - 15 != inp[10]:
        z = z // 26 * 26 + inp[10] + 6
        return False
    else:
        if len(inp) == 11:
            return True
        z //= 26
    if z % 26 - 7 != inp[11]:
        z = z // 26 * 26 + inp[11] + 8
        return False
    else:
        if len(inp) == 12:
            return True
        z //= 26
    if z % 26 - 10 != inp[12]:
        z = z // 26 * 26 + inp[12] + 4
        return False
    else:
        if len(inp) == 13:
            return True
        z //= 26
    if z % 26 != inp[13]:
        z = z // 26 * 26 + inp[13] + 6
        return False
    else:
        return True
        z //= 26

def dfs(numbers):
    valid = valid_state(numbers)
    if not valid:
        return False
    if len(numbers) == 14:
        print("".join(str(i) for i in numbers))
        return numbers
    res = []
    for next_num in range(9, 0, -1):
        res = dfs(numbers+[next_num])
        if res:
            return numbers+[next_num]
    return res

def dfs_reverse(numbers):
    valid = valid_state(numbers)
    if not valid:
        return False
    if len(numbers) == 14:
        print("".join(str(i) for i in numbers))
        return numbers
    res = []
    for next_num in range(1, 10):
        res = dfs_reverse(numbers+[next_num])
        if res:
            return res
    return res



# def find_next_nonzero(n):
#     n = [d for d in str(int("".join(n)) - 1)]
#     while n.count("0"):
#         position = n[::-1].index("0")
#         n = [d for d in str(int("".join(n)) - 10 ** position)]
#     return n


if __name__ == "__main__":
    instructions = [i.split("//")[0].split() for i in open("input.txt").read().strip().split("\n")]
    # dfs([])
    dfs_reverse([])

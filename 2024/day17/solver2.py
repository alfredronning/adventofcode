registers, program = open("input.txt").read().strip().split("\n\n")

a, b, c = [int(r.split(": ")[1]) for r in registers.split("\n")]
program = [int(i) for i in program.split(": ")[1].split(",")]
#program = [2,4, 1,1, 7,5, 1,5, 4,3, 0,3, 5,5, 3,0]

#while a != 0:
#    b = a%8
#    b = b^1
#    c = a // (2**b)
#    b = b^5
#    b = b^c
#    a = a // (2**3)
#    print(b%8)

#00000000XYZ
#(a >> XYz) ^ xYZ % 8 = program[i]

def find_bits(program, pinned, bits, pos, d):
    out = program[pos]
    pinned1 = pinned[:]
    bits1 = bits[:]
    for i in range(3):
        if pinned1[-pos*3-i-1] and bits1[-pos*3-i-1] != (d >> i) & 1:
            return False, pinned1, bits1
        pinned1[-pos*3-i-1] = True
        bits1[-pos*3-i-1] = bool((d >> i) & 1)
    shiftedbits = out ^ d ^ 0b100
    shifted_amount = d ^ 0b001
    for i in range(3):
        if pinned1[-pos*3-shifted_amount-i-1] and bits1[-pos*3-shifted_amount-i-1] != (shiftedbits >> i) & 1:
            return False, pinned1, bits1
        pinned1[-pos*3-shifted_amount-i-1] = True
        bits1[-pos*3-shifted_amount-i-1] = bool((shiftedbits >> i) & 1)
    return True, pinned1, bits1

def find_a(program, pinned, bits, pos, valid):
    if pos == len(program):
        valid.append(int("".join(str(int(i)) for i in bits), 2))
        return
    for d in range(8):
        is_valid, pinned1, bits1 = find_bits(program, pinned, bits, pos, d)
        if is_valid:
            find_a(program, pinned1, bits1, pos+1, valid)

size = len(program)*3
pinned = [False]*(size*2)
a_bits = [False]*(size*2)
valid = []
find_a(program, pinned, a_bits, 0, valid)
print(min(valid))


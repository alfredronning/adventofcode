VALUES = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}

def decode_snafu(snafu):
    decimal = 0
    for i, n in enumerate(snafu[::-1]):
        decimal += VALUES[n] * 5 ** i
    return decimal

def encode_snafu(decimal):
    snafu = ""
    while decimal:
        decimal, digit = divmod(decimal, 5)
        if digit % 5 < 3:
            snafu += str(digit)
        else:
            decimal += 1
            if digit % 5 == 3:
                snafu += "="
            else:
                snafu += "-"
    return snafu[::-1]

if __name__ == "__main__":
    snafu_numbers = open("input.txt").read().strip().split("\n")
    res = 0
    for snafu_number in snafu_numbers:
        res += decode_snafu(snafu_number)
    print(res)
    print(encode_snafu(res))

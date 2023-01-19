import string

REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]#, "cid"}

def valid_passport(passport):
    if not all(required_field in passport for required_field in REQUIRED_FIELDS):
        return False
    byr, iyr, eyr, hgt, hcl, ecl, pid = [passport[field] for field in REQUIRED_FIELDS]

    if not byr.isnumeric() or int(byr) < 1920 or int(byr) > 2002:
        return False
    if not iyr.isnumeric() or int(iyr) < 2010 or int(iyr) > 2020:
        return False
    if not eyr.isnumeric() or int(eyr) < 2020 or int(eyr) > 2030:
        return False
    if not (hgt[:-2].isnumeric() and hgt[-2:] in ["in", "cm"]) or not (150 <= int(hgt[:-2]) <= 193 if hgt[-2:] == "cm" else 59 <= int(hgt[:-2]) <= 76):
        return False
    if hcl[0] != "#" or len(hcl) != 7 or not all(c in string.hexdigits for c in hcl[1:]):
        return False
    if not ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if len(pid) != 9 or not pid.isnumeric():
        return False
    return True

if __name__ == "__main__":
    passports = open("input.txt").read().strip().split("\n\n")
    passports = [dict(field.split(":") for field in passport.replace("\n", " ").split()) for passport in passports]
    valid_passports = 0
    for passport in passports:
        valid_passports += valid_passport(passport)
    print(valid_passports)


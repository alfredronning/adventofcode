REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}#, "cid"}

def valid_passport(passport):
    for required_field in REQUIRED_FIELDS:
        if required_field not in passport:
            return False
    return True


if __name__ == "__main__":
    passports = open("input.txt").read().strip().split("\n\n")
    passports = [set(field.split(":")[0] for field in passport.replace("\n", " ").split()) for passport in passports]
    valid_passports = 0
    for passport in passports:
        valid_passports += valid_passport(passport)
    print(valid_passports)


import re

if __name__ == "__main__":
    sues = open("input.txt").read().strip().split("\n")
    gift = open("gift.txt").read().strip().split("\n")
    compund_dict = dict()
    for compound in gift:
        k, v = compound.split(": ")
        compund_dict[k] = v
    for sue in sues:
        groups = re.search("Sue (\d+): ([a-z]+): (\d+), ([a-z]+): (\d+), ([a-z]+): (\d+)", sue)
        sueid, compounds = groups.group(1), [groups.group(i+2) for i in range(6)]
        all_macth = True
        for compound_id in range(3):
            k, v = compounds[compound_id*2], compounds[compound_id*2+1]
            if compund_dict[k] != v:
                all_macth = False
                break
        if all_macth:
            print(sueid)



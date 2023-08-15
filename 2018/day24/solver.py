import re

class Group:
    def __init__(self, unit_type, id, init_text):
        self.unit_type = unit_type
        self.id = id
        got_effect = 1 if "(" in init_text else 0
        if got_effect:
            grps = re.search(r"(\d*) .* (\d*) .* \((.*)\) .* does (.*) at .* (\d*)", init_text).groups() #type: ignore
        else:
            grps = re.search(r"(\d*) .* (\d*) .* does (.*) at .* (\d*)", init_text).groups() #type: ignore
        self.units = int(grps[0])
        self.hp = int(grps[1])
        self.attack_dammage = int(grps[2+got_effect].split()[0]) # type: ignore
        self.dammage_type = grps[2+got_effect].split()[1]
        self.initiative = int(grps[3+got_effect])
        self.attack_target = None
        self.target_dammage = 0
        self.immune = []
        self.weakness = []
        if got_effect:
            for effect in grps[2].split("; "):
                if "weak" in effect:
                    self.weakness = effect.split(" to ")[1].split(", ")
                if "immune" in effect:
                    self.immune = effect.split(" to ")[1].split(", ")

    def find_target(self, remainding_groups):
        best_effective_power = 0
        self.attack_target = None
        self.target_dammage = 0
        for grp in remainding_groups:
            if self.unit_type == grp.unit_type:
                continue
            dammage_delt = grp.dammage(self.attack_dammage*self.units, self.dammage_type) # type: ignore
            effective_power = grp.attack_dammage*grp.units
            if dammage_delt < self.target_dammage or dammage_delt == 0:
                continue
            if dammage_delt > self.target_dammage:
                self.target_dammage = dammage_delt
                best_effective_power = effective_power
                self.attack_target = grp
                continue
            if effective_power < best_effective_power:
                continue
            if effective_power > best_effective_power:
                best_effective_power = effective_power
                self.attack_target = grp
                continue
            if grp.initiative > self.attack_target.initiative: #type: ignore
                self.attack_target = grp

    def dammage(self, attack_dammage, dammage_type):
        if dammage_type in self.immune:
            return 0
        elif dammage_type in self.weakness:
            return 2*attack_dammage
        return attack_dammage

    def attack(self, attack_dammage, dammage_type):
        self.units -= self.dammage(attack_dammage, dammage_type)//self.hp

    def dead(self):
        return self.units <= 0

if __name__ == "__main__":
    immune, infection = open("input.txt").read().strip().split("\n\n")
    testline = immune.split("\n")[1]

    immune_grps = []
    infection_grps = []
    for i, grp in enumerate(immune.split("\n")[1:]):
        immune_grps.append(Group("immune", i+1, grp))
    for i, grp in enumerate(infection.split("\n")[1:]):
        infection_grps.append(Group("infection", i+1, grp))

    dead_grps = set()
    while immune_grps and infection_grps:
        remainding_grps = immune_grps+infection_grps
        remainding_grps.sort(key=lambda g: (g.attack_dammage*g.units, g.initiative), reverse=True)
        taken = set()
        for grp in remainding_grps:
            grp.find_target([g for g in remainding_grps if g not in taken])
            taken.add(grp.attack_target)
        remainding_grps.sort(key=lambda g: g.initiative, reverse=True)
        for grp in remainding_grps:
            if grp.attack_target is None or grp in dead_grps:
                continue
            grp.attack_target.attack(grp.attack_dammage*grp.units, grp.dammage_type)
            if grp.attack_target.dead():
                dead_grps.add(grp.attack_target)
        immune_grps = [g for g in immune_grps if g not in dead_grps]
        infection_grps = [g for g in infection_grps if g not in dead_grps]
    print(sum(g.units for g in immune_grps+infection_grps if g not in dead_grps))


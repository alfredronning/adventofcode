print(sum(len([c for c in set(grp.replace("\n", "")) if all(c in p for p in grp.split("\n"))]) for grp in open("input.txt").read().strip().split("\n\n")))

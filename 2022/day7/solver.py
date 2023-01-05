class File():
    def __init__(self, parent, name, size=0):
        self.name = name
        self.subfiles = {"..": self if parent is None else parent}
        self.size = size

    def add_subfile(self, f):
        if f.name not in self.subfiles:
            self.subfiles[f.name] = f

    def getsize(self):
        return self.size if self.size else sum(f.getsize() for d, f in self.subfiles.items() if d != "..")
    
    def getpath(self):
        if self.subfiles[".."] == self:
            return self.name
        return self.subfiles[".."].getpath() + self.name + "/"

    def __repr__(self):
        return str(self.getsize())

def create_file_tree(console):
    dirs = {}
    cd = File(None, "/")
    dirs["/"] = cd
    pointer = 1
    while pointer < len(console):
        command = console[pointer]
        if command[:4] == "$ cd":
            cd = cd.subfiles[command[5:]]
            pointer += 1
        elif command[:4] == "$ ls":
            pointer += 1
            command = console[pointer]
            while command[0] != "$":
                typ, name = command.split()
                subfile = File(cd, name, 0 if typ == "dir" else int(typ))
                if typ == "dir":
                    dirs[subfile.getpath()] = subfile
                cd.add_subfile(subfile)
                pointer += 1
                if pointer >= len(console):
                    break
                command = console[pointer]
        else:
            raise Exception("invalid console output")
    return dirs

if __name__ == "__main__":
    console = open("input.txt").read().strip().split("\n")
    dirs = create_file_tree(console)
    print(sum(f.getsize() for f in dirs.values() if f.getsize() <= 100000))


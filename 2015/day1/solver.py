if __name__ == "__main__":
    inp = open("input.txt").read().strip()
    print(inp.count("(")-inp.count(")"))


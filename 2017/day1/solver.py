if __name__ == "__main__":
   inp = open("input.txt").read().strip()
   inp = inp+inp[0]

   print(sum(int(inp[i]) for i in range(len(inp)-1) if inp[i] == inp[i+1]))


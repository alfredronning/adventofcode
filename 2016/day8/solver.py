def rect(a, b, screen):
    for i in range(b):
        for j in range(a):
            screen[i][j] = 1

def rot_row(a, screen):
    last = screen[a][-1]
    for i in range(len(screen[a])-1, 0, -1):
        screen[a][i] = screen[a][i-1]
    screen[a][0] = last

def rot_col(a, screen):
    last = screen[-1][a]
    for i in range(len(screen)-1, 0, -1):
        screen[i][a] = screen[i-1][a]
    screen[0][a] = last

if __name__ == "__main__":
    instructions = open("input.txt").read().strip().split("\n")
    height, width = 6, 50
    screen = [[0]*width for _ in range(height)]
    for instruction in instructions:
        if "rect" in instruction:
            a, b = [int(i) for i in instruction.split()[1].split("x")]
            rect(a, b, screen)
        elif "row" in instruction:
            a, b = [int(i) for i in instruction.split("=")[1].split(" by ")]
            for _ in range(b):
                rot_row(a, screen)
        elif "col" in instruction:
            a, b = [int(i) for i in instruction.split("=")[1].split(" by ")]
            for _ in range(b):
                rot_col(a, screen)
    for row in screen:
        print("".join("#" if i == 1 else " " for i in row))


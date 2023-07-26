if __name__ == "__main__":
    serial = 8199
    size = 300

    cell_powers = {}
    for i in range(1, size+1):
        for j in range(1, size+1):
            rack_id = i+10
            power = rack_id*j+serial
            power *= rack_id
            cell_powers[(i, j)] = int(str(power)[-3])-5

    max_square = 0
    max_pos = None

    for i in range(1, size-1):
        for j in range(1, size-1):
            current_square = 0
            for k in range(3):
                for l in range(3):
                    current_square += cell_powers[(i+k, j+l)]
            if current_square > max_square:
                max_square = current_square
                max_pos = (i, j)
    print(max_pos)
    

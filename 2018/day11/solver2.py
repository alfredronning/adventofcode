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
            square_size = 1
            while i+square_size<=300 and j+square_size<=300 and square_size < 160:
                for k in range(square_size):
                    current_square += cell_powers[(i+k, j+square_size-1)]
                for k in range(square_size-1):
                    current_square += cell_powers[(i+square_size-1, j+k)]
                if current_square > max_square:
                    max_square = current_square
                    max_pos = (i, j, square_size)
                square_size += 1
    print(max_square)
    print(max_pos)
    

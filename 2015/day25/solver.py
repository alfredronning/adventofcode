if __name__ == "__main__":
    sol_row, sol_col = 2978, 3083
    sol_row, sol_col = float(sol_row), float(sol_col)
    first_col_index = sol_row/2*(sol_row-1)+1
    index = int(first_col_index + (sol_col-1) * (sol_col/2+sol_row))

    current = 20151125
    mult = 252533
    div = 33554393
    for _ in range(index-1):
        current = (current*mult)%div
    print(current)
    current = (current*mult)%div


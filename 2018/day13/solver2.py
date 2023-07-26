def check_collision(cart_pos):
    collision = []
    for cart1 in cart_pos:
        for cart2 in cart_pos:
            if cart1 == cart2:
                continue
            if cart_pos[cart1] == cart_pos[cart2]:
                collision.append(cart1)
    return collision


def simulate(board, cart_pos, cart_states, d):
    collision = set()
    sorted_carts = sorted(cart_pos, key=lambda c: cart_pos[c])
    for cart in sorted_carts:
        if cart in collision:
            continue
        x, y = cart_pos[cart]
        turn_state, direction = cart_states[cart]
        cart_pos[cart] = (x+d[direction][0], y+d[direction][1])
        x, y = cart_pos[cart]
        tile = board[x][y]
        if tile == "+":
            direction = (direction + (-1 if turn_state == 0 else 1 if turn_state == 2 else 0))%4
            turn_state = (turn_state+1)%3
        elif tile == "\\":
            direction = (direction + (-1 if direction == 0 or direction == 2 else 1))%4
        elif tile == "/":
            direction = (direction + (1 if direction == 0 or direction == 2 else -1))%4
        cart_states[cart] = (turn_state, direction)
        collision.update(check_collision(cart_pos))
    return set(collision)

if __name__ == "__main__":
    board = [[t for t in r] for r in open("input.txt").read().split("\n")]

    cart_states = {}
    cart_pos = {}
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
 
    cartid = 0
    for i, line in enumerate(board):
        for j, tile in enumerate(line):
            if tile == "^":
                cart_pos[cartid] = (i, j)
                cart_states[cartid] = (0, 0)
                cartid += 1
                board[i][j] = "|"
            if tile == ">":
                cart_pos[cartid] = (i, j)
                cart_states[cartid] = (0, 1)
                cartid += 1
                board[i][j] = "-"
            if tile == "v":
                cart_pos[cartid] = (i, j)
                cart_states[cartid] = (0, 2)
                cartid += 1
                board[i][j] = "|"
            if tile == "<":
                cart_pos[cartid] = (i, j)
                cart_states[cartid] = (0, 3)
                cartid += 1
                board[i][j] = "-"

    tick = 0
    while True:
        collision = simulate(board, cart_pos, cart_states, d)
        if collision:
            for c in collision:
                cart_pos.pop(c)
        if len(cart_pos) == 1:
            c = list(cart_pos)[0]
            print(str(cart_pos[c][1])+","+str(cart_pos[c][0]), tick)
            break
        tick += 1


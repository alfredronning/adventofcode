ENERGY_LEVELS = {"A": 1, "B": 10, "C": 100, "D": 1000}
ROOM_X_CORDS = {"A": 2, "B": 4, "C": 6, "D": 8}

class Boardstate:
    def __init__(self, rooms, hallway, energy):
        self.hallway = hallway
        self.rooms = rooms
        self.energy = energy
        self.h = -self.energy
        for room in self.rooms:
            amphoids = self.rooms[room]
            if len(amphoids) == 2:
                self.h += (100000 if amphoids[0] == room else -100000)
                self.h += (100000 if amphoids[1] == room else -100000)
            elif len(amphoids) == 1:
                self.h += (100000 if amphoids[0] == room else -100000)
                self.h += 20000
            else:
                self.h += 20000

    def is_over(self):
        if not all(spot == None for spot in self.hallway):
            return False
        for room in self.rooms:
            if not all(amphoid == room for amphoid in self.rooms[room]):
                return False
        return True

    def __hash__(self):
        hashstr = "".join("0" if spot is None else spot for spot in self.hallway)
        for room in self.rooms.values():
            if len(room) == 0:
                hashstr += "00"
            elif len(room) == 1:
                hashstr += "0" + room[0]
            else:
                hashstr += room[1] + room[0]
        return hashstr
        # return hash(str(self.rooms)+str(self.hallway))

    def get_next_states(self):
        next_states = []
        # next states for moving amhpid back
        for i, amphoid in enumerate(self.hallway):
            if amphoid is None:
                continue
            destination_room = self.rooms[amphoid]
            room_exit = ROOM_X_CORDS[amphoid]
            if any(room_amhoid != amphoid for room_amhoid in destination_room):
                continue
            startx = i+1 if i < room_exit else room_exit
            endx = room_exit if i < room_exit else i-1
            if any(self.hallway[spot] is not None for spot in range(startx, endx+1)):
                continue
            next_energy = self.energy + (abs(i-room_exit) + 2 - len(destination_room))*ENERGY_LEVELS[amphoid]
            next_rooms = self.rooms.copy()
            next_rooms[amphoid] = next_rooms[amphoid] + [amphoid]
            next_hallway = [None if j == i else h for j, h in enumerate(self.hallway)]
            next_states.append(Boardstate(next_rooms, next_hallway, next_energy))

        # next states for moving amhoid out
        for room in self.rooms:
            room_exit = ROOM_X_CORDS[room]
            if all(amphoid == room for amphoid in self.rooms[room]):
                continue
            top_amphoid = self.rooms[room][-1]
            for i, hallwayspot in enumerate(self.hallway):
                if i in ROOM_X_CORDS.values():
                    continue
                startx = min(i, room_exit)
                endx = max(i, room_exit)
                if any(self.hallway[spot] is not None for spot in range(startx, endx+1)):
                    continue
                next_energy = self.energy + (abs(i-room_exit) + 3 - len(self.rooms[room]))*ENERGY_LEVELS[top_amphoid]
                next_rooms = self.rooms.copy()
                next_rooms[room] = self.rooms[room][:-1]
                next_hallway = [top_amphoid if j == i else h for j, h in enumerate(self.hallway)]
                new_board = Boardstate(next_rooms, next_hallway, next_energy)
                next_states.append(new_board)
        return next_states

    def __repr__(self):
        if not self.rooms or not self.hallway:
            return "Empty board"
        return "h: {}, A: {}, B: {}, C: {}, D: {}"\
            .format(str(self.hallway), str(self.rooms["A"]), str(self.rooms["B"]),
                    str(self.rooms["C"]), str(self.rooms["D"]))

def insert_by_hueristic(queue, item):
    for i, queue_item in enumerate(queue):
        if queue_item.h < item.h:
            queue.insert(i, item)
            return
    queue.append(item)

def find_lowest_energy(board):
    queue = [board]
    res = float("inf")
    visited = dict()
    while queue:
        current_board = queue.pop(0)
        if current_board.__hash__() in visited and visited[current_board.__hash__()] <= current_board.energy:
            continue
        visited[current_board.__hash__()] = current_board.energy
        if current_board.is_over():
            res = min(res, current_board.energy)
            continue
        for next_board in current_board.get_next_states():
            if next_board.energy >= res:
                continue
            insert_by_hueristic(queue, next_board)
    return res

def find_lowest_energy_dfs(board, visited, currentbest):
    visited[board.__hash__()] = board.energy
    if board.is_over():
        currentbest[0] = min(currentbest[0], board.energy)
        return board.energy
    res = float("inf")
    for next_board in sorted(board.get_next_states(), key=lambda x: -x.h):
        if next_board.__hash__() in visited and visited[next_board.__hash__()] <= next_board.energy:
            continue
        if next_board.energy >= currentbest[0]:
            continue
        res = min(res, find_lowest_energy_dfs(next_board, visited, currentbest))
    return res

if __name__ == "__main__":
    board = open("input.txt").read().strip().split("\n")[1:]
    amphoids = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] in "ABCD":
                amphoids.append([row, col, board[row][col]])
    rooms = dict()
    for amphoid in amphoids:
        amphoid_room = "ABCD"[(amphoid[1]-3)//2]
        if amphoid_room in rooms:
            rooms[amphoid_room].insert(0, amphoid[-1])
        else:
            rooms[amphoid_room] = [amphoid[-1]]
    hallway = [None]*(len(board[0])-2)

    startstate = Boardstate(rooms, hallway, 0)
    #print(find_lowest_energy_dfs(startstate, dict(), [15000]))
    print(find_lowest_energy(startstate))


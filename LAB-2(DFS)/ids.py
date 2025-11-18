goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def neighbors(state):
    x, y = find_blank(state)
    result = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new = [row[:] for row in state]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            result.append(new)
    return result

def dls(state, path, limit):
    if state == goal:
        return path
    if limit == 0:
        return None
    for nb in neighbors(state):
        if nb not in path:
            res = dls(nb, path + [nb], limit - 1)
            if res: return res
    return None

def ids(start, maxd=20):
    for d in range(maxd+1):
        res = dls(start, [start], d)
        if res: return res
    return None

start = [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]]

sol = ids(start)
if sol:
    print("IDS solved in", len(sol)-1, "moves")
    for s in sol:
        for r in s: print(r)
        print()
else:
    print("No solution")
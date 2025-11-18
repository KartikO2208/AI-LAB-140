from collections import deque

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def is_goal(state):
    return state == goal_state


def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors


def dfs(start_state, max_depth=50):
    stack = [(start_state, [start_state], 0)]
    visited = set()

    while stack:
        state, path, depth = stack.pop()
        state_tuple = tuple(tuple(row) for row in state)

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if is_goal(state):
            return path

        if depth < max_depth:
            for neighbor in get_neighbors(state):
                stack.append((neighbor, path + [neighbor], depth + 1))

    return None


start = [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]]

solution = dfs(start)
if solution:
    print("DFS Solution found in", len(solution) - 1, "moves:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")

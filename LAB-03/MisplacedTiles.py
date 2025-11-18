import heapq

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

def misplaced(state):
    return sum(state[i][j] != 0 and state[i][j] != goal[i][j]
               for i in range(3) for j in range(3))



def to_tuple(state): return tuple(num for row in state for num in row)

def neighbors(state):
    x,y = [(i,j) for i in range(3) for j in range(3) if state[i][j]==0][0]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for dx,dy in dirs:
        nx,ny = x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            new = [row[:] for row in state]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            yield new

def a_star(start, h):
    pq = []
    heapq.heappush(pq,(h(start),0,start))
    seen = {to_tuple(start):0}
    while pq:
        f,g,state = heapq.heappop(pq)
        if state == goal:
            return g
        for nb in neighbors(state):
            ng = g+1
            t = to_tuple(nb)
            if ng < seen.get(t,1e9):
                seen[t] = ng
                heapq.heappush(pq,(ng+h(nb),ng,nb))
    return -1

start = [[1,2,3],
         [0,4,6],
         [7,5,8]]

print("Steps with Misplaced Tiles:", a_star(start, misplaced))

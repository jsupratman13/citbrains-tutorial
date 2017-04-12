grid = [[0,1,0,0,0,0],
        [0,1,0,0,0,0],
        [0,0,0,0,1,0],
        [0,1,1,1,1,0],
        [0,0,0,0,1,0]]

goal = [len(grid)-1,len(grid[0])-1]
cost = 1

delta = [[-1, 0], #go up
        [0, -1], #go left
        [ 1, 0], #go down
        [ 0, 1]] #go rught

delta_name = ['^','<','V', '>']

def compute_value(grid, goal, cost):
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True
    while change:
        change = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y] = '*'
                        change = True
                elif grid[x][y] == 0:
                    for i in range(len(delta)):
                        x2 = x + delta[i][0]
                        y2 = y + delta[i][1]
                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2]==0:
                            v2 = value[x2][y2] + cost
                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2
                                policy[x][y] = delta_name[i]

    return value,policy

val,pol = compute_value(grid,goal,cost)
for v in val:
    print v

for p in pol:
    print p

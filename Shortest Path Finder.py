from collections import deque


def shortest_path(maze, start, end):
    if maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1:
        return None  # Start or end points are walls

    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = deque([(start, 0)])  # (position, distance)

    while queue:
        (x, y), dist = queue.popleft()

        if (x, y) == end:
            return dist  # Found the shortest path

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), dist + 1))

    return None  # No path found


# Example maze represented as a 2D grid (0 represents empty cell, 1 represents wall)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

start_point = (0, 0)
end_point = (4, 4)

shortest_dist = shortest_path(maze, start_point, end_point)
if shortest_dist is not None:
    print("Shortest distance from start to end:", shortest_dist)
else:
    print("No path found from start to end.")

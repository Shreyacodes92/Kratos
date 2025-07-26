"""
Rover Object Model
Author: Shreya Dharwad
Description: A simulation of a rover moving across a grid using object-oriented programming.
Includes classes for Position, Map, and Rover with battery constraints and traversal logic.
"""

class Position:
    def _init_(self, x, y, traversable=True):
        self.x = x
        self.y = y
        self.traversable = traversable

class Map:
    def _init_(self, width, height, blocked_positions=None):
        self.grid = [[Position(x, y) for y in range(height)] for x in range(width)]
        if blocked_positions:
            for x, y in blocked_positions:
                self.grid[x][y].traversable = False

    def is_traversable(self, x, y):
        return (
            0 <= x < len(self.grid)
            and 0 <= y < len(self.grid[0])
            and self.grid[x][y].traversable
        )

class Rover:
    def _init_(self, start_pos):
        self.battery = 100
        self.position = start_pos

    def traverse(self, target_x, target_y, map_obj):
        from collections import deque

        start = (self.position.x, self.position.y)
        visited = set()
        queue = deque([(start[0], start[1], 0)])  # (x, y, steps)

        while queue:
            x, y, steps = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))

            if x == target_x and y == target_y:
                self.battery -= steps
                self.position = map_obj.grid[x][y]
                return steps

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if map_obj.is_traversable(nx, ny) and (nx, ny) not in visited:
                    queue.append((nx, ny, steps + 1))

        return -1  # No path found

# Example usage
if _name_ == "_main_":
    # Create a 5x5 map with some blocked positions
    my_map = Map(5, 5, blocked_positions=[(1, 1), (2, 2)])

    # Start position (0, 0)
    start_pos = my_map.grid[0][0]

    # Create rover and try to reach (4, 4)
    rover = Rover(start_pos)
    steps = rover.traverse(4, 4, my_map)

    print(f"Steps taken: {steps}")
    print(f"Remaining battery: {rover.battery}%")

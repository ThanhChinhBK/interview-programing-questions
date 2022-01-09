class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for instruction in instructions:
            if instruction == "L":
                dx, dy = dy, -dx 
            elif instruction == "R":
                dx, dy = -dy, dx
            else:
                x, y = x + dx, y + dy
        return (x ==0 and y == 0) or (dx != 0 or dy != 1)

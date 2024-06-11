from collections import defaultdict

class Solution:
    def trap(self, height: List[int]) -> int:
        # Find the heighst wall. 
        maxWallAt = height.index(max(height))
        water = 0
        print(maxWallAt)

        # Water will be trapped on the left side if there is at least one wall.
        leftWall = 0
        for i in range(0, maxWallAt):
            if height[i] > leftWall:
                leftWall = height[i]
            else:
                water += leftWall - height[i]

        # Water will be trapped on the right side if there is at least one wall.
        rightWall = 0
        for i in range(len(height) - 1, maxWallAt, -1):
            if height[i] > rightWall:
                rightWall = height[i]
            else:
                water += rightWall - height[i]
    
        return water




        




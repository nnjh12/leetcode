class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mem = {}
        return self.canJumpHelper(nums, 0, mem)
  
    def canJumpHelper(self, nums: List[int], start: int, mem: dict) -> bool:
        # If already visited:
        if mem.get(start) is not None:
            #print("already visited")
            return mem.get(start)

        n = len(nums) - start
        # Edge case
        if n < 2:
            #Wprint("case1-true")
            #mem[start] = True
            return True

        # Need to handle the case when nums[0] is 0.
        if nums[start] == 0:
            #print("case2-false")
            #mem[start] = False
            return False
        
        # If possible max jumps is greater or equal to distance to the last index
        if nums[start] >= n-1:
            #print("case3-true")
            #mem[start] = True
            return True

        # We can jump 1 to nums[0] if nums[i] is not 0.
        for i in range(1, nums[start] + 1):
            if self.canJumpHelper(nums, start + i, mem):
                return True
            else:
                mem[start] = False
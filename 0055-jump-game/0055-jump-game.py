class Solution:
    # Attemp2. linear
    def canJump(self, nums: List[int]) -> bool:
        energy = 0
        for num in nums:
            if energy < 0:
                return False
            # If num is greater than current energy,
            # upgrade energy to num.
            if num > energy:
                energy = num
            # To move to next num, we need to use 1 energy.
            energy -= 1
        
        # If we can iterate to the last num, return true.
        return True

    """
    # Attemp1. DP - not very efficient
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
    """
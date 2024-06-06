class Solution:
    def jump(self, nums: List[int]) -> int:
        mem = {}
        return self.jumpHelper(nums, 0, mem)

    def jumpHelper(self, nums: List[int], start: int, mem: dict) -> int:
        # If we have already visited this index before,
        # return the value.
        if mem.get(start) is not None:
            return mem.get(start)

        distance = len(nums) - start -1
        # If distance is less than 1,
        # we can arrive to the last index without any jump.
        if distance < 1:
            mem[start] = 0
            return 0
                
        energy = nums[start]
        # If we don't have any energy, we cannot arrive to the last index.
        if energy < 1:
            mem[start] = float('inf')
            return float('inf')
        
        # If energy is greater or equal to distance,
        # we can arrive to the last index from the current position.
        if energy >= distance:
            mem[start] = 1
            return 1
        
        # From the current position, we can jump from 1 to amount of energy.
        # Find the minimum jumps to arrive to the last index
        possibleJumps = [1 + self.jumpHelper(nums, start + i, mem) for i in range(1, energy + 1)]
        
        # for i in range(1, energy + 1):
        #     jump = self.jumpHelper(nums, start + i, mem)
        #     possibleJumps.append(jump)
        
        #[1 + self.jumpHelper(nums, start + i, mem) for i in range(1, energy + 1)]
        
        minJump = min(possibleJumps)
        mem[start] = minJump
        return minJump



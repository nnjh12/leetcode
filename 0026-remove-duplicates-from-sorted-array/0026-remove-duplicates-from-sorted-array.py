class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        cusor = 1 # next index to be overwritten
        start = 0 # starting index for finding next unique number

        while start < len(nums):
            start = self.findNextUniqueNumIndex(nums, start)
            if start < len(nums):
                nums[cusor] = nums[start]
                #print(cusor, start, nums)
                cusor += 1
        return cusor
    
    # find next unique number's index
    def findNextUniqueNumIndex(self, nums: List[int], start):
        if start >= len(nums):
            return start

        cur = nums[start]
        i = start + 1
        while i < len(nums):
            if nums[i] != cur:
                return i
            i += 1
        # if everything are duplicates, i will be len(nums)
        return i





class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # edge case
        if len(nums) <= 2:
            return len(nums)
        
        # the place where need to be written
        j = 2 

        for i in range(2, len(nums)):
            # if current element is not equal to element at j-2
            # need to compare i to j-2, because i-2 might be already overwritten,
            # and j-2 was the original element two index ahead from i.
            if nums[i] != nums[j-2]:
                # update element at j
                nums[j] = nums[i]
                j += 1

        return j
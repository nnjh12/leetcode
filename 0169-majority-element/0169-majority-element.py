from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count elements in nums 
        c = Counter(nums)

        # find element that has more than len(nums)/2
        filtered = [key for key, val in c.items() if val > len(nums)//2]
        return filtered[0]
        
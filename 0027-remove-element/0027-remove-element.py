class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        l = 0
        r = len(nums) - 1
        while l <= r:
            num1 = nums[l]
            num2 = nums[r]
            # case1. if num1 and num2 are same as val
            if num1 == val and num2 == val:
                r -= 1
                k -= 1
            # case2. if both num1 and num2 are not same as val
            elif num1 != val and num2 != val:
                l += 1
            # case3. if num1 is not val and num2 is val
            elif num1 != val and num2 == val:
                l += 1
                r -= 1
                k -= 1
            # case4. if num1 is val and num2 is not val
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                k -= 1
        return k




            
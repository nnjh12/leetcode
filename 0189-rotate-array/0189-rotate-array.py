class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # edge case
        if n < 2:
            return nums

        # minimize k value. If list contains 3 elements, k=4 has the same result with k=1.
        k = k % n

        # save last k elements
        temp = nums[n-k:n]
        
        # move first n-k elements
        nums[k:n] = nums[0:n-k]

        # append temp to first k positions
        nums[0: k] = temp

        """
        Attempt1. tried to have only two space holding one int each.
        Have bugs. nums = [1,2,3,4,5,6,7], k = 2
        Iterated index 0-3-6-1-4-2-5 but at some point the value was already updated and original value was lost.

        n = len(nums)

        for start in range(0, k):
            i = start
            cur = nums[i]

            while i < n:
                # find a new position
                j = (i + k) % n
                
                # save the new position value
                temp = nums[j]
                
                # move the element to the new position
                nums[j] = cur
                
                cur = temp                
                i += k
    """

                
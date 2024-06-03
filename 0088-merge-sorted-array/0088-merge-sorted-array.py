class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = 0
        i2 = 0
        while i1 < m+i2 and i2 < n:
            # if num1 is correctly positioned,
            if nums1[i1] <= nums2[i2]:
                # move to the next element in nums1
                i1 += 1
            # if num2 needs to be inserted to nums1
            else: 
                # push the elements from index i1 to the end of the array and empty at index i1.
                self.pushElements(nums1, i1, m+n-2)
                # insert num2 into nums1.
                nums1[i1] = nums2[i2]
                # move to the next elements in nums1 and nums2.
                i1 += 1
                i2 += 1
        
        # if there are more elements left in nums2
        if i2 < n:
            # copy the remaining elements in nums2 to nums1.
            nums1[i1:] = nums2[i2:]
    
    # push elements at index i from start to end(inclusive) at index i+1
    def pushElements(self, arr, start, end):
        if start > end or end + 1 >= len(arr):
            print("end index out of bound")
            return
        i = end
        while i >= start:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = 0
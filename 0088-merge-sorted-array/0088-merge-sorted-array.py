class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = 0
        i2 = 0
        while i1 < m+i2 and i2 < n:
            if nums1[i1] <= nums2[i2]:
                i1 += 1
            else: 
                print('else')
                self.pushElements(nums1, i1, m+n-2)
                nums1[i1] = nums2[i2]
                i1 += 1
                i2 += 1
            print(i1, i2, nums1, nums2)
        if i2 < n:
            nums1[i1:] = nums2[i2:]
    
    def pushElements(self, arr, start, end):
        if start > end or end + 1 >= len(arr):
            print("end index out of bound")
            return
        i = end
        while i >= start:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = 0
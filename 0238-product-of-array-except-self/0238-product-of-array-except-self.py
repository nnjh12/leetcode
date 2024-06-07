class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero = []
        mul = 1
        answer = []

        # Multiply all the numbers except 0.
        # Track where zero is located.
        for i, num in enumerate(nums):
            if num == 0:
                zero.append(i)
            else:
                mul = num * mul
        
        # If there are two or more than zero, all the elements become zero.
        if len(zero) > 1:
            answer = [0] * n
        # If there is only one zero, all the element except zero become zero.
        elif len(zero) == 1:
            answer = [0] * n
            i = zero[0]
            answer[i] = mul
        # If there is no zero, divide mul with num.
        else:
            for num in nums:
                answer.append(mul//num)
        
        return answer





        